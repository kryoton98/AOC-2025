with open(r"C:\Code Forces\AOC\AOC 2025\day7input.txt") as f:
    grid = [line.rstrip('\n') for line in f if line.rstrip('\n')]

height = len(grid)
width = len(grid[0])

start_row = start_col = None
for r, row in enumerate(grid):
    c = row.find('S')
    if c != -1:
        start_row, start_col = r, c
        break

cols = {start_col}
count = 0

for r in range(start_row + 1, height):
    row = grid[r]
    next_cols = set()
    for c in cols:
        if not (0 <= c < width):
            continue
        if row[c] == '^':
            count += 1
            if c - 1 >= 0:
                next_cols.add(c - 1)
            if c + 1 < width:
                next_cols.add(c + 1)
        else:
            next_cols.add(c)
    cols = next_cols
    if not cols:
        break

print(count)