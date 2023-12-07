import re
import collections


EXAMPLE1 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def is_possible(subgame: str) -> bool:
    counts = collections.defaultdict(int)
    for color in ('red', 'blue', 'green'):
        for n in map(int, re.findall(r'(\d+) ' + color, subgame)):
            counts[color] += n
    # print(counts)
    return counts['red'] <= 12 and counts['green'] <= 13 and counts['blue'] <= 14


def part1(s :str) -> int:
    possible_ids: list[int] = []

    for line in s.strip().split('\n'):
        m = re.findall(r'^Game (\d+)', line)[0]
        game_id = int(m)
        subgames = line.split(':')[1].split(';')
        if all(map(is_possible, subgames)):
            possible_ids.append(game_id)
    return sum(possible_ids)


def part2(s: str) -> int:
    ans = 0

    for line in s.strip().split('\n'):
        line = line.split(':')[1]
        counts = {c: 0 for c in ['red', 'green', 'blue']}
        for subgame in line.split(';'):
            for color in counts.keys():
                for n in map(int, re.findall(r'(\d+) ' + color, subgame)):
                    counts[color] = max(counts[color], n)
        # print(counts)
        power = 1
        for v in counts.values():
            power *= v
        ans += power

    return ans


assert(part1(EXAMPLE1) == 8)
with open('../input/day02.txt', 'r') as f:
    print(part1(f.read()))

assert(part2(EXAMPLE1) == 2286)
with open('../input/day02.txt', 'r') as f:
    print(part2(f.read()))
