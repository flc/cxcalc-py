import logging


__all__ = ["Plugin", "FloatPlugin", "StringPlugin", "IntegerPlugin"]


logger = logging.getLogger(__name__)


class Plugin(object):
    name = None
    default_options = ""
    default_result_keys = []
    result_columns_num = 1
    result_column_offset = 0
    coerce = float

    def __init__(self, result_keys=None, options=None):
        if result_keys is None:
            result_keys = self.default_result_keys[:]
        self.result_keys = result_keys

        if options is None:
            options = self.default_options
        if isinstance(options, basestring):
            if options:
                options = options.split(" ")
            else:
                options = []
        self.options = options

    def get_params_list(self):
        params = [self.name]
        params.extend(self.options)
        return params

    def get_params(self):
        return " ".join(self.get_params_list())

    def get_result_columns_num(self):
        return self.result_columns_num

    def get_result_column_offset(self):
        return self.result_column_offset

    def get_result_values(self, values):
        """
        :param values: list of values coming from this plugin
        """
        print self.coerce
        print values
        try:
            value = values[self.result_column_offset]
        except IndexError:
            value = None
        else:
            if "FAILED" in value:
                value = None
                logger.warning("%s failed: %s", self.name, values)
            elif value == '\xe2\x88\x9e':
                # XXX INF?
                value = None
            elif value == "":
                value = None
            else:
                value = self.coerce(value)
        return [
            (self.result_keys[0], value),
        ]


FloatPlugin = Plugin


class StringPlugin(Plugin):
    coerce = unicode


class IntegerPlugin(Plugin):
    coerce = int
