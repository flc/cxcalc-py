from .base import FloatPlugin


class LogP(FloatPlugin):
    """Logarithm of the octanol/water partition coefficient"""
    name = "logp"
    default_result_keys = ["logp"]


class LogD(FloatPlugin):
    """Logarithm of the octanol/water distribution coefficient
    (default at pH=7.4)"""
    name = "logd"
    default_options = "-H 7.4"
    default_result_keys = ["logd"]

