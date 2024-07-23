a, b, c = map(int, input().split())

print(a + b > c and a < b + c and a + c > b)