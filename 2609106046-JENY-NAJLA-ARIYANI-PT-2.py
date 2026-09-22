makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000

biaya_aplikasi = 5000

harga_makanan = [
    makanan_1,
    makanan_2,
    makanan_3,
    makanan_4,
    makanan_5,
    makanan_6,
    biaya_aplikasi
]

total_bayar = (
    makanan_1 +
    makanan_2 +
    makanan_3 +
    makanan_4 +
    makanan_5 +
    makanan_6 +
    biaya_aplikasi
)

rata_rata = total_bayar / len(harga_makanan)

nim = 46

bolean = nim != rata_rata

kurs_euro = 5.77
total_euro = total_bayar * kurs_euro

print("Slice index negatif =", harga_makanan[-7:])
print("Biaya aplikasi =", biaya_aplikasi)
print("Total bayar =", total_bayar)
print("Rata rata=", rata_rata)
print("NIM=", nim)
print("Bolean=", bolean)
print("Total euro=", total_euro)