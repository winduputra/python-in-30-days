while True:
    x = input("Masukkan angka: ")
    if x == "":
        print("Input tidak boleh kosong")
        continue
    try:
        x = int(x)
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        continue
    break

kuadrat = lambda x: x**2
print("Kuadrat dari", x, "adalah", kuadrat(x))