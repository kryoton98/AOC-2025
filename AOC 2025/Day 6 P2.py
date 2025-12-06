from functools import reduce
filename = r"C:\Code Forces\AOC\AOC 2025\day6input.txt"

with open(filename, 'r', encoding='utf-8') as f:
    raw_lines = [line.rstrip('\n') for line in f]

width = max(len(s) for s in raw_lines)
rows = [s.ljust(width) for s in raw_lines]

R = len(rows) 
columns = list(map(list, zip(*rows)))  

problems = []
current = []

for col in columns:
    if all(c.isspace() for c in col):
        if current:
            problems.append(current)
            current = []
    else:
        current.append(col)

if current:
    problems.append(current)

def parse_problem(cols):
    R = len(cols[0])
    digit_rows = range(0, R - 1) 
    op_row = R - 1

    ops = set()
    for col in cols:
        c = col[op_row]
        if c in "+*":
            ops.add(c)

    op = ops.pop()

    numbers = []
    for col in reversed(cols):
        digits = ''.join(
            ch for i, ch in enumerate(col)
            if i in digit_rows and ch.isdigit()
        )
        if digits:
            numbers.append(int(digits))

    return op, numbers

grand_total = 0

for block in problems:
    op, nums = parse_problem(block)
    if op == '+':
        result = sum(nums)
    elif op == '*':
        result = reduce(lambda x, y: x * y, nums)

    grand_total += result

print(grand_total)
