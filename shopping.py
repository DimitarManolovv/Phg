budget = float(input())
broi_videokarti = int(input())
broi_procesori = int(input())
broi_ram = int(input())

obshta_cena_videokarta = 250 * broi_videokarti
cena_procesor = obshta_cena_videokarta * 0.35
obshta_cena_procesori = broi_procesori * cena_procesor
cena_ram = obshta_cena_videokarta * 0.10
obshta_cena_ram = broi_ram * cena_ram

obshta_suma = obshta_cena_videokarta + obshta_cena_procesori + obshta_cena_ram

if broi_videokarti > broi_procesori:
    obshta_suma = obshta_suma - (obshta_suma * 0.15)

if budget >= obshta_suma:
    ostatuchen_budget = budget - obshta_suma
    print(f'You have {ostatuchen_budget:.2f} leva left!')
elif budget < obshta_suma:
    nujna_suma = obshta_suma - budget
    print(f'Not enough money! You need {nujna_suma:.2f} leva more!')