book1 = [
    {"title": "Harry Potter", "Tahun Terbit": 1997, "Harga": 100000},
    {"title": "Lord of the Rings", "Tahun Terbit": 1954, "Harga": 150000},
    {"title": "The Hobbit", "Tahun Terbit": 1937, "Harga": 120000},
]
book2 = [
    {"title": "Learning Python", "Tahun Terbit": 2000, "Harga": 200000},
    {"title": "Python Crash Course", "Tahun Terbit": 2015, "Harga": 250000},
    {"title": "Automate the Boring Stuff with Python", "Tahun Terbit": 2015, "Harga": 300000},
]

daftar_buku = [book1, book2]
kategori_buku = {"Novel", "Programming"}

buku_baru = {
    "title": "The Catcher in the Rye",
    "Tahun Terbit": 1951,
    "Harga": 180000,
}
daftar_buku.append(buku_baru)
kategori_buku.add("Novel")

print("Daftar Buku:", daftar_buku)
print("Kategori Buku:", kategori_buku)