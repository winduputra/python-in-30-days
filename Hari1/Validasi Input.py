while True:
    try:
        nama = input("Masukkan nama: ").strip()
        umur = input("Masukkan Umur: ")
        umur = int(umur)
        thn_lahir = 2025 - int(umur)
       
        if not nama.isalpha():
            print("Nama Hanya Boleh Mengandung Huruf!")
            continue
       
        if umur < 0:
            print("Umur Tidak Boleh Negatif!")
            continue
        
        elif umur > 120:
            print("Umur Anda Tidak Masuk Akal!")
            continue
        
        else:
            break
 
    except ValueError:
        print("Umur Harus Angka!")

print(f"Nama Anda: {nama}")
print(f"Umur Anda: {umur}")
print(f"Tahun Lahir Anda: {thn_lahir}")
