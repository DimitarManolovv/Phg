nachalno_chislo = int(input())
bonus = 0

if nachalno_chislo <= 100:
    bonus = 5
elif nachalno_chislo > 1000:
    bonus = 0.1 * nachalno_chislo
else:
    bonus = 0.2 * nachalno_chislo
if nachalno_chislo % 2 == 0:
    bonus = bonus + 1
elif nachalno_chislo % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + nachalno_chislo)