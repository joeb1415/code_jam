import os
import numpy as np
import math

from datetime import datetime


def run(input_filename):
    input = open(input_filename).read()
    input = input.split('\n')

    n_cases = int(input[0])

    result_dict = {}

    for case in range(1, n_cases + 1):
        stack = input[case]
        binary_stack = make_binary(stack)
        flip_count = get_flip_count(binary_stack)
        result_dict[case] = flip_count

    output_list = ['Case #{}: {}'.format(key, value) for key, value in result_dict.items()]
    output = '\n'.join(output_list)

    return output


def make_binary(stack):
    binary = []
    for char in stack:
        if char == '-':
            binary.append(0)
        else:
            binary.append(1)
    return binary


def get_flip_count(binary_stack):
    flip_count = 0
    last_char = binary_stack[0]
    for char in binary_stack:
        if char == last_char:
            continue
        flip_count += 1
        last_char = char

    if last_char == 0:
        flip_count += 1

    return flip_count

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
