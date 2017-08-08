import os
import numpy as np

from datetime import datetime


def run(input_filename):
    input = open(input_filename).read()
    input = input.split('\n')

    n_cases = int(input[0])

    result_dict = {}

    for case in range(1, n_cases + 1):
        orig_len, iterations, samples = tuple(map(int, input[case].split(' ')))
        test_tiles = get_test_tiles(orig_len, iterations, samples)
        tile_str = format_tiles(test_tiles)
        result_dict[case] = tile_str

    output_list = ['Case #{}: {}'.format(key, value) for key, value in result_dict.items()]
    output = '\n'.join(output_list)

    return output


def get_test_tiles(orig_len, iterations, samples):
    """
    GGG GGGGGGGGG
    GGL GGGGGGGGL
    GLG GGGGLGGGG
    GLL GGGGLLGLL
    LGG LGGGGGGGG
    LGL LGLGGGLGL
    LLG LLGLLGGGG
    LLL LLLLLLLLL
    """
    if samples > orig_len:
        raise Exception('samples must be <= original length')

    if samples == orig_len:
        test_tiles = [x + 1 for x in range(samples)]
        return test_tiles

    if samples == orig_len - 1:
        if iterations == 1:
            return 'IMPOSSIBLE'

        test_tiles = [x + 2 for x in range(samples)]
        return test_tiles

    return 'IMPOSSIBLE'


def format_tiles(test_tiles):
    if isinstance(test_tiles, list):
        return ' '.join(map(str, test_tiles))

    return test_tiles


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
