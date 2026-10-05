print("\n🚒 Sistem Rekapitulasi Sebaran Titik Api Karhutla 🔥")

while True:
    print("\n📃 Form Login Pengguna (●ˇ∀ˇ●)")
    username = input("\nMasukkan username: ").lower()
    password = input("Masukkan password: ").lower()

    if username == "" and password == "":
        print("\nUsername dan password tidak boleh kosong!")
        continue
    elif username == "":
        print("\nUsername tidak boleh kosong!")
        continue
    elif password == "":
        print("\nPassword tidak boleh kosong!")
        continue
    elif username != "jeny" and password != "046":
        print("\nUsername dan password tidak valid!")
    elif username != "jeny":
        print("\nUsername tidak valid!")
    elif password != "046":
        print("\nPassword tidak valid!")
    else:
        print("\nLogin berhasil! Selamat datang,", username, "(❁´◡`❁)")
        break

kalimantan_gambut = 0
kalimantan_mineral = 0
sumatera_gambut = 0
sumatera_mineral = 0

while True:
    print("\n📃 Input Wilayah dan Jenis Lahan 🌳")
    while True:
        pulau = input("\nMasukkan Pulau (Kalimantan/Sumatera): ").lower()
        if pulau == "":
            print("\nNama pulau tidak valid!")
        elif pulau == "kalimantan":
            while True:
                lahan = input("Masukkan Lahan (Gambut/Mineral): ").lower()
                if lahan == "":
                    print("\nJenis lahan tidak valid!")
                elif lahan == "gambut":
                    break
                elif lahan == "mineral":
                    break
                else:
                    print("\nJenis lahan tidak tersedia!")
            break
        elif pulau == "sumatera":
            while True:
                lahan = input("Masukkan Lahan (Gambut/Mineral): ").lower()
                if lahan == "":
                    print("\nJenis lahan tidak valid!")
                elif lahan == "gambut":
                    break
                elif lahan == "mineral":
                    break
                else:
                    print("\nJenis lahan tidak tersedia!")
            break
        else:
            print("\nNama pulau tidak tersedia!")
    print("\n📃 Luas Lahan yang Terbakar 🔥")
    while True:
        titik_api = input("\nMasukkan Jumlah Titik Api: ")
        if titik_api == "":
            print("\nJumlah titik api tidak valid!")
        elif not titik_api.isdigit():
            print("\nJumlah titik api tidak valid!")
        else:
            titik_api = int(titik_api)
            break

    luas = titik_api * 5
    
    if pulau == "kalimantan":
        if lahan == "gambut":
            kalimantan_gambut += luas
        else:
            kalimantan_mineral += luas
    elif pulau == "sumatera":
        if lahan == "gambut":
            sumatera_gambut += luas
        else:
            sumatera_mineral += luas

    print("\n📃 Hasil Pendataan ✏️")
    print("\nWilayah :", pulau)
    print("Jenis Lahan :", lahan)
    print("Jumlah Titik Api :", titik_api)
    print("Luas Lahan :", luas, "hektare")

    while True:    
        ulang = input("\nInput data titik api lagi? (y/t): ").lower()
        if ulang == "":
            print("\nInput tidak valid!")
        elif ulang != "y" and ulang != "t":
            print("\nInput tidak valid!")
        else:
            break
    if ulang == "t":
        break

total = (kalimantan_gambut + kalimantan_mineral
         + sumatera_gambut + sumatera_mineral)

print("\n🚒 Hasil Akhir Rekapitulasi Sebaran Titik Api Karhutla 🔥")
print("\nKalimantan-Gambut :", kalimantan_gambut, "Hektare")
print("Kalimantan-Mineral:", kalimantan_mineral, "Hektare")
print("Sumatera-Gambut   :", sumatera_gambut, "Hektare")
print("Sumatera-Mineral  :", sumatera_mineral, "Hektare")
print("\nTotal Luas Lahan yang Terbakar  :", total, "Hektare")
print("\nTerima kasih atas partisipasi Anda! 🙏")
