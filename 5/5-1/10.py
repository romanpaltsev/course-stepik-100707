n = int(input())

i = 0
s = 1000

while i < n:
    s *= 1.05
    n -= 1
    
print(round(s, 2))