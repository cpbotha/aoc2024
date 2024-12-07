# started at about 8:20
# p1 submitted 8:50
# p2 submitted 8:56

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


def concat(l, r):
    return int(str(l) + str(r))


# p1 thoughts: minor extra effort to support additional operators
# p2 thoughts: he he he -- just going to add this concat operator to the end
OPS = [operator.add, operator.mul, concat]


# p1 thoughts: might want to parallelize this for p2
def check_eqn(tvo):
    test_val, operands = tvo
    # loop through all of the permutations of add, sum, ...
    for ops in product(OPS, repeat=len(operands) - 1):
        ans = operands[0]
        for i, op in enumerate(ops):
            ans = op(ans, operands[i + 1])

        if ans == test_val:
            # there might be more solutions, but for part 1 we early-out
            return True

    return False


valid_eqns = [tvo for tvo in eqns if check_eqn(tvo)]
p1sum = sum([tvo[0] for tvo in valid_eqns])
# p1: 5837374519342
# p2: 492383931650959 in 8.5 secs
print(p1sum)
# %%
