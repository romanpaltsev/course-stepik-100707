n, m = map(int, input().split())

i = 1
lst = []
lst.append(n + 1)
s = (m - n) / 2

while i < s:
    lst.append(n + 3)
    n += 2
    i += 1

print(*lst)