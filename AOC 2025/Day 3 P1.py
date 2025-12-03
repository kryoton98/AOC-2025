import sys

total = 0

for line in sys.stdin:
    n = line.strip()
    if not n:
        continue
        
    maxx = -1
    
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            curr = 10*int(n[i]) + int(n[j])
            if curr > maxx:
                maxx = curr
                
    total += maxx

print(total)