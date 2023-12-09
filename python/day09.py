EXAMPLE="""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def diff(a: list[int]) -> list[int]:
    b = [0] * (len(a)-1)
    for i in range(len(a)-1):
        b[i] = a[i+1] - a[i]
    return b


def extrapolate(a: list[int]) -> int:
    stack = [a[-1]]
    while True:
        a = diff(a)
        if all(x == 0 for x in a):
            break
        stack.append(a[-1])
    x = 0
    while stack:
        x = x + stack.pop()
    return x


def part1(s: str) -> int:
    ans = 0
    for line in s.strip().split('\n'):
        a = list(map(int, line.split()))
        ans += extrapolate(a)
    return ans


def extrapolate_backward(a: list[int]) -> int:
    stack = [a[0]]
    while True:
        a = diff(a)
        if all(x == 0 for x in a):
            break
        stack.append(a[0])
    x = 0
    while stack:
        x = stack.pop() - x
    return x


def part2(s: str) -> int:
    ans = 0
    for line in s.strip().split('\n'):
        a = list(map(int, line.split()))
        ans += extrapolate_backward(a)
    return ans

print(part1(EXAMPLE))
with open('../input/day09.txt') as f:
    print(part1(f.read()))

print(extrapolate_backward([10,13,16,21,30,45]))
with open('../input/day09.txt') as f:
    print(part2(f.read()))