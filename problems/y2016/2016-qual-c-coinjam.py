import os
import numpy as np
import math

from datetime import datetime


def run(input_filename):
    input = open(input_filename).read()
    input = input.split('\n')

    n_cases = int(input[0])

    length, count = tuple(map(int, input[1].split(' ')))
    start_int, end_int = get_params(length)
    coin_list = get_coin_list(start_int, end_int, count)

    coin_list_2 = [key + ' ' + ' '.join(map(str, value)) for key, value in coin_list.items()]
    coin_list_3 = '\n'.join(coin_list_2)
    output = 'Case #1:\n' + coin_list_3

    return output


def get_params(length):
    """build binary strings 100..001 and 111..111, interpret as ints, return range"""
    start_str = '1' + '0'*(length-2) + '1'
    end_str = '1' * length

    start_int = int(start_str, 2)
    end_int = int(end_str, 2)

    return start_int, end_int


def get_coin_list(start_int, end_int, count):
    coin_list = {}
    for coin in range(start_int, end_int + 1, 2):  # by 2's, so always 1xxx1
        bin_str = bin(coin)[2:]  # strip '0b' off start
        factor_list = get_factor_list(bin_str)
        if factor_list is None:
            continue
        coin_list[bin_str] = factor_list

        if len(coin_list) == count:
            return coin_list

    return None


def get_factor_list(bin_str):
    """
    translate binary string into ints as interpreted in bases 2-10
    return a factor for that base-translated composite number
    if any of those 9 interpretations of the binary string are prime, return None
    """
    factor_list = []
    for base in range(2, 11):
        int_value = int(bin_str, base)
        factor = find_a_factor(int_value)
        if factor is None:
            return None

        factor_list.append(factor)

    return factor_list


def find_a_factor(value):
    """return a factor of a composite number, or 1 if prime"""
    for factor in range(2, int(math.sqrt(value)) + 1):
        if value % factor == 0:
            return factor

    return None


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
        text_file.write(output[:-1])  # strip last blank line
