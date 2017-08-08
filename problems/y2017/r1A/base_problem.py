import config
import numpy as np

from datetime import datetime

logger = config.logging.getLogger(__name__)


class BaseProblem:
    """

    """
    def __init__(self):
        self.start_time = datetime.utcnow()
        pass

    def log_runtime(self):
        elapsed_time = (datetime.utcnow() - self.start_time).total_seconds()
        logger.debug('Code run time = {:06.3f}s'.format(elapsed_time))

    def parse_input(self, input_filename):
        pass

    def initialize_case(self, input_text, case_number):
        result = ''
        return result

    def run(self, problem_letter, input_file):
        input_filename = '{}-{}.in'.format(problem_letter, input_file)
        output_filename = '{}-{}.out'.format(problem_letter, input_file)

        input_text = open(input_filename).read()
        input_text = input_text.split('\n')

        n_cases = int(input_text[0])

        result_dict = {}

        for case_number in range(1, n_cases + 1):
            result = self.initialize_case(input_text, case_number)
            result_dict[case_number] = result

        output_list = ['Case #{}: {}'.format(key, value) for key, value in result_dict.items()]
        output = '\n'.join(output_list)

        self.log_runtime()

        with open(output_filename, 'w') as text_file:
            text_file.write(output)
