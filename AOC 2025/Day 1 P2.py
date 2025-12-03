n = 50
count = 0

inputs = []
with open(r'C:\Code Forces\AOC\AOC 2025\day1input.txt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        inputs.append(line)

for s in inputs:
    amount = int(s[1:])
    direction = s[0]
    
    for _ in range(amount):
        if direction == "R":
            n = (n + 1) % 100
        elif direction == "L":
            n = (n - 1) % 100
        
        if n == 0:
            count += 1

print(count)
