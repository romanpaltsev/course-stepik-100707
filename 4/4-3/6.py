m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

a, b, c = map(int, input().split())

a = "#" + m[a - 1] if a in [1, 4] else m[a - 1]
b = "#" + m[b - 1] if b in [1, 4] else m[b - 1]
c = "#" + m[c - 1] if c in [1, 4] else m[c - 1]

print(a, b, c)