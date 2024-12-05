# opened day 05 problem at about 7:30 but knew would not have much time to work on this
# because of household logistics
# p1 submitted 8:24 but had to go for my Thursday morning run - p2 sorting solution came up during run
# 10:30 at work after first meeting could start implementing p2, submitted at 10:40

# %%

from functools import cmp_to_key
from pathlib import Path
from collections import defaultdict

fn = Path(__file__).parent / "input.txt"
b1, b2 = fn.read_text().strip().split("\n\n")

# for each line, record that prev must be before next, but also that next must be after prev as we want to be able to
# look up the relationship from any side
after_me = defaultdict(list)
before_me = defaultdict(list)
for l in b1.split("\n"):
    p, n = l.split("|")
    after_me[p].append(n)
    before_me[n].append(p)


# For part 2, we will simply use built-in sort using the prev/next relationships
# cmp function must return - for less than, + for greater than, 0 for equal
def cmp(a, b):
    if a in after_me and b in after_me[a]:
        return -1
    if a in before_me and b in before_me[a]:
        return 1
    if b in after_me and a in after_me[b]:
        return 1
    if b in before_me and a in before_me[b]:
        return -1

    # lazy, so taking this chance (laziness was right)
    raise RuntimeError


# for each sequence, stick val:idx in a dict
# for each val, check that all after_me values have greater indices and that all before_me indices have smaller values
valid_sum = 0
repaired_sum = 0
for update in b2.split("\n"):
    # for each update, we create dict from page number to position in list
    update_dict = {}
    update_list = update.split(",")
    for i, p in enumerate(update_list):
        update_dict[p] = i

    # go through update dict, check for each number that it satisfies all before_me and after_me constraints
    # numbers are in dict, constraints are also in dicts, so should be fast
    valid = True
    for p in update_dict:
        if p in after_me:  # constraint exists
            for ap in after_me[p]:  # ap = after page
                if ap in update_dict and update_dict[ap] <= update_dict[p]:
                    valid = False

        if valid and p in before_me:
            for bp in before_me[p]:
                if bp in update_dict and update_dict[bp] >= update_dict[p]:
                    valid = False

    if valid:
        valid_sum += int(update_list[len(update_list) // 2])

    else:
        sorted_update_list = sorted(update_list, key=cmp_to_key(cmp))
        repaired_sum += int(sorted_update_list[len(sorted_update_list) // 2])

# part1: 5964
print(valid_sum)

# part 2: 4719
print(repaired_sum)
