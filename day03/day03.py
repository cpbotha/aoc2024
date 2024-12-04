# started at 9:13, submitted p1 at 9:19 during meeting (sorry), p2 at 9:34

# %% parse the input
from pathlib import Path
import re

fn = Path(__file__).parent / "input.txt"
code = fn.read_text().strip()

# %% part 1
sum = 0
for m in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", code):
    sum += int(m[0]) * int(m[1])

print(sum)

# %% part 2
sum = 0
mul_dict = {}
for mo in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", code):
    # map start position to the mul operands
    mul_dict[mo.span()[0]] = (mo.group(1), mo.group(2))

# find "do()" OR "don't()"
dodo_dict = {}
for mo in re.finditer(r"(do\(\)|don't\(\))", code):
    dodo_dict[mo.span()[0]] = True if mo.group(1) == "do()" else False

on = True
for i in range(len(code)):
    if i in dodo_dict:
        on = dodo_dict[i]
    elif i in mul_dict and on:
        sum += int(mul_dict[i][0]) * int(mul_dict[i][1])

print(sum)
