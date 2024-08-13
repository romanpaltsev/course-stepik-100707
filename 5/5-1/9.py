n = int(input())

s = 1
i = 3

while i < n:
    s *= 2
    n -= i
    
print(s)