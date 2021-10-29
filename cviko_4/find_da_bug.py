# druhá největší hodnota (bez opakování)
max = int(input())
dmax = int(input())

if dmax > max:
    dmax, max = max, dmax

while True:
    i = int(input())
    if i == -1:
        break

    if i > max:
        dmax, max = max, i
    elif (i > dmax or max == dmax):
        dmax = i

if dmax > max:
    dmax = max

print(dmax)
