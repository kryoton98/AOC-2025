with open(r"C:\Code Forces\AOC\AOC 2025\day7input.txt") as f:
    grid = [line.rstrip('\n') for line in f if line.rstrip('\n')]

height = len(grid)
width = len(grid[0])

for r, row in enumerate(grid):
    c = row.find('S')
    if c != -1:
        start_row, start_col = r, c
        break

timelines = [[0] * width for _ in range(height)]
timelines[start_row][start_col] = 1

for r in range(start_row + 1, height):
    for c in range(width):
        if timelines[r-1][c] == 0:
            continue
        if grid[r][c] == '^':
            if c - 1 >= 0:
                timelines[r][c-1] += timelines[r-1][c]
            if c + 1 < width:
                timelines[r][c+1] += timelines[r-1][c]
        else:
            timelines[r][c] += timelines[r-1][c]

print(sum(timelines[-1]))
