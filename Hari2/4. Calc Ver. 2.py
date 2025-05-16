def input_angka(angka1, angka2, batas):
    try:
        angka1 = int(input('masukkan angka pertama:'))
        angka2 = int(input('masukkan angka kedua:'))
        if len(str(angka1)) > batas or len(str(angka2)) > batas:
            print("Hanya boleh 2 angka saja!")
        return angka1, angka2
    except ValueError:
        print("Invalid Input, harap masukkan angka")
        return input_angka(angka1, angka2, batas)

def calc():
    angka1, angka2 = input_angka("masukkan angka pertama: ", "Masukkan Angka Kedua: ", 2)
    operasi = input("Pilih Operasi Bilangan: ")
    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        hasil = angka1 / angka2
    else:
        print("Operasi tidak valid")
        return
    print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")

calc()