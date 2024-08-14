names_students = list(map(str.lower, input().split()))

i = 0

while len(names_students) > i:
    if names_students[i][0] == names_students[i][-1]:
        print("ДА")
        break
    
    i += 1
else:
    print("НЕТ")