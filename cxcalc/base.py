import logging
import os
import subprocess
import threading
from subprocess import Popen, PIPE

from .plugins import SDFPlugin


logger = logging.getLogger(__name__)


class Base(object):
    default_bin_path = os.path.join(
        os.environ["VIRTUAL_ENV"], "marvinbeans", "bin", "cxcalc"
        )
    default_options = ""

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
        self._process = None

        self.validate()

    def validate(self):
        pass

    def callback(self, data):
        logger.debug("callback data: %s", data)
        if self._callback is not None:
            self._callback(data)

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
        if self.options:
            params.extend(self.options.split(" "))
        for plugin in self.plugins:
            params.extend(plugin.get_params_list())
        return params

    def get_params(self):
        return " ".join(self.get_params_list())

    def _write(self, process, iterable):
        stdin = process.stdin
        write = stdin.write
        flush = stdin.flush
        for el in iterable:
            write(el)
            flush()
        stdin.close()

    def process_line(self, line):
        pass

    def _read(self, reader_func, buff=None, err=False):
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
                if err:
                    log_func = logger.warning
                else:
                    log_func = logger.debug
                log_func("%s line: %s",
                         "stderr" if err else "stdout",
                         line)
                if not err:
                    logger.debug("%s line: %s",
                                 "stderr" if err else "stdout",
                                 line.replace("\t", "<TAB>"))
                if not err:
                    self.process_line(line)


    def create_writer_thread(self, process, iterable):
        writer_thread = threading.Thread(target=self._write,
                                         args=(process, iterable))
        writer_thread.daemon = True
        return writer_thread

    def create_reader_thread(self, process, out_buff):
        reader_thread = threading.Thread(
                                    target=self._read,
                                    args=(process.stdout.read, out_buff, False)
                                    )
        reader_thread.daemon = True
        return reader_thread

    def create_error_reader_thread(self, process, error_buff):
        error_reader_thread = threading.Thread(
                                    target=self._read,
                                    args=(process.stderr.read, error_buff, True)
                                    )
        error_reader_thread.daemon = True
        return error_reader_thread

    def _run(self, process, iterable):
        out_buff = None
        error_buff = None
        #if capture:
            #out_buff = []
            #error_buff = []

        writer_thread = self.create_writer_thread(process, iterable)
        reader_thread = self.create_reader_thread(process, out_buff)
        error_reader_thread = self.create_error_reader_thread(process, error_buff)

        threads = [writer_thread, reader_thread, error_reader_thread]
        for th in threads:
            th.start()
        for th in threads:
            th.join()

    def run(self, iterable):
        process = self.create_process()

        self._run(process, iterable)

        process.wait()

        process.stdout.close()
        process.stderr.close()

        status = process.returncode

        return status


class Calculator(Base):
    """For table output"""
    default_options = "-N h -i ID"

    def __init__(self, *args, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)

        self._all_columns_num = self.get_all_columns_num()

    def get_all_columns_num(self):
        columns_num = 1  # id + plugin columns
        for plugin in self.plugins:
            columns_num += plugin.get_result_columns_num()
        return columns_num

    def process_line(self, line):
        #values = line.strip().split("\t")
        values = [v.strip() for v in line.split("\t")]
        logger.debug("line values: %s | len: %s", values, len(values))
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


class CollectMixin(object):

    def __init__(self, *args, **kwargs):
        super(CollectMixin, self).__init__(*args, **kwargs)
        self._data = []

    def callback(self, data):
        self._data.append(data)

    def get_data(self):
        return self._data


class CollectCalculator(CollectMixin, Calculator):
    pass



class SDFCalculator(Base):
    """For table output"""

    def __init__(self, *args, **kwargs):
        super(SDFCalculator, self).__init__(*args, **kwargs)
        self._current_sdf_lines = []

    def validate(self):
        for plugin in self.plugins:
            if not isinstance(plugin, SDFPlugin):
                raise AssertionError("You can only use SDFPlugins")

    def process_line(self, line):
        self._current_sdf_lines.append(line)
        if line.startswith('$$$$'):
            self.callback(self._current_sdf_lines)
            self._current_sdf_lines = []


class CollectSDFCalculator(CollectMixin, SDFCalculator):
    pass
