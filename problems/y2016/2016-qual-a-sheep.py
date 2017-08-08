import os
import numpy as np

from datetime import datetime


def run(input_filename):
    input = open(input_filename).read()
    input = input.split('\n')

    n_cases = int(input[0])

    result_dict = {}

    for case in range(1, n_cases + 1):
        start = int(input[case])
        last_number = count_sheep(start)
        result_dict[case] = last_number

    output_list = ['Case #{}: {}'.format(key, value) for key, value in result_dict.items()]
    output = '\n'.join(output_list)

    return output


def count_sheep(start):
    """
    Small dataset: 0 <= start <= 200
    Large dataset: 0 <= N <= 10^6
    """
    if not isinstance(start, int):
        raise Exception('start must be int')
    if start == 0:
        return 'INSOMNIA'

    last_number = start
    multiply = 1
    digits = set()
    while len(digits) < 10:
        last_number = multiply * start
        new_digits = set(map(int, list(str(last_number))))
        digits = digits.union(new_digits)
        multiply += 1

    return last_number




# generic

def get_filenames():
    path_parts = __file__.split(os.path.sep)
    filename = path_parts[-1].split('.')[0]  # right part is '.py'
    input_filename = os.path.sep.join(path_parts[:-1] + [filename + '.in'])
    output_filename = os.path.sep.join(path_parts[:-1] + [filename + '.out'])

    return input_filename, output_filename


def print_runtime(start_time):
    run_seconds = (datetime.now() - start_time).total_seconds()
    print('Code run time = {:02.0f}:{:02.0f}:{:06.3f}'.format(
        np.floor(run_seconds / 3600),
        np.floor((run_seconds % 3600) / 60),
        run_seconds % 60)
    )
    return


if __name__ == '__main__':
    start_time = datetime.now()
    input_filename, output_filename = get_filenames()

    output = run(input_filename)

    print_runtime(start_time)
    with open(output_filename, 'w') as text_file:
        text_file.write(output)
