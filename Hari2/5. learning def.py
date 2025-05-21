def cek_angka():
	try:
		angka = int(input("Masukkan Angka: "))
		if angka <= 1:
			print(f'Angka {angka} Bukan Bilangan Prima')
		elif angka % 2 != 0 and angka % 3 != 0 and angka % 5 != 0 and angka % 7 != 0:
			print(f"Angka {angka} Bukan Bilangan Prima")
		else:
			print(f"Bilangan {angka} adalah angka Prima")
	except ValueError:
		print("Angka Invalid")
cek_angka()

