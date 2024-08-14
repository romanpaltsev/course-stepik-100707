p = [0] * 10
i = 0

while i < 7:
    i += 1
    n = int(input())
    if p[n] == 1:
        continue
    else:
        p[n] = 1
    

print(*p)