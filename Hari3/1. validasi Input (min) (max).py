def input_angka(min, max):
    while True:
        try:
            angka = int(input("Masukkan Angka:  ({min}-{max}): "))
            if min <= angka <= max:
             return angka
            print(f"Harap masukkan angka yang valid antara {min} dan {max}!")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

angka_user = input_angka(1, 100)
print(f"Angka yang Anda masukkan adalah: {angka_user}")