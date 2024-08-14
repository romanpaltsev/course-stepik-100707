import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

i = 0
lst_out = []

while len(lst_in) > i:
    if not (len(lst_in[i].split())) > 1:
        lst_out.append(lst_in[i])
    i += 1
    
print(*lst_out)