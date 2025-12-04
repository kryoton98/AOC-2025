import sys

grid = [line.strip() for line in sys.stdin if line.strip()]


rows = len(grid)
cols = len(grid[0])

count = 0

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            rolls = 0
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        rolls += 1
            
            if rolls < 4:
                count += 1

print(count)
