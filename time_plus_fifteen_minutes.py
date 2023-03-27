chas = int(input())
minuti = int(input())

minuti = minuti + 15

if minuti > 59:
    chas = chas + 1
    minuti = (minuti - 60)

if chas > 23:
    chas = 00

if minuti <= 9:
    print(f'{chas}:0{minuti}')
if minuti >= 10:
    print(f'{chas}:{minuti}')