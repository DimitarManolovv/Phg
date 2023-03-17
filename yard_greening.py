kvadratni_metri=float(input())
cena_za_kvadrat=kvadratni_metri*7.61
discount=cena_za_kvadrat*0.18
finalna_cena=cena_za_kvadrat-discount
print(f"The final price is:{finalna_cena} lv.")
print(f"The discount is:{discount} lv.")