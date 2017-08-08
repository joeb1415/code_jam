import os
import numpy as np

from datetime import datetime

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def initialize_case(input, case):
    party_count = int(input[case * 2 - 1])
    count_per_party = map(int, input[case * 2].split(' '))
    party_dict = dict(zip(alphabet[:party_count], count_per_party))

    evacuation_sequence = evacuate(party_dict)

    return evacuation_sequence


def evacuate(party_dict):
    """
    Small dataset

    2 ≤ N ≤ 3.
    sum of all Pi ≤ 9.
    Large dataset

    2 ≤ N ≤ 26.
    sum of all Pi ≤ 1000.
    """

    total_senators = sum(party_dict.values())

    party_count_dist = {}
    for party, count in party_dict.items():
        if count in party_count_dist:
            party_count_dist[count].add(party)
        else:
            party_count_dist[count] = set(party)

    largest_party_count = max(party_count_dist.keys())  # which is also = max(party_dict.values())

    evacuation_sequence = []

    while total_senators > 0:
        evac_1 = party_count_dist[largest_party_count].pop()

        if (largest_party_count - 1) not in party_count_dist:
            party_count_dist[largest_party_count - 1] = set()

        party_count_dist[largest_party_count - 1].add(evac_1)

        total_senators -= 1

        # if two single senators left, don't take just 1 of them
        if largest_party_count == 1 and len(party_count_dist[largest_party_count]) == 2:
            evac_2 = ''
        elif len(party_count_dist[largest_party_count]) > 0:
            evac_2 = party_count_dist[largest_party_count].pop()
            party_count_dist[largest_party_count - 1].add(evac_2)
            total_senators -= 1

            if len(party_count_dist[largest_party_count]) == 0:
                party_count_dist.pop(largest_party_count)  # no more parties have this many senators remaining
                largest_party_count -= 1
        else:
            party_count_dist.pop(largest_party_count)  # no more parties have this many senators remaining
            largest_party_count -= 1
            evac_2 = ''

        evac_pair = evac_1 + evac_2

        evacuation_sequence.append(evac_pair)

    evacuation_sequence_str = ' '.join(evacuation_sequence)

    return evacuation_sequence_str


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


def run(input_filename):
    input = open(input_filename).read()
    input = input.split('\n')

    n_cases = int(input[0])

    result_dict = {}

    for case in range(1, n_cases + 1):
        result = initialize_case(input, case)
        result_dict[case] = result

    output_list = ['Case #{}: {}'.format(key, value) for key, value in result_dict.items()]
    output = '\n'.join(output_list)

    return output


if __name__ == '__main__':
    start_time = datetime.now()
    input_filename, output_filename = get_filenames()

    output = run(input_filename)

    print_runtime(start_time)
    with open(output_filename, 'w') as text_file:
        text_file.write(output)
