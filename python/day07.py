import collections
import dataclasses


EXAMPLE = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


CARD_CHARS = 'AKQJT98765432'
CARD_STRENGTH =  {
    c: i for i, c in enumerate(reversed(CARD_CHARS))
}


def hand_to_int(hand: str) -> int:
    base = len(CARD_CHARS)
    n = 0
    for c in hand:
        n *= base
        n += CARD_STRENGTH[c]
    return n

def hand_to_type(hand: str) -> int:
    count = tuple(sorted(collections.Counter(hand).values()))
    return {
        (5,): 7,  # Five of a kind
        (1, 4): 6,  # Four of a kind
        (2, 3): 5,  # Full house
        (1, 1, 3): 4,  # Three of a kind
        (1, 2, 2): 3,  # Two pair
        (1, 1, 1, 2): 2,  # One pair
        (1, 1, 1, 1, 1): 1,  # High card
    }[count]


def hand_to_strengh(hand: str) -> tuple[int, int]:
    return (hand_to_type(hand), hand_to_int(hand))


@dataclasses.dataclass
class Hand:
    hand: str
    bid: int

    @property
    def strength(self):
        return hand_to_strengh(self.hand)

    def __lt__(self, other: 'Hand') -> bool:
        return self.strength < other.strength

def part1(s: str) -> int:
    ans = 0

    hands: list[Hand] = []
    for line in s.strip().split('\n'):
        hand, bid = line.split(' ')
        hands.append(Hand(hand, int(bid)))
    hands.sort()

    for i, hand in enumerate(hands, start=1):
        ans += i * hand.bid
    return ans


CARD_CHARS2 = 'AKQT98765432J'
CARD_STRENGTH2 =  {
    c: i for i, c in enumerate(reversed(CARD_CHARS2))
}


def hand_to_int2(hand: str) -> int:
    base = len(CARD_CHARS2)
    n = 0
    for c in hand:
        n *= base
        n += CARD_STRENGTH2[c]
    return n

def hand_to_type2(hand: str) -> int:
    jcount = sum(c == 'J' for c in hand)
    t = hand_to_type(hand)

    if jcount == 0:
        return t

    return {
        # j=1
        (1, 1): 2,
        (1, 2): 4,
        (1, 3): 5,
        (1, 4): 6,
        (1, 6): 7,
        # j=2
        (2, 5): 7,
        (2, 3): 6,
        (2, 2): 4,
        # j=3
        (3, 5): 7,
        (3, 4): 6,
        # j=4
        (4, 6): 7,
        # j=5
        (5, 7): 7,
    }[(jcount, t)]

def hand_to_strengh2(hand: str) -> tuple[int, int]:
    return (hand_to_type2(hand), hand_to_int2(hand))


@dataclasses.dataclass
class Hand2:
    hand: str
    bid: int

    @property
    def strength(self):
        return hand_to_strengh2(self.hand)

    def __lt__(self, other: 'Hand') -> bool:
        return self.strength < other.strength

def part2(s: str) -> int:
    ans = 0

    hands: list[Hand] = []
    for line in s.strip().split('\n'):
        hand, bid = line.split(' ')
        hands.append(Hand2(hand, int(bid)))
    hands.sort()

    for i, hand in enumerate(hands, start=1):
        ans += i * hand.bid
    return ans



print(part1(EXAMPLE))
with open('../input/day07.txt') as f:
    print(part1(f.read()))

print(part2(EXAMPLE))
with open('../input/day07.txt') as f:
    print(part2(f.read()))