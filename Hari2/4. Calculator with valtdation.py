def input_angka(prompt1, prompt2, max_length):
    try:
        angka1 = int(input(prompt1))
        angka2 = int(input(prompt2))
        if len(str(angka1)) > max_length or len(str(angka2)) > max_length:
            print(f"Angka tidak boleh lebih dari {max_length} karakter.")
            return input_angka(prompt1, prompt2, max_length)
        return angka1, angka2
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return input_angka(prompt1, prompt2, max_length)

def kalkulator():
    angka1, angka2 = input_angka("Masukkan Angka Pertama (Maks. 2 Char): ", "Masukkan Angka Kedua (Maks. 2 Char)", 2)
    #angka2 = input_angka("Masukkan Angka Kedua (Maks. 2 Char): ", 2)
    print("Pilih Operasi Matematika:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    
    operasi = input("Masukkan pilihan operasi (1/2/3/4): ")
    
    if operasi == "1":
        hasil = angka1 + angka2
        simbol = "+"
    elif operasi == "2":
        hasil = angka1 - angka2
        simbol = "-"
    elif operasi == "3":
        hasil = angka1 * angka2
        simbol = "*"
    elif operasi == "4":
        if angka2 != 0:
            hasil = angka1 / angka2
            simbol = "/"
        else:
            print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
            return
    else:
        print("Operasi tidak valid.")
        return
    
    print(f"Hasil: {angka1} {simbol} {angka2} = {hasil}")

kalkulator()
