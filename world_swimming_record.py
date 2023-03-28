from math import floor
rekord_sekundi=float(input())
razstoqnie_metri=float(input())
vreme_za_metar=float(input())

zabavqne=floor((razstoqnie_metri/15))*12.5
obshto_vreme=(razstoqnie_metri*vreme_za_metar)+zabavqne

if obshto_vreme<rekord_sekundi:
    print(f'Yes, he succeeded! The new world record is {obshto_vreme:.2f} seconds.')
elif obshto_vreme>= rekord_sekundi:
    nedostigashto_vreme=obshto_vreme-rekord_sekundi
    print(f'No, he failed! He was {nedostigashto_vreme:.2f} seconds slower.')