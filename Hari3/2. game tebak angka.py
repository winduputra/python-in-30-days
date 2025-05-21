import random

def tebak_angka():
    angka = random.randint(1, 100)
    print("Selamat datang di permainan tebak angka!")
    print("Kesempatan Anda adalah 100 kali.")
    kesempatan = 10
    score = 0
    while kesempatan > 0:
        try:
            tebakan = int(input("Tebak angka antara 1 dan 10: "))
            if tebakan < 1 or tebakan > 100:
                print("Tebakan harus antara 1 dan 100.")
                continue
            if tebakan == angka:
                print("Selamat! Anda menebak angka dengan benar.")
                break
            elif tebakan < angka:
                kesempatan -= 1
                print(f"Tebakan terlalu rendah! Anda memiliki {kesempatan} kesempatan tersisa.")
            elif tebakan > angka:
                kesempatan -= 1
                print(f"Tebakan terlalu tinggi! Anda memiliki {kesempatan} kesempatan tersisa.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
    if kesempatan == 0:
        print(f"Kesempatan Anda habis! Angka yang benar adalah {angka}.")
    if tebakan == angka:
        score = kesempatan * 10
        print(f"Skor Anda: {score}")
        with open("score.txt", "a") as file:
            file.write(f"Nama: {input('Masukkan Nama Anda: ')}, Skor: {score}\n")
tebak_angka()

def main():
    while True:
        tebak_angka()
        if input("Apakah Anda ingin bermain lagi? (y/n): ").lower() != 'y':
            print("Terima kasih telah bermain!")
            break
main()