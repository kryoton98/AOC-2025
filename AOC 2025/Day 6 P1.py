from functools import reduce

filename = r"C:\Code Forces\AOC\AOC 2025\day6input.txt"

with open(filename, 'r', encoding='utf-8') as f:
    raw_lines = [line.rstrip('\n') for line in f]

wid = max(len(s) for s in raw_lines)
rows = [s.ljust(wid) for s in raw_lines]

cols = list(map(list, zip(*rows)))

probs = []
cur = []

for col in cols:
    if all(c.isspace() for c in col):
        if cur:
            prob_rows = list(map(''.join, zip(*cur)))
            probs.append(prob_rows)
            cur = []
    else:
        cur.append(col)

if cur:
    prob_rows = list(map(''.join, zip(*cur)))
    probs.append(prob_rows)

grand_total = 0

for prob_lines in probs:
    lines = [line.strip() for line in prob_lines if line.strip()]
    if not lines:
        continue

    op = lines[-1]
    numbers = [int(line) for line in lines[:-1]]

    if op == '+':
        result = sum(numbers)
    else:
        result = reduce(lambda x, y: x * y, numbers)
 
    grand_total += result

print(grand_total)
