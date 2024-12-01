# %%
from pathlib import Path

fn = Path(__file__).parent / "input.txt"

lines = fn.read_text().strip().split("\n")

lists = [[], []]
for line in lines:
    elems = [int(e) for e in line.split()]
    for i in range(2):
        lists[i].append(elems[i])

# %% part 1

lists[0].sort()
lists[1].sort()

# element by element subtraction between two lists
dists = [abs(es[1] - es[0]) for es in zip(lists[1], lists[0])]

# 2756096
print(sum(dists))

# %% part 2 - damnit Python...

from collections import Counter

c = Counter(lists[1])
print(sum([e * c[e] for e in lists[0]]))
