import os
import random

akun = [["admin", "admin123", "admin"]]

karakter = []
id_berikutnya = 1

pilihan_skill = ("Racun", "Beku", "Penghindaran")
jenis_statistik = ("HP", "ATK", "DEF")
pilihan_senjata = ("Pedang Kayu", "Busur Kayu", "Tongkat Kayu")
daftar_monster = (("Slime", 18, 4), ("Goblin", 24, 5),
                  ("Serigala Hutan", 30, 6))

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("== ⚔️ PETUALANGAN: HUTAN TERLARANG 🌲 ==")
    print("1. Login | 2. Register | 3. Keluar")
    pilihan = input("\nPilih menu: ").strip()

    if pilihan == "3":
        print("\nTerima kasih telah bermain!")
        break

    elif pilihan == "2":
        print("\n== REGISTER ==")
        username = input("\nUsername baru (3-20 karakter): ").strip().lower()
        password = input("Password baru (3-30 karakter): ")
        sudah_ada = False
        for data in akun:
            if data[0] == username:
                sudah_ada = True

        if not (3 <= len(username) <= 20):
            print("\nUsername harus terdiri dari 3-20 karakter.")
        elif not username.isascii() or not username.isalnum():
            print("\nUsername hanya boleh berisi huruf dan angka.")
        elif sudah_ada:
            print("\nUsername sudah digunakan.")
        elif not (3 <= len(password) <= 30) or password.strip() == "":
            print("\nPassword harus terdiri dari 3-30 karakter.")
        else:
            akun.append([username, password, "pengguna"])
            print("\nRegister berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")

    elif pilihan == "1":
        print("\n== LOGIN ==")
        username = input("\nUsername: ").strip().lower()
        password = input("Password: ")
        peran = ""
        for data in akun:
            if data[0] == username and data[1] == password:
                peran = data[2]
                break

        if peran == "":
            print("\nLogin gagal! Username atau password salah/kosong.")
            input("Tekan Enter untuk kembali...")
            continue

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("== ⚔️ MENU KARAKTER 🤺 ==")
            print("Login sebagai:", username, "| Peran:", peran)
            print("\n1. Buat karakter | 2. Lihat karakter")
            print("3. Ubah karakter | 4. Hapus karakter")
            print("5. Logout | 6. Petualangan (upgrade)")
            menu = input("\nPilih menu: ").strip()

            if menu == "1":
                print("\n== BUAT KARAKTER ==")
                nama = input("\nNama karakter (1-30 karakter): ").strip()
                if not (1 <= len(nama) <= 30):
                    print("\nNama wajib diisi, maksimal 30 karakter.")
                else:
                    skill_awal = []
                    for nama_skill in pilihan_skill:
                        skill_awal.append([nama_skill, 0])
                    statistik_awal = []
                    for nama_statistik in jenis_statistik:
                        statistik_awal.append([nama_statistik, 0])
                    karakter.append([id_berikutnya, username, nama, 0,
                                     skill_awal, "Pedang Kayu", 0,
                                     statistik_awal])
                    print("Karakter berhasil dibuat! ID:", id_berikutnya)
                    print("\nLevel: 0 | Senjata: Pedang Kayu")
                    print("HP: 30 | ATK: 6 | DEF: 0")
                    print("Racun: 🔐 | Beku: 🔐 | Penghindaran: 🔐")
                    id_berikutnya += 1

            elif menu in ("2", "3", "4", "6"):
                print("\n== INFORMASI KARAKTER ==")
                jumlah = 0
                for data in karakter:
                    if peran == "admin" or data[1] == username:
                        hp_maksimal = 30 + 10 * data[7][0][1]
                        atk = 6 + 2 * data[7][1][1] + data[6]
                        pertahanan = 2 * data[7][2][1]
                        print("Pemain:", data[1], "| ID:", data[0])
                        print("\nNama Karakter:", data[2], "| Level:", data[3])
                        print("Senjata:", data[5], "| Level:", data[6])
                        print("HP:", hp_maksimal, "| ATK:", atk, "| DEF:", pertahanan)
                        print("\nSkill:")
                        for data_skill in data[4]:
                            if data_skill[1] == 0:
                                print("-", data_skill[0], "| Level: 🔐 (terkunci)")
                            else:
                                print("-", data_skill[0], "| Level:", data_skill[1])
                        jumlah += 1

                if jumlah == 0:
                    print("\nKarakter tidak ditemukan.")
                elif menu in ("3", "4", "6"):
                    id_teks = input("\nMasukkan ID karakter: ").strip()
                    indeks = -1
                    for i in range(len(karakter)):
                        if str(karakter[i][0]) == id_teks:
                            if peran == "admin" or karakter[i][1] == username:
                                indeks = i
                                break

                    if indeks == -1:
                        print("\nID tidak ditemukan.")

                    elif menu == "3":
                        print("1. Ubah nama | 2. Ganti senjata")
                        ubah = input("\nPilih perubahan: ").strip()
                        if ubah == "1":
                            nama_baru = input("Nama baru: ").strip()
                            if 1 <= len(nama_baru) <= 30:
                                karakter[indeks][2] = nama_baru
                                print("\nNama berhasil diubah.")
                            else:
                                print("\nNama wajib diisi, maksimal 30 karakter.")
                        elif ubah == "2":
                            for i in range(len(pilihan_senjata)):
                                print(i + 1, ".", pilihan_senjata[i])
                            print("\n> Jika pemain memilih senjata yang berbeda, maka level senjata sebelumnya akan direset.")
                            senjata_teks = input("Pilih senjata: ").strip()
                            if senjata_teks in ("1", "2", "3"):
                                senjata_baru = pilihan_senjata[int(senjata_teks) - 1]
                                if senjata_baru == karakter[indeks][5]:
                                    print("\nSenjata sudah digunakan.")
                                else:
                                    karakter[indeks][5] = senjata_baru
                                    karakter[indeks][6] = 0
                                    print("\nSenjata berhasil diganti. Level: 0")
                            else:
                                print("\nPilihan senjata tidak valid.")
                        else:
                            print("\nPilihan perubahan tidak valid.")

                    elif menu == "4":
                        konfirmasi = input("Hapus karakter ini? (y/t): ").strip().lower()
                        if konfirmasi == "y":
                            del karakter[indeks]
                            print("\nKarakter beserta datanya berhasil dihapus.")
                        else:
                            print("\nPenghapusan dibatalkan.")

                    elif menu == "6":
                        print("\n== ⚔️ PETUALANGAN: HUTAN TERLARANG 🌲 ==")
                        print("> Kalahkan monster untuk mendapatkan hadiah.")
                        print("> Skill akan terbuka setelah pemain menyelesaikan petualangan.")
                        print("> Skill yang aktif mempunyai jeda 3 giliran.")
                        print("> Jika pemain kalah/kabur, maka tidak akan mendapatkan hadiah.")
                        level = karakter[indeks][3]
                        hp_pemain = 30 + 10 * karakter[indeks][7][0][1]
                        atk_pemain = (6 + 2 * karakter[indeks][7][1][1]
                                      + karakter[indeks][6])
                        def_pemain = 2 * karakter[indeks][7][2][1]
                        musuh = random.choice(daftar_monster)
                        (nama_musuh, hp_dasar, atk_dasar) = musuh
                        hp_musuh = hp_dasar + 2 * level
                        atk_musuh = atk_dasar + level // 3
                        skill = karakter[indeks][4]
                        cooldown = [0, 0, 0]
                        racun_giliran = 0
                        kabur = False

                        print("\nSaat sedang menjelajahi hutan terlarang, kamu bertemu dengan", nama_musuh)
                        print("Segera kalahkan musuh!")
                        
                        while hp_pemain > 0 and hp_musuh > 0:
                            print("\nHP kamu:", hp_pemain, "|", nama_musuh, "HP:", hp_musuh)
                            print("1. Serang dengan", karakter[indeks][5])
                            for i in range(len(skill)):
                                print(i + 2, ".", skill[i][0], "| Level:",
                                      skill[i][1], "| Cooldown:", cooldown[i])
                            print("0. Kabur")
                            aksi = input("\nPilih aksi: ").strip()
                            if aksi == "0":
                                kabur = True
                                break
                            if aksi not in ("1", "2", "3", "4"):
                                print("\nAksi tidak valid!")
                                continue

                            skill_dipakai = -1
                            if aksi != "1":
                                skill_dipakai = int(aksi) - 2
                                if skill[skill_dipakai][1] == 0:
                                    print("\nSkill masih terkunci")
                                    continue
                                if cooldown[skill_dipakai] > 0:
                                    print("\nSkill masih cooldown! Pilih aksi lain.")
                                    continue

                            freeze = False
                            dodge = False
                            if aksi == "1":
                                hp_musuh = max(0, hp_musuh - atk_pemain)
                                print("\nSerangan memberikan", atk_pemain, "DMG.")
                            elif aksi == "2":
                                racun_giliran = 3
                                print("\nMusuh diracuni selama 3 giliran.")
                            elif aksi == "3":
                                peluang = min(90, 45 + 5 * skill[1][1])
                                freeze = random.randint(1, 100) <= peluang
                                if freeze:
                                    print("\nMusuh berhasil dibekukan! Musuh melewatkan giliran ini.")
                                else:
                                    print("\nMusuh gagal dibekukan!")
                            elif aksi == "4":
                                peluang = min(90, 55 + 5 * skill[2][1])
                                dodge = random.randint(1, 100) <= peluang
                                if dodge:
                                    print("\nPenghindaran berhasil untuk giliran ini!")
                                else:
                                    print("\nPenghindaran gagal!")

                            if racun_giliran > 0 and hp_musuh > 0:
                                dmg_racun = 2 + skill[0][1]
                                hp_musuh = max(0, hp_musuh - dmg_racun)
                                racun_giliran -= 1
                                print("Racun memberikan", dmg_racun, "DMG.")

                            if hp_musuh > 0:
                                if freeze or dodge:
                                    print("Kamu berhasil menghindari serangan musuh.")
                                else:
                                    dmg = max(1, atk_musuh - def_pemain)
                                    hp_pemain = max(0, hp_pemain - dmg)
                                    print("Musuh berhasil menyerangmu! HP berkurang sebesar", dmg)

                            for i in range(len(cooldown)):
                                if i == skill_dipakai:
                                    cooldown[i] = 3
                                elif cooldown[i] > 0:
                                    cooldown[i] -= 1

                        if hp_musuh == 0:
                            print("\nPetualangan berhasil! Monster dikalahkan.")
                            karakter[indeks][3] += 1
                            karakter[indeks][6] += 1
                            print("\n> Level karakter naik menjadi:", karakter[indeks][3])
                            print("> Level senjata naik menjadi:", karakter[indeks][6])
                            while True:
                                print("> Pilih satu untuk diupgrade: 1. HP | 2. ATK | 3. DEF")
                                hadiah = input("\nPilihan upgrade: ").strip()
                                if hadiah in ("1", "2", "3"):
                                    posisi = int(hadiah) - 1
                                    karakter[indeks][7][posisi][1] += 1
                                    print("\nLevel", karakter[indeks][7][posisi][0],
                                          "naik menjadi:", karakter[indeks][7][posisi][1])
                                    break
                                print("\nPilihan tidak valid!")

                            posisi_skill = random.randint(0, 2)
                            sebelumnya = skill[posisi_skill][1]
                            skill[posisi_skill][1] += 1
                            if sebelumnya == 0:
                                print("Skill baru terbuka:", skill[posisi_skill][0])
                            else:
                                print("Skill acak ditingkatkan:", skill[posisi_skill][0])
                            print("Level skill sekarang:", skill[posisi_skill][1])
                        elif kabur:
                            print("\nKamu kembali ke desa tanpa mendapatkan hadiah.")
                        else:
                            print("\nPetualangan gagal! Tidak ada upgrade.")
            elif menu == "5":
                break
            else:
                print("Pilihan menu tidak valid.")
            input("\nTekan Enter untuk melanjutkan...")

    else:
        print("Pilihan menu tidak valid.")
        input("Tekan Enter untuk kembali...")