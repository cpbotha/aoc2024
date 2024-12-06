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
            gpos_orig = gpos
            o[gpos] = "X"

rmax = ri
cmax = ci

# guard is looking up
gvec = [-1, 0]
gvec_orig = gvec.copy()
o_orig = o.copy()

dirs = {}


def step(gpos, gvec, o, dirs):
    # guard wants to go here
    cand_pos = (gpos[0] + gvec[0], gpos[1] + gvec[1])
    if cand_pos[0] < 0 or cand_pos[0] > rmax or cand_pos[1] < 0 or cand_pos[1] > cmax:
        # guard has exited the area, success!
        return 1, gpos, gvec

    if o.get(cand_pos) in ("#", "O"):
        # guard has hit an obstacle, turn right
        gvec = [gvec[1], -1 * gvec[0]]
        return 0, gpos, gvec

    gpos = cand_pos
    if dirs.get(gpos) == gvec:
        return -1, gpos, gvec

    o[gpos] = "X"
    dirs[gpos] = gvec
    return 0, gpos, gvec


ret = 0
while ret == 0:
    ret, gpos, gvec = step(gpos, gvec, o, dirs)


c = Counter(o.values())
# 4939
print(c["X"])

# %% part 2

# we can only insert obstacle on guard's known route (4000ish checks)
# for each of these candidate obstacles, we have to detect loops

num_loops = 0
for pos in o:
    if o[pos] == "X":
        check_o = o_orig.copy()
        # install obstacle
        check_o[pos] = "O"
        # reset guard
        gpos = gpos_orig
        gvec = gvec_orig.copy()

        # check if we get -1
        ret = 0
        dirs = {}
        while ret == 0:
            ret, gpos, gvec = step(gpos, gvec, check_o, dirs)

        if ret == -1:
            num_loops += 1

print(num_loops)
