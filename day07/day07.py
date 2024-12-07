# started at about 8:20
# p1 submitted 8:50

# %%

from pathlib import Path
from joblib import Parallel, delayed
from itertools import product
import operator

# there are duplicate test values in the full input
fn = Path(__file__).parent / "input.txt"

lines = fn.read_text().strip().split("\n")

eqns = []
for line in lines:
    l, r = line.split(":")
    test_val = int(l)
    operands = [int(e) for e in r.strip().split(" ")]
    eqns.append((test_val, operands))


# p1 thoughts: minor extra effort to support additional operators
OPS = [operator.add, operator.mul]


# p1 thoughts: might want to parallelize this for p2
def check_eqn(tvo):
    test_val, operands = tvo
    # loop through all of the permutations of add, sum
    for ops in product([0, 1], repeat=len(operands) - 1):
        ans = operands[0]
        for i, op in enumerate(ops):
            ans = OPS[op](ans, operands[i + 1])

        if ans == test_val:
            # there might be more solutions, but for part 1 we early-out
            return True

    return False


valid_eqns = [tvo for tvo in eqns if check_eqn(tvo)]
p1sum = sum([tvo[0] for tvo in valid_eqns])
# 5837374519342
print(p1sum)
# %%
