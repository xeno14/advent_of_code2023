import math
import re
import itertools

EXAMPLE1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

EXAMPLE2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

EXAMPLE3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


G = dict[str, tuple[str, str]]

def parse(s: str) -> tuple[str, G]:
    lines = s.strip().split('\n')
    g: G = {}
    for line in lines[2:]:
        m = re.findall(r'(.+) = \((.+), (.+)\)', line)
        a, b, c = m[0]
        g[a] = (b, c)
    return lines[0], g


def part1(s: str) -> int:
    step = 0

    instruction, g = parse(s)
    pos = 'AAA'

    instruction = itertools.cycle(instruction)
    for nxt in instruction:
        if nxt == 'L':
            pos = g[pos][0]
        else:
            pos = g[pos][1]
        step += 1
        if pos == 'ZZZ':
            break
    return step


def part2(s: str) -> int:
    instruction, g = parse(s)

    ans = 1

    for pos in [k for k in g if k.endswith('A')]:
        step = 0
        for nxt in itertools.cycle(instruction):
            if nxt == 'L':
                pos = g[pos][0]
            else:
                pos = g[pos][1]
            step += 1
            if pos.endswith('Z'):
                break
        ans = math.lcm(ans, step)
    return ans
    

assert part1(EXAMPLE1) == 2
assert part1(EXAMPLE2) == 6
with open('../input/day08.txt') as f:
    print(part1(f.read()))

assert part2(EXAMPLE3) == 6
with open('../input/day08.txt') as f:
    print(part2(f.read()))