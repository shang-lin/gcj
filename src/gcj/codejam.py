import re
import sys

from .utils import CodeJamUtils


class CodeJam(object):

    def __init__(self, func):
        """ Sets the solver function and the input and output file names. """

        if len(sys.argv) < 2:
            print("Input file not specified.")
            sys.exit()
        self.input_file = sys.argv[1]

        # If no output file is provided, construct it from the input filename.
        # If the input filename ends with the suffix ".in", replace the suffix with ".out".from
        # Otherwise, append .out to the input filename.
        if len(sys.argv) < 3:
            # Contruct output file name from input file
            if self.input_file.endswith('.in'):
                self.output_file = re.sub('.in$', '.out', sys.argv[1])
            else:
                self.output_file = self.input_file + '.out'
        else:
            self.output_file = sys.argv[2]
        self.solver_fn = func


    def run(self):
        with open(self.input_file, 'r') as infile:
            with open(self.output_file, 'w') as outfile:
                total_cases = CodeJamUtils.parse_int(infile.readline())
                ncase = 1
                for line in infile:
                    values = CodeJamUtils.parse(line)
                    result = self.solver_fn(*values)
                    outfile.write('Case #{}: {}\n'.format(ncase, result))
                    ncase += 1


