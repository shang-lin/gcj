
class CodeJamUtils(object):

    @staticmethod
    def convert_type(val):
        try:
            v = int(val)
            return v
        except ValueError:
            try:
                v = float(val)
                return v
            except ValueError:
                   return val

    @staticmethod
    def parse_int(line):
        return int(line.rstrip())

    @staticmethod
    def parse(line):
        return [CodeJamUtils.convert_type(v) for v in line.rstrip().split()]