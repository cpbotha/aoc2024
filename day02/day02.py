# start reading at 7:46. p1 8:05, p2 8:16
# each line is a report, consisting of levels
# report is safe when both:
# 1.levels are all increasing or all decreasing
# 2.two adjacent levels differ by at least 1 and at most 3

# %% parse the input
from pathlib import Path
from time import perf_counter_ns
import numpy as np

fn = Path(__file__).parent / "input.txt"

# thanks python
reports = [np.array([int(e) for e in line.split()]) for line in fn.read_text().strip().split("\n")]

# %% part 1


def is_safe(r):
    # these are the intervals between levels
    deltas = (r - np.roll(r, 1))[1:]
    if (np.all(deltas > 0) or np.all(deltas < 0)) and np.all(np.abs(deltas) <= 3) and np.all(np.abs(deltas) >= 1):
        return True

    return False


# 421
safes = [is_safe(r) for r in reports]
print(np.sum(safes))

# %% part 2


sum = 0
for r in reports:
    if is_safe(r):
        sum += 1

    else:
        # report is unsafe, apply dampener:
        # bruteforce but early-exit removing a level and trying again
        for i in range(len(r)):
            if is_safe(np.delete(r, i)):
                sum += 1
                break

# 476
print(sum)
