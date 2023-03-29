from math import ceil
ime_serial=str(input())
epizod_length=int(input())
pochivka_length=int(input())

vreme_za_obqd=pochivka_length*0.125
vreme_za_otdih=pochivka_length*0.25
ostanalo_vreme=pochivka_length-vreme_za_obqd-vreme_za_otdih

if ostanalo_vreme >= epizod_length:
    ostanalo_vreme_serial=ceil(ostanalo_vreme-epizod_length)
    print(f'You have enough time to watch {ime_serial} and left with {ostanalo_vreme_serial} minutes free time.')
elif ostanalo_vreme< epizod_length:
    nujno_vreme=ceil(epizod_length-ostanalo_vreme)
    print(f"You don't have enough time to watch {ime_serial}, you need {nujno_vreme} more minutes.")