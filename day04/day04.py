# opened problem at 7:34 -- thought yes / no?
# submitted part 1 at 7:57
# 8:00 to 8:10 fetched someone with car, brain was working on part 2
# submitted part 2 at 8:16 -- sample_word() was ready for this!

# %%

from pathlib import Path
import re

fn = Path(__file__).parent / "input.txt"
lines = fn.read_text().strip().split("\n")

# %% part 1

# right, left, up, down, down-right, up-left, up-right, down-left
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def sample_word(r, c, dir: tuple[int, int], length=4):
    chars = []
    for _ in range(length):
        if r < 0 or c < 0 or r >= len(lines) or c >= len(lines[0]):
            # we needed one more char, but were out of bounds, so no word
            return None

        chars.append(lines[r][c])
        r += dir[0]
        c += dir[1]

    return "".join(chars)


num = 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "X":
            for dir in dirs:
                word = sample_word(r, c, dir)
                if word == "XMAS":
                    num += 1

print(num)

# %% part 2
from collections import Counter

xm_dirs = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

centre_count = Counter()
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "M":
            for dir in xm_dirs:
                word = sample_word(r, c, dir, length=3)
                if word == "MAS":
                    # add this to the total MAS intersecting this A position
                    centre_count[(r + dir[0], c + dir[1])] += 1

# how many A positions have 2 occurrences
print(sum([1 for v in centre_count.values() if v == 2]))
