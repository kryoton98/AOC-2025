from bisect import bisect_right

with open(r"C:\Code Forces\AOC\AOC 2025\day5input.txt") as f:
    ranges, ids = f.read().strip().split("\n\n")

pairs = []
for line in ranges.splitlines():
    start, end = map(int, line.split("-"))
    pairs.append((start, end))

pairs.sort()
merged = []
for start, end in pairs:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

starts = [s for s, _ in merged]
ends = [e for _, e in merged]

fresh = 0
for line in ids.splitlines():
    val = int(line)
    idx = bisect_right(starts, val) - 1
    if idx >= 0 and starts[idx] <= val <= ends[idx]:
        fresh += 1

print(fresh)
