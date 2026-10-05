
print("=" * 55)
print("     SISTEM REKAPITULASI TITIK API KEBAKARAN")
print("              BPBD & MANGGALA AGNI")
print("=" * 55)

# FORM LOGIN
while True:
    print("\n========== FORM LOGIN ==========")
    username = input("Masukkan Username : ").strip().lower()
    password = input("Masukkan Password : ").strip()

    if username == "" or password == "":
        print("Username dan password tidak boleh kosong!")
    elif username != "jihan" and password != "046":
        print("Username dan password salah!")
    elif username != "jihan":
        print("Username salah!")
    elif password != "046":
        print("Password salah!")
    else:
        print("\nLogin berhasil! Selamat datang,", username)
        break

# INISIALISASI TOTAL LUAS LAHAN
kalimantan_gambut = 0
kalimantan_mineral = 0
sumatera_gambut = 0
sumatera_mineral = 0

# PERULANGAN INPUT DATA
while True:
    print("\n========== INPUT DATA TITIK API ==========")

    # INPUT PULAU
    while True:
        pulau = input("Masukkan Pulau (Kalimantan/Sumatera): ").strip().upper()

        if pulau == "":
            print("Nama pulau tidak boleh kosong!")
        elif pulau != "KALIMANTAN" and pulau != "SUMATERA":
            print("Pulau tidak tersedia!")
        else:
            break

    # INPUT JENIS LAHAN
    while True:
        lahan = input("Masukkan Lahan (Gambut/Mineral): ").strip().upper()

        if lahan == "":
            print("Jenis lahan tidak boleh kosong!")
        elif lahan != "GAMBUT" and lahan != "MINERAL":
            print("Jenis lahan tidak tersedia!")
        else:
            break

    # INPUT JUMLAH TITIK API
    while True:
        hotspot = input("Masukkan Jumlah Titik Api: ").strip()

        if hotspot == "":
            print("Jumlah titik api tidak boleh kosong!")
        elif not hotspot.isdigit():
            print("Masukkan angka bulat yang tidak negatif!")
        else:
            hotspot = int(hotspot)
            break

    # KONVERSI LUAS LAHAN
    luas = hotspot * 5

    # NESTED IF UNTUK KATEGORI WILAYAH
    if pulau == "KALIMANTAN":
        if lahan == "GAMBUT":
            kalimantan_gambut += luas
        else:
            kalimantan_mineral += luas

    elif pulau == "SUMATERA":
        if lahan == "GAMBUT":
            sumatera_gambut += luas
        else:
            sumatera_mineral += luas

    print("\n========== HASIL PENDATAAN ==========")
    print("Wilayah       :", pulau)
    print("Jenis Lahan   :", lahan)
    print("Jumlah Hotspot:", hotspot)
    print("Luas Terbakar :", luas, "Hektare")

    # PENGULANGAN INPUT DATA
    while True:
        ulang = input("\nInput data lagi? (Y/T): ").strip().upper()

        if ulang == "":
            print("Pilihan tidak boleh kosong!")
        elif ulang != "Y" and ulang != "T":
            print("Masukkan Y atau T!")
        else:
            break

    if ulang == "T":
        break

# RINGKASAN AKHIR
total = (kalimantan_gambut + kalimantan_mineral
         + sumatera_gambut + sumatera_mineral)

print("\n" + "=" * 55)
print("          REKAPITULASI AKHIR KEBAKARAN")
print("=" * 55)
print("Kalimantan - Gambut :", kalimantan_gambut, "Hektare")
print("Kalimantan - Mineral:", kalimantan_mineral, "Hektare")
print("Sumatera   - Gambut :", sumatera_gambut, "Hektare")
print("Sumatera   - Mineral:", sumatera_mineral, "Hektare")
print("-" * 55)
print("Total Luas Terbakar :", total, "Hektare")
print("=" * 55)
print("Terima kasih! Pendataan telah selesai.")
