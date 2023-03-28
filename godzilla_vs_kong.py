budjet_za_filma = float(input())
broi_statisti = int(input())
cena_obkleklo_1_statist = float(input())

dekor_za_filma = budjet_za_filma * 0.10

if broi_statisti > 150:
    cena_obkleklo_1_statist = cena_obkleklo_1_statist - (cena_obkleklo_1_statist * 0.10)

obshto_pari = (broi_statisti * cena_obkleklo_1_statist) + dekor_za_filma

if obshto_pari > budjet_za_filma:
    print("Not enough money!")
    nedostigashti_pari = obshto_pari - budjet_za_filma
    print(f'Wingard needs {nedostigashti_pari:.2f} leva more.')
else:
    print("Action!")
    ostanali_pari = budjet_za_filma - obshto_pari
    print(f'Wingard starts filming with {ostanali_pari:.2f} leva left.')