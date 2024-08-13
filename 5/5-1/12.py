start = 100
end = 999
lst = []

while start < end:
    if start % 47 == 43 and start % 3 == 0:
        lst.append(start)
        start += 47
    else:
        start += 1
    
print(*lst)