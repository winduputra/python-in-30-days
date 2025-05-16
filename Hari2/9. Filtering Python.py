angka = [10, 33, 54, 71, 90, 101]
angka_genap = list(filter(lambda x: x % 2 == 0, angka))
angka_ganjil = list(filter(lambda x: x % 2 != 0, angka))
print("Angka genap:", angka_genap)
print("Angka ganjil:", angka_ganjil)