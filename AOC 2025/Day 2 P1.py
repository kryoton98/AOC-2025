import re

a = []
for i in range(1, 10**5):
    s = str(i) + str(i)
    a.append(int(s))

a.sort()

x = list(map(str, input().split(',')))
sum = 0

for i in x:
    parts = re.split('-', i)
    l, r = map(int, parts)

    #binary search to find the range in a
    # Find the first index where a[index] >= l
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= l:
            l_index = mid
            right = mid - 1
        else:
            left = mid + 1

    # Find the last index where a[index] <= r
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] <= r:
            r_index = mid
            left = mid + 1
        else:
            right = mid - 1

    for j in range(l_index, r_index + 1):
        sum += a[j]

print(sum)