# blocks: file-len - space-len - file-len - space-len
# file-blocks are numbered 0 .. N

# thanks pypy!
# uv run python day09.py  0.60s user 0.03s system 99% cpu 0.629 total
# with python 3.13
# uv run --python 3.13 python day09.py  14.03s user 0.51s system 99% cpu 14.616 total
# (of which most is part 1)

# %%
from collections import defaultdict
from pathlib import Path
from itertools import product
from operator import itemgetter

# there are duplicate test values in the full input
fn = Path(__file__).parent / "input.txt"
line = fn.read_text().strip()

# the whole map is 95307 long
sum([int(e) for e in line])

# map for part 1: list of block ids and -1 for spaces
map = []
block_spans = {}
space_spans = []
for bi, b in enumerate(line):
    if bi % 2 == 0:
        block_id = bi // 2
        block_spans[block_id] = (len(map), int(b))  # part 2: block_id -> (start, length)
        map.extend([int(block_id) for _ in range(int(b))])
    else:
        space_spans.append((len(map), int(b)))
        map.extend([-1 for _ in range(int(b))])

# highest block_id 9999
print(f"highest block_id: {max(block_spans.keys())}")

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
def part1(first_space, last_block):
    while first_space < last_block:
        map[first_space] = map[last_block]
        map[last_block] = -1
        first_space = find_next_space(first_space)
        last_block = find_last_block_idx(last_block)

    checksum = 0
    for i in range(first_space):
        checksum += i * map[i]

    return checksum


# test: 1928
# puzzle: 6331212425418
checksum = part1(first_space, last_block)
print(checksum)

# %% part 2

# for block_id, (bidx, blen) in reversed(block_spans.items()):
for block_id in range(max(block_spans.keys()), -1, -1):
    bidx, blen = block_spans[block_id]
    # find first space large enough to take this block
    for sidx, (space_idx, space_len) in enumerate(space_spans):
        # the lack of this space_idx > bidx check cost me 30 minutes
        # worked fine on test data, too high on puzzle data <--- AoC worst nightmare
        # wasted time debugging (which did result in much faster code), until I went back to the problem and read:
        # "If there is no span of free space ***to the left of a file*** that is large enough to fit the file". DOH!
        # LESSON: read the question again
        if space_idx >= bidx:
            break
        if space_len >= blen:
            # move the block
            block_spans[block_id] = (space_idx, blen)
            # adjust / remove the space span
            del space_spans[sidx]
            if space_len > blen:
                space_spans.insert(sidx, (space_idx + blen, space_len - blen))
                # space_spans.append((space_idx + blen, space_len - blen))
                # space_spans.sort(key=itemgetter(0))

            # print(f"moved block {block_id} to {space_idx}")
            # print(sorted(space_spans.items()))

            # break out of the space_spans search, start with next block_span
            break


checksum2 = 0
for block_id, (bidx, blen) in block_spans.items():
    for i in range(bidx, bidx + blen):
        checksum2 += i * block_id

# ARGH! test should be 2858, but I'm getting: 2854, 2874, .... 2858
# ok now test input correct, but puzzle: 8592266602739 is too high
# part 2: 6363268339304
print(checksum2)
