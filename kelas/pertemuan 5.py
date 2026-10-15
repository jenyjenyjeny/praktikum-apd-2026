# kartu = {"kartu merah", "kartu merah", "kartu hijau", "kartu biru"}
# print(kartu)

# list
# kartu = ("kartu merah", "kartu merah", "kartu hijau", "kartu biru")
# set_kartu = set(kartu)
# print(set_kartu)

# tuple
# buah = set(("apel", "jeruk", "mangga", "apel"))
# print(buah)

# akses element set
# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka)

# nambah element set
# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# hapus element set
# buah = {"apel", "mangga", "jeruk"}
# buah.remove("mangga")
# print(buah)

# operasi himpunan set
# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)

# angka1 = {1, 2, 3, 4, 5}
# angka2 = {4, 5, 6, 7, 8}
# irisan = angka1.intersection(angka2)
# print(irisan)

# angka1 = {1, 2, 3, 4, 5}
# angka2 = {4, 5, 6, 7, 8}
# irisan = angka1.difference(angka2)
# print(irisan)

# angka1 = {1, 2, 3, 4, 5}
# angka2 = {4, 5, 6, 7, 8}
# irisan = angka1.update(angka2)
# print(angka1)

# dictionary
# Praktikum = {
#     "APD" : "Belajar Dictionary",
#     "Orsikom" : "Belajar Logism",
# }
# print(Praktikum)
# print(Praktikum["Orsikom"])

# biodata = {
#     "nama" : "jeny",
#     "nim" : 046,
#     "pacar" : ["laptop", "anime"],
#     "sosmed" : "instagram",
# }
# print(biodata)

# List_game = dict(Genshin_Impact="Open World", Mole="Moba",
# Stardew_Valley="Farming Simulation")
# print(List_game)

# Biodata = {
#     "Nama" : "Siti Julpa",
#     "NIM" : 25091060,
#     "KRS" : ["Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Instagram" : "julpatarr"
# }
# print(f"Nama saya adalah {Biodata['Nama']}")
# print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} dan {Biodata['KRS'][1]}")

# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

# game = {
#     "pou" : "chill",
#     "genshin impact" : "action",
#     "valorant" : "fps",
#     "minecraft" : "sandbox",
#     "mobile legend" : "moba"
# }
# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)

# for i in game.values():
#     print(i)

# for i, j in game.items():
#     print(f"{i} adalah jenis game {j}")

# game.update({"resident evil" : "horror"})
# print(game)

# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))

# print(game)
# game["genshin impact"] = "adventure"
# print(game)

# print(game)
# game.update({"genshin impact" : "adventure"})
# print(game)

# aset = {
#     "jenis" : "rumah",
#     "harga" : 120000000,
#     "alamat" : "Jl. Raya No. 1",
#     "berpenghuni" : True,
#     "luas" : "120m x 80m"
# }
# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# print(aset)
# aset.clear()
# print(aset)

# print("Panjang dictionary :", len(aset))
# print(len(aset))

# menu = {
#     "ayam geprek" : 15000,
#     "ayam goreng" : 13000,
#     "ayam bakar" : 17000,
#     "nasi goreng" : 12000,
#     "mie goreng" : 10000
# }
# menu_baru = menu.copy()
# menu_baru["nasi goreng"] = 15000
# print(menu)
# print(menu_baru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000

# menu = dict.fromkeys(key, value)
# print(menu)

# menu = {
#     "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
#     "nasi" : ["nasi goreng", "nasi uduk"],
#     "mie" : ["mie goreng rendang", "mie goreng aceh"],
#     "kuah" : ["soto", "rawon", "sop iga"]
# }
# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
#     for kategori in j:
#         print(kategori)
#     print("")