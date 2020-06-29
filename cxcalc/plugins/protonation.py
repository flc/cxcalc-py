import logging


from .base import FloatPlugin, IntegerPlugin


logger = logging.getLogger(__name__)


class Pka(IntegerPlugin):
    """Number of negative charges on the major microspecies at pH=7.4;
    Number of positive charges on the major microspecies at pH=7.4;
    Total charge on the major microspecies at pH=7.4;
    Number of charges on the major microspecies at pH=7.4;
    Lowest acidic pKa;
    Highest basic pKa"""
    name = "pka"
    default_options = "-a 10 -b 10 -d large"
    default_result_keys = [
        "pka_negative", "pka_positive", "pka_total",
        "pka_number", "pka_strongest_acidic", "pka_strongest_basic"
        ]
    result_columns_num = 20 + 1

    def __init__(self, ph=None, *args, **kwargs):
        super(Pka, self).__init__(*args, **kwargs)
        if ph is None:
            ph = 7.4
        self.ph = ph

    def _get_param_value(self, default, param_names):
        params_list = self.get_params_list()

        value = default

        for name in param_names:
            try:
                index = params_list.index(name)
            except ValueError:
                continue
            else:
                value = int(params_list[index + 1])
                break

        return value

    def get_num_acidic_pka(self):
        return self._get_param_value(2, ["-a", "--na"])

    def get_num_basic_pka(self):
        return self._get_param_value(2, ["-b", "--nb"])

    def get_result_columns_num(self):
        """Reimplemented from Plugin.get_result_columns_num."""
        apka = self.get_num_acidic_pka()
        bpka = self.get_num_basic_pka()
        return apka + bpka + 1  # +1 is atoms

    def get_result_values(self, values):
        """Reimplemented from Plugin.get_result_values."""
        apka = self.get_num_acidic_pka()
        bpka = self.get_num_basic_pka()

        pka_neg_d = values[:apka]
        pka_strongest_acidic = None
        if not pka_neg_d:
            # it's empty
            pka_negative = 0
        elif 'FAILED' in pka_neg_d[0]:
            pka_negative = None
            logger.warning("pka negative failed: %s", values)
        else:
            float_values = [float(v) for v in pka_neg_d if v]
            pka_negative = len([v for v in float_values if v < self.ph])
            if float_values:
                pka_strongest_acidic = min(float_values)

        pka_pos_d = values[apka:apka+bpka]
        pka_strongest_basic = None
        if not pka_pos_d:
            # it's empty
            pka_positive = 0
        elif 'FAILED' in pka_pos_d[0]:
            pka_positive = None
            logger.warning("pka positive failed: %s", values)
        else:
            float_values = [float(v) for v in pka_pos_d if v]
            pka_positive = len([v for v in float_values if v > self.ph])
            if float_values:
                pka_strongest_basic = max(float_values)

        if pka_negative is None or pka_positive is None:
            pka_total = None
            pka_number = None
        else:
            pka_total = pka_positive - pka_negative
            pka_number = pka_positive + pka_negative

        return list(zip(self.result_keys, [
            pka_negative, pka_positive, pka_total,
            pka_number, pka_strongest_acidic, pka_strongest_basic,
            ]))


class AvgCharge(FloatPlugin):
    """Average charge of the microspecies population (at pH=7.4 by default)"""
    name = "averagemicrospeciescharge"
    default_result_keys = ["avg_charge"]
    result_columns_num = 2  # pH is in the first column
    result_column_offset = 1


class PI(FloatPlugin):
    """pI; pH value where the net charge of an ionizable molecule is zero"""
    name = "isoelectricpoint"
    default_result_keys = ["pi"]

