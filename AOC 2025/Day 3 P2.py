import sys

total = 0

for line in sys.stdin:
    n = line.strip()
    if not n:
        continue

    stack = []
    remove = len(n) - 12
    
    for digit in n:
        while remove > 0 and len(stack) != 0 and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)
        

    result = "".join(stack[:12])
    
    total += int(result)

print(total)