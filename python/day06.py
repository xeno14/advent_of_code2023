import re
import numpy as np

EXAMPLE="""
Time:      7  15   30
Distance:  9  40  200    
"""


def part1(s: str) -> int:
    lines = s.strip().split('\n')

    time_list = map(int, re.split(r'\s+',lines[0])[1:])
    distance_list = map(int, re.split(r'\s+',lines[1])[1:])

    ans = 1
    for time, distance in zip(time_list, distance_list):
        count = 0
        for v in range(time+1):
            count += (v * (time - v) > distance)
            
        ans *= count

    return ans

def part2(s: str) -> int:
    line1, line2 = s.strip().replace(' ', '').split('\n')
    time = int(line1.split(':')[1])
    distance = int(line2.split(':')[1])

    v = np.arange(time+1, dtype=np.int64)
    return np.sum(v * (time - v) > distance)


print(part1(EXAMPLE))
with open('../input/day06.txt') as f:
    print(part1(f.read()))

print(part2(EXAMPLE))
with open('../input/day06.txt') as f:
    print(part2(f.read()))