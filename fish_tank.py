duljina_cm=int(input())
shirochina_cm=int(input())
visochina_cm=int(input())
procent=float(input())/100
obem=duljina_cm*shirochina_cm*visochina_cm
obem_litri=obem/1000
nujni_litri=obem_litri*(1-procent)
print(nujni_litri)