cena_ekskurziq = float(input())
broi_puzeli = int(input())
broi_govoreshti_kukli = int(input())
broi_plusheni_mecheta = int(input())
broi_minioni = int(input())
broi_kamioncheta = int(input())

obshta_cena = (broi_puzeli * 2.60) + (broi_govoreshti_kukli * 3) + (broi_plusheni_mecheta * 4.10) + (
            broi_minioni * 8.20) + (broi_kamioncheta * 2)
obsht_broi_igrachki = broi_puzeli + broi_govoreshti_kukli + broi_plusheni_mecheta + broi_minioni + broi_kamioncheta

if obsht_broi_igrachki >= 50:
    obshta_cena = obshta_cena - (obshta_cena * 0.25)

obshta_cena = obshta_cena - (obshta_cena * 0.10)

if cena_ekskurziq <= obshta_cena:
    ostavashti_pari = obshta_cena - cena_ekskurziq
    print(f'Yes! {ostavashti_pari:.2f} lv left.')
else:
    nedostigashti_pari = cena_ekskurziq - obshta_cena
    print(f'Not enough money! {nedostigashti_pari:.2f} lv needed.')
