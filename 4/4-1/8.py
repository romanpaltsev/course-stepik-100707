a, b, c, d = map(int, input().split())

if a - 1 > c and b - 1 > d or a - 1 > d and b - 1 > c:
  print("ДА")
else:
  print("НЕТ")