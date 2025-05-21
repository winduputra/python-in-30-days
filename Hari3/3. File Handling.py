while True:
    try:
        with open("data.txt", "r") as file:
            data = file.read()
            print(data)
            break           
    except FileNotFoundError:
        print("File tidak ditemukan. Silakan buat file data1.txt terlebih dahulu.")
        nama = input("Masukkan Nama: ")
        umur = input("Masukkan Umur: ")
        with open("data.txt", "w") as e:
            e.write(f"Nama: {nama}\nUmur: {umur} Tahun")
