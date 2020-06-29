import logging
try:
  basestring
except NameError:
  basestring = str


__all__ = ["Plugin", "FloatPlugin", "StringPlugin", "IntegerPlugin"]


logger = logging.getLogger(__name__)


class PluginBase(object):
    name = None
    default_options = ""
    required_options = []

    def __init__(self, options=None):
        if options is None:
            options = self.default_options
        if isinstance(options, basestring):
            if options:
                options = options.split(" ")
            else:
                options = []
        self.options = self.required_options + options

    def get_params_list(self):
        params = [self.name]
        if self.options:
            params.extend(self.options)
        return params

    def get_params(self):
        return " ".join(self.get_params_list())


class Plugin(PluginBase):
    default_result_keys = []
    result_columns_num = 1
    result_column_offset = 0
    coerce = float

    def __init__(self, result_keys=None, *args, **kwargs):
        if result_keys is None:
            result_keys = self.default_result_keys[:]
        self.result_keys = result_keys
        super(Plugin, self).__init__(*args, **kwargs)

    def get_result_columns_num(self):
        return self.result_columns_num

    def get_result_column_offset(self):
        return self.result_column_offset

    def get_result_values(self, values):
        """
        :param values: list of values coming from this plugin
        """
        offset = self.result_column_offset
        values = values[offset:offset + len(self.result_keys)]
        _values = []
        for value in values:
            if "FAILED" in value:
                value = None
                logger.warning("%s failed: %s", self.name, values)
            elif value == '\xe2\x88\x9e':
                # XXX INF?
                logger.info("%s value is inf: %s", self.name, values)
                value = None
            elif value == "":
                logger.info("%s empty value: %s", self.name, values)
                value = None
            else:
                try:
                    value = self.coerce(value)
                except Exception as e:
                    logger.error("%s coerce error | value: %s", self.name, value)
                    logger.exception(e)
                    value = None
            _values.append(value)
        return list(zip(self.result_keys, _values))


FloatPlugin = Plugin


class StringPlugin(Plugin):
    #coerce = unicode
    coerce = str


class IntegerPlugin(Plugin):
    coerce = int


class SDFPlugin(PluginBase):
    required_options = ["-f", "sdf"]
