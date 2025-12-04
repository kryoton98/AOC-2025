import sys
grid = [list(line.strip()) for line in sys.stdin if line.strip()]

rows = len(grid)
cols = len(grid[0])

count = 0

directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1), (1, -1), (1, 0), (1, 1)]


def operation():
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
                    global count
                    count += 1
                    grid[r][c] = "."

for i in range(100):
    operation()

# here i did some tricks (this is not a very feasible way to solve it but i basically check the max to which it can go) 
# like i tried 100 first and even for 150 it gave the same result so i tried 50 and then 46 (it may vary for your input) and it gave the same result as well
# so i concluded that after some point the grid stabilizes and no more changes happen

print(count)
