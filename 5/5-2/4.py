cities = input().split()

i = 0

while len(cities) > i:
    if len(cities[i]) > 5:
        s = "ДА"
    else:
        s = "НЕТ"

    i += 1
    
print(s)