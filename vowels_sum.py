words = input()

a = 0
o = 0
u = 0
e = 0
i = 0

for letters in words:
    if letters == "a":
        a = a +1
    elif letters == "o":
        o = o +1
    elif letters == "u":
        u = u + 1
    elif letters == "e":
        e = e +1
    elif letters == "i":
        i = i +1

result = (a * 1) + (e * 2) + (i * 3) + (o * 4) + (u * 5)
print(result)