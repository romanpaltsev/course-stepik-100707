s = 1

while True:
    n = int(input())
    if n < 0:
        continue
    if n == 0:
        break
    s = s * n
    
print(s)