import os
import subprocess
import threading
import logging
from subprocess import Popen, PIPE


logger = logging.getLogger(__name__)


class Calculator(object):
    default_bin_path = os.path.join(
        os.environ["VIRTUAL_ENV"], "marvinbeans", "bin", "cxcalc"
        )
    default_options = "-N h -i ID"

    def __init__(self, plugins, options=None, bin_path=None):
        self.plugins = plugins

        if options is None:
            options = self.default_options
        self.options = options

        if bin_path is None:
            bin_path = self.default_bin_path
        assert os.path.isfile(bin_path)
        self.bin_path = bin_path

    def create_process(self):
        command = self.get_params_list()
        logger.debug("command: %s", command)
        process = subprocess.Popen(
                            self.get_params_list(),
                            #shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
        return process

    def get_params_list(self):
        params = [self.bin_path]
        params.extend(self.options.split(" "))
        for prop in self.plugins:
            params.extend(prop.get_params_list())
        return params

    def get_params(self):
        return " ".join(self.get_params_list())

    def process_line(self, line):
        values = line.strip().split("\t")

        try:
            _id = int(values[0])
        except ValueError:
            return {}

        data = {
            "id": _id,
        }

        current = 1
        for plugin in self.plugins:
            column_num = plugin.get_result_columns_num()
            _from = current
            _to = current + column_num
            plugin_values = values[_from:_to]
            current = _to
            try:
                plugin_data = plugin.get_result_values(plugin_values)
            except Exception, e:
                #log.exception(e)
                #log.debug('line: %s', line)
                #log.debug('fields: %s', fields)
                raise
                #return {}
            else:
                data.update(plugin_data)

        return data

    def _read(self, reader_func, buff=None):
        chars = []
        while True:
            char = reader_func(1)
            if char == "":
                break
            chars.append(char)
            if char == "\n":
                line = "".join(chars)
                if buff is not None:
                    buff.append(line.rstrip())
                chars = []
                logger.debug("line: %s", line)
                self.process_line(line)
                #yield line

    def _write(self, process, iterator):
        for el in iterator:
            process.stdin.write(el + "\n")
            process.stdin.flush()

    #def run(self, mol_iterator):
        #process = self.create_process()


        #w_thread = threading.Thread(target=self._write,
                                    #args=(process, mol_iterator))
        #w_thread.daemon = True


        #stdout_buff = []
        #r_thread = threading.Thread(target=self._read,
                                  #args=(process.stdout.read, stdout_buff))
        #r_thread.daemon = True


        #threads = [w_thread, r_thread]
        #for th in threads:
            #th.start()
        #for th in threads:
            #th.join()

        #process.wait()
        ##process.stdout.close()
        ##process.stderr.close()
        #status = process.returncode
        #print stdout_buf
        #return status

    def run(self, mol_iterator):
        process = self.create_process()
        inp = "\n".join(list(mol_iterator))
        output = process.communicate(input=inp)[0]
        from cStringIO import StringIO
        out = StringIO(output)
        self._read(out.read)

