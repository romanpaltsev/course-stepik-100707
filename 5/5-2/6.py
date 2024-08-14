n = int(input())

lst = []
i = 1

while n >= i:
    if i % 3 == 0 and i % 5 == 0:
        lst.append(i)
    i += 1
else:
    if n >= 100:
        print("слишком большое значение n")
    else:
        print(*lst)