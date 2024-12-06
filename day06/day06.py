# part 1: 7:25 - 8:05
# part 2: EEEEKE

# %%

from collections import Counter
from pathlib import Path

fn = Path(__file__).parent / "input.txt"

lines = fn.read_text().strip().split("\n")

# obstacles
o = {}
for ri, r in enumerate(lines):
    for ci, c in enumerate(r):
        if c == "#":
            o[(ri, ci)] = "#"
        elif c == "^":
            gpos = (ri, ci)
            o[gpos] = "X"

rmax = ri
cmax = ci

# guard is looking up
gvec = [-1, 0]


def step():
    global gpos, gvec
    # guar wants to go here
    cand_pos = (gpos[0] + gvec[0], gpos[1] + gvec[1])
    if cand_pos[0] < 0 or cand_pos[0] > rmax or cand_pos[1] < 0 or cand_pos[1] > cmax:
        # guard has exited the area, success!
        return True

    if o.get(cand_pos) == "#":
        # guard has hit an obstacle, turn right
        gvec = [gvec[1], -1 * gvec[0]]
        return False

    gpos = cand_pos
    o[gpos] = "X"
    return False


while not step():
    print(gpos)
    pass


c = Counter(o.values())
# 4939
print(c["X"])
