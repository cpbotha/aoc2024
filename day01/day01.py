# %%
from pathlib import Path
from time import perf_counter_ns

fn = Path(__file__).parent / "input.txt"

lines = fn.read_text().strip().split("\n")

lists = [[], []]
for line in lines:
    elems = [int(e) for e in line.split()]
    for i in range(2):
        lists[i].append(elems[i])

# %% part 1


s1 = perf_counter_ns()

lists[0].sort()
lists[1].sort()

# element by element subtraction between two lists
dists = [abs(es[1] - es[0]) for es in zip(lists[1], lists[0])]

# 2756096
p1 = sum(dists)
e1 = perf_counter_ns()
print(f"Part 1: {p1} in {(e1 - s1)/1000} µs")

# %% part 2 - damnit Python...

from collections import Counter


s2 = perf_counter_ns()
c = Counter(lists[1])
# 23117829
p2 = sum([e * c[e] for e in lists[0]])
e2 = perf_counter_ns()
print(f"Part 2: {p2} in {(e2 - s2)/1000} µs")
