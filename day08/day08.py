# 50x50 grid in full data

# many other summer activities going on this Sunday, so am time-slicing this

# part 1: initially wanted to solve the quadratic equations, but then saw antinodes are always OUTSIDE the pair, so can
# keep it simpler: find the antinode by adding the dist between the pair to each of the sides, check that

# part 2: haha! just a bit of time between run and having to leave for family lunch. Got the right answer at about 11:32
# when we had to leave! HURRAH

# %%
from collections import defaultdict
from pathlib import Path
from itertools import product

# there are duplicate test values in the full input
fn = Path(__file__).parent / "input.txt"
lines = fn.read_text().strip().split("\n")

freq_lut = defaultdict(list)
for ri, line in enumerate(lines):
    for ci, freq in enumerate(line):
        if freq != ".":
            freq_lut[freq].append((ri, ci))

# p1 thoughts: not required for p1, but I'm going to map from antinode pos to all freqs causing it
antinodes = defaultdict(list)
for freq, coords in freq_lut.items():
    # for every pair of coordinates
    for coord_pair in product(coords, coords):
        if coord_pair[0] == coord_pair[1]:
            continue

        # calculate the row,col delta
        dr = coord_pair[1][0] - coord_pair[0][0]
        dc = coord_pair[1][1] - coord_pair[0][1]
        # add to the second
        an1 = (coord_pair[1][0] + dr, coord_pair[1][1] + dc)
        # subtract from the first
        an0 = (coord_pair[0][0] - dr, coord_pair[0][1] - dc)
        # check if valid!
        if an1[0] >= 0 and an1[0] < len(lines) and an1[1] >= 0 and an1[1] < len(lines[0]):
            antinodes[an1].append(freq)
        if an0[0] >= 0 and an0[0] < len(lines) and an0[1] >= 0 and an0[1] < len(lines[0]):
            antinodes[an0].append(freq)

# 278
print(f"part 1: {len(antinodes.keys())}")

# %% part 2

# I did not want to try bresenham, I wanted to do more manually


def march(start, m, delta_c, antinodes2):
    antinodes2.add(start)
    dc = delta_c
    while True:
        r = start[0] + m * dc  # float
        # check if we are still inside!
        c = start[1] + dc  # int
        if r < 0 or r >= len(lines) or c < 0 or c >= len(lines[0]):
            break
        # check if r close to an integer
        if abs(r - int(r)) < 1e-6:
            antinodes2.add((int(r), c))

        dc += delta_c


antinodes2 = set()
for freq, coords in freq_lut.items():
    # for every pair of coordinates
    for coord_pair in product(coords, coords):
        if coord_pair[0] == coord_pair[1]:
            continue

        # calculate the row,col delta
        dr = coord_pair[1][0] - coord_pair[0][0]
        dc = coord_pair[1][1] - coord_pair[0][1]

        # gradient
        m = dr / dc

        # march "up" along gradient
        march(coord_pair[0], m, 1, antinodes2)
        # march "down"
        march(coord_pair[0], m, -1, antinodes2)

# 1067
print(f"part 2: {len(antinodes2)}")
