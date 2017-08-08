import sys
import argparse

import config

from a import BaseProblem as ProblemA
from b import BaseProblem as ProblemB
from c import BaseProblem as ProblemC

logger = config.logging.getLogger(__name__)


def get_problem(problem_letter):
    try:
        if problem_letter == 'A':
            problem = ProblemA()
        elif problem_letter == 'B':
            problem = ProblemB()
        elif problem_letter == 'C':
            problem = ProblemC()
        else:
            raise NotImplementedError("Problem Letter must be one of: 'A', 'B', or 'C'.")
    except NotImplementedError as e:
        pass
    else:
        return problem, problem_letter


def get_input_file(input_file):
    try:
        if input_file in ['', 'sample']:
            input_file = 'sample'
        elif input_file in ['s', 'small']:
            input_file = 'small'
        elif input_file in ['l', 'large']:
            input_file = 'large'
        else:
            raise NotImplementedError("Input File must be one of: '' or 'sample', 's' or 'small', or 'l' or 'large'.")
    except NotImplementedError as e:
        pass
    else:
        return input_file


def main():
    logger.debug('Begin.')

    parser = argparse.ArgumentParser(description='Problem Letter (A, B, C) and Input File size (sample, small, large).')
    parser.add_argument(dest='problem_letter', help='A, B, or C.')
    parser.add_argument(dest='input_file', help='sample, small, large.')
    args = parser.parse_args()

    problem, problem_letter = get_problem(args.problem_letter)
    input_file = get_input_file(args.input_file)

    problem.run(problem_letter, input_file)

    logger.debug('End.')


if __name__ == '__main__':
    main()
