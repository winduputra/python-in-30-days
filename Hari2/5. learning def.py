def buat_bakso(jenis, ukuran):
    if jenis == "kecil":
        harga = 1000
    else:
        harga = 5000

    if ukuran:
        return f"Bakso {jenis} ukuran {ukuran} dengan harga {harga}"
    else:
        return f"Bakso {jenis} dengan harga {harga}"

print(buat_bakso("kecil", "besar"))


