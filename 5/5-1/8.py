n = int(input())

n1, n2 = 1, 1

lst = [n1, n2]

while len(lst) < n:
    n1, n2 = n2, n1 + n2
    lst.append(n2)
    
print(*lst)