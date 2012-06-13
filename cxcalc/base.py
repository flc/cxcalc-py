import os
import subprocess
import threading
import logging
from subprocess import Popen, PIPE


class Calculator(object):
    default_bin_path = os.path.join(
        os.environ["VIRTUAL_ENV"], "marvinbeans", "bin", "cxcalc"
        )
    default_options = "-N h -i ID"

    def __init__(self, plugins, options=None, bin_path=None, callback=None):
        self.plugins = plugins

        if options is None:
            options = self.default_options
        self.options = options

        if bin_path is None:
            bin_path = self.default_bin_path
        assert os.path.isfile(bin_path)
        self.bin_path = bin_path

        self._callback = callback

        self._all_columns_num = self.get_all_columns_num()
        self._process = None

    def create_process(self):
        command = self.get_params_list()
        logger.debug("command: %s", command)
        return subprocess.Popen(
                                self.get_params_list(),
                                shell=False,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                )

    def get_process(self):
        if self._process is None:
            self._process = self.create_process()
        return self._process

    def get_params_list(self):
        params = [self.bin_path]
        params.extend(self.options.split(" "))
        for prop in self.plugins:
            params.extend(prop.get_params_list())
        return params

    def get_params(self):
        return " ".join(self.get_params_list())

    def callback(self, data):
        logger.debug("callback data: %s", data)
        if self._callback is not None:
            self._callback(data)

    def get_all_columns_num(self):
        columns_num = 1  # id + plugin columns
        for plugin in self.plugins:
            columns_num += plugin.get_result_columns_num()
        return columns_num

    def process_line(self, line):
        #values = line.strip().split("\t")
        values = [v.strip() for v in line.split("\t")]
        logger.debug("line values: %s | len: %s", values, len(values))
        #print values
        _id = values[0]

        data = {
            "id": _id,
        }

        failed = False
        if len(values) != self._all_columns_num:
            logger.error("Column number mismatch: %s "
                         "| actual len: %s | should be: %s",
                         values, len(values), self._all_columns_num)
            failed = True

        if not failed:
            current = 1
            for plugin in self.plugins:
                column_num = plugin.get_result_columns_num()
                _from = current
                _to = current + column_num
                plugin_values = values[_from:_to]
                current = _to
                logger.debug("plugin values (%s): %s", plugin.name, plugin_values)
                try:
                    plugin_data = plugin.get_result_values(plugin_values)
                except Exception, e:
                    logger.exception(e)
                    logger.debug('exception | line: %s', line)
                    logger.debug('exception | values: %s', values)
                    raise
                    #return {}
                else:
                    data.update(plugin_data)

        self.callback(data)

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
                logger.debug("line: %s", line.replace("\t", "<TAB>"))
                self.process_line(line)

    def _write(self, process, iterable):
        stdin = process.stdin
        write = stdin.write
        flush = stdin.flush
        for el in iterable:
            write(el)
            flush()
        stdin.close()

    def run(self, iterable):
        process = self.create_process()

        self._run(process, iterable)

        process.wait()

        process.stdout.close()
        process.stderr.close()

        status = process.returncode

        return status

    def _run(self, process, iterable):
        out_buff = None
        error_buff = None
        #if capture:
            #out_buff = []
            #error_buff = []

        writer_thread = threading.Thread(target=self._write,
                                         args=(process, iterable))
        writer_thread.daemon = True

        reader_thread = threading.Thread(
                                    target=self._read,
                                    args=(process.stdout.read, out_buff)
                                    )
        reader_thread.daemon = True

        error_reader_thread = threading.Thread(
                                    target=self._read,
                                    args=(process.stderr.read, error_buff)
                                    )
        error_reader_thread.daemon = True

        threads = [writer_thread, reader_thread, error_reader_thread]
        for th in threads:
            th.start()
        for th in threads:
            th.join()

    #def run_(self, mol_iterator):
        #process = self.create_process()
        #inp = "\n".join(list(mol_iterator))
        #output = process.communicate(input=inp)[0]
        #from cStringIO import StringIO
        #out = StringIO(output)
        #self._read(out.read)



