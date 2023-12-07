from typing import Any
import numpy as np
import multiprocessing


EXAMPLE = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def parse(s: str):
    parts = s.strip().split('\n\n')

    seeds = parts[0].split(': ')[1].split()
    print('std::vector<int> seeds = {%s};' % (
        ', '.join(seeds)
    ))
    print('std::vector<std::vector<std::tuple<int64_t, int64_t, int64_t>>> maps {')

    for part in parts[1:]:
        print('  {')
        for line in part.split('\n')[1:]:
            print('   {%s},' % ', '.join(line.split()))
        print('  },')
    print('};')



# parse(EXAMPLE)
with open('../input/day05.txt') as f:
    print(parse(f.read()))
