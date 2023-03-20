godishna_taksa=int(input())
cena_kecove=godishna_taksa-(godishna_taksa*0.40)
cena_ekip=cena_kecove-(cena_kecove*0.20)
cena_topka=0.25*cena_ekip
cena_aksesoar=0.2*cena_topka
obshta_cena=godishna_taksa+cena_kecove+cena_ekip+cena_topka+cena_aksesoar
print(obshta_cena)