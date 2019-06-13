import collections

# Score categories
# Change the values as you see fit
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: x.count(1)
TWOS = lambda x: x.count(2)*2
THREES = lambda x: x.count(3)*3
FOURS = lambda x: x.count(4)*4
FIVES = lambda x: x.count(5)*5
SIXES = lambda x: x.count(6)*6
FULL_HOUSE = lambda x: sum(x) if sorted(collections.Counter(x).values())==[2,3] else 0
FOUR_OF_A_KIND = lambda x: sum(y*4 for y in set(x) if x.count(y)>3)
LITTLE_STRAIGHT = lambda x: 30 if len(set(x))==5 and not 6 in set(x) else 0
BIG_STRAIGHT = lambda x: 30 if len(set(x)) ==5 and not 1 in set(x) else 0
CHOICE = sum


def score(dice, category):
    return category(dice)
