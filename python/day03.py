import pprint
import itertools

EXAMPLE1 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def parse_line(line: str) -> list[tuple[int, int]]:  # pos, number.
    i = 0
    num = 0
    tmp_pos = []
    res = []
    for i in range(len(line)):
        if line[i].isdigit():
            num = num*10 + int(line[i])
            tmp_pos.append(i)
        else:
            res.extend((pos, num) for pos in tmp_pos)
            tmp_pos.clear()
            num = 0
    if num > 0:
        res.extend((pos, num) for pos in tmp_pos)
        tmp_pos.clear()
    return res


def part1(s: str) -> int:
    ans = 0
    num_loc: dict[tuple[int, int], int] = {}

    lines = s.strip().split('\n')
    for row in range(len(lines)):
        for col, num in parse_line(lines[row]):
            num_loc[(row, col)] = num

    used = set()

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            c = lines[row][col]
            if c.isdigit():
                continue
            if c == '.':
                continue
            for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
                if dx == 0 and dy == 0:
                    continue
                if row + dx < 0 or col + dy < 0 or row + dx >= len(lines) or col + dy >= len(lines[row]):
                    continue
                nr = row + dx
                nc = col + dy
                num = num_loc.get((nr, nc))
                if not num or (nr, nc) in used:
                    continue

                nnc = nc
                while num_loc.get((nr, nnc)) == num:
                    used.add((nr, nnc))
                    nnc += 1
                nnc = nc
                while num_loc.get((nr, nnc)) == num:
                    used.add((nr, nnc))
                    nnc -= 1

                ans += num

    return ans
    

def part2(s: str) -> int:
    ans = 0
    num_loc: dict[tuple[int, int], int] = {}

    lines = s.strip().split('\n')
    for row in range(len(lines)):
        for col, num in parse_line(lines[row]):
            num_loc[(row, col)] = num

    used = set()

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            c = lines[row][col]
            if c != '*':
                continue

            nums = []
            for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
                if dx == 0 and dy == 0:
                    continue
                if row + dx < 0 or col + dy < 0 or row + dx >= len(lines) or col + dy >= len(lines[row]):
                    continue
                nr = row + dx
                nc = col + dy
                num = num_loc.get((nr, nc))
                if not num or (nr, nc) in used:
                    continue

                nnc = nc
                while num_loc.get((nr, nnc)) == num:
                    used.add((nr, nnc))
                    nnc += 1
                nnc = nc
                while num_loc.get((nr, nnc)) == num:
                    used.add((nr, nnc))
                    nnc -= 1

                nums.append(num)
            if len(nums) == 2:
                ans += nums[0] * nums[1]

    return ans


print(part1(EXAMPLE1))
with open('../input/day03.txt') as f:
    print(part1(f.read()))

print(part2(EXAMPLE1))
with open('../input/day03.txt') as f:
    print(part2(f.read()))