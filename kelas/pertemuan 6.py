# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas
# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang())

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# #Kita panggil fungsinya lalu argumen kita adalah angka 7
# print("Luas persegi:", luas_persegi(7))

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas
# def total_harga_tanah(panjang, lebar, harga = 100000):
#     total = luas_persegi_panjang(panjang, lebar) * harga
#     return total
# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang(7, 4))
# print("Total harga tanah:", total_harga_tanah(7, 4))

# #Tanpa parameter
# def pengumuman():
#     print("Hari ini Pengujian Proyek Akhir")
# #Pemanggilan Prosedur
# pengumuman()

# #Dengan parameter 
# def sapa_pengguna(nama_pengguna):
#     print(f"Halo, selamat datang {nama_pengguna}")
# #Pemanggilan Prosedur
# sapa_pengguna("Citra")

# #Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"

# #Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

# #Mengakses variabel lokal
# data()

# #Mengakses variabel global
# print("Nama:", nama)
# print("Prodi:", prodi)

# def faktorial(n):
#     #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1: 
#         return 1
#     #Rekursive Case: Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")


# umur = int(input('Masukkan Angka : '))
# print(umur) #input 'cinta APD'

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)'
# else :
#     print(f'Angka yang kamu input : {angka}')

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print(f'Angka yang kamu input : {angka}')
# finally:
#     print('Blok Try Selesai')

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(e)