lst = list(map(int, input().split()))
end = lst[-1] % 2 != 0
lst.pop()
print(*lst, end)