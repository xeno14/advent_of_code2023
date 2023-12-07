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


class Map:

    def __init__(self, ranges: list[tuple[int, int, int]]) -> None:
        self.ranges = ranges
    
    def __call__(self, x: int) -> int:
        for dst, src, rng in self.ranges:
            if src <= x <= src + rng:
                return dst + x - src
        return x

    def __repr__(self) -> str:
        return 'Map(%s)' % self.ranges


def parse(s: str) -> tuple[list[int], list[Map]]:
    parts = s.strip().split('\n\n')

    seeds = list(map(int, parts[0].split(': ')[1].split()))

    maps = []
    for part in parts[1:]:
        ranges = []
        for line in part.split('\n')[1:]:
            ranges.append(list(map(int, line.split(' '))))
        m = Map(ranges)
        maps.append(m)
    return seeds, maps


def do_map(seed: int, maps: list[Map]) -> int:
    x = seed
    print('seed', seed)
    for m in maps:
        x = m(x)
        print(x)
    return x


def part1(s : str) -> int:
    seeds, maps = parse(s)

    return min(map(lambda seed: do_map(seed, maps), seeds))


assert (part1(EXAMPLE) == 35)
with open('../input/day05.txt') as f:
    print(part1(f.read()))
