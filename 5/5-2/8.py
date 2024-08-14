x = int(input())

i = 1
n = 10

while True:
    if n > x:
        print(i)
        break
    n = n * 1.1
    i += 1 