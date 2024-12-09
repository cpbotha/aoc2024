# blocks: file-len - space-len - file-len - space-len
# file-blocks are numbered 0 .. N

# %%
from collections import defaultdict
from pathlib import Path
from itertools import product

# there are duplicate test values in the full input
fn = Path(__file__).parent / "input.txt"
line = fn.read_text().strip()

# the whole map is 95307 long
sum([int(e) for e in line])

map = []
for bi, b in enumerate(line):
    if bi % 2 == 0:
        block_id = bi // 2
        map.extend([int(block_id) for _ in range(int(b))])
    else:
        map.extend([-1 for _ in range(int(b))])

# keep track of this to reduce searching
first_space = map.index(-1)


def find_last_block_idx(start_pos):
    # iterate in reverse from start_pos, find first positive integer
    for i in range(len(map) - 1, -1, -1):
        if map[i] != -1:
            return i

    return 99999999999999


def find_next_space(start_pos):
    for i in range(start_pos, len(map)):
        if map[i] == -1:
            return i

    return 99999999999999


last_block = find_last_block_idx(len(map) - 1)

# %% part 1 takes > 10 seconds with python 3.13, < 2s with pypy
while first_space < last_block:
    map[first_space] = map[last_block]
    map[last_block] = -1
    first_space = find_next_space(first_space)
    last_block = find_last_block_idx(last_block)

checksum = 0
for i in range(first_space):
    checksum += i * map[i]

print(checksum)

# %% part 2
