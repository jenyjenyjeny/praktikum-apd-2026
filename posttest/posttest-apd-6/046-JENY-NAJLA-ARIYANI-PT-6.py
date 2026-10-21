import os
import random

akun = {
    "admin": {"password": "admin123", "peran": "admin"}
}

karakter = {}
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

        if not (3 <= len(username) <= 20):
            print("\nUsername harus terdiri dari 3-20 karakter.")
        elif not username.isascii() or not username.isalnum():
            print("\nUsername hanya boleh berisi huruf dan angka.")
        elif username in akun:
            print("\nUsername sudah digunakan.")
        elif not (3 <= len(password) <= 30) or password.strip() == "":
            print("\nPassword harus terdiri dari 3-30 karakter.")
        else:
            akun[username] = {"password": password, "peran": "pengguna"}
            print("\nRegister berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")

    elif pilihan == "1":
        print("\n== LOGIN ==")
        username = input("\nUsername: ").strip().lower()
        password = input("Password: ")
        peran = ""
        if username in akun and akun[username]["password"] == password:
            peran = akun[username]["peran"]

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
                    skill_awal = {}
                    for nama_skill in pilihan_skill:
                        skill_awal[nama_skill] = 0
                    statistik_awal = {}
                    for nama_statistik in jenis_statistik:
                        statistik_awal[nama_statistik] = 0
                    karakter[str(id_berikutnya)] = {
                        "pemilik": username,
                        "nama": nama,
                        "level": 0,
                        "skill": skill_awal,
                        "senjata": "Pedang Kayu",
                        "level_senjata": 0,
                        "statistik": statistik_awal
                    }
                    print("Karakter berhasil dibuat! ID:", id_berikutnya)
                    print("\nLevel: 0 | Senjata: Pedang Kayu")
                    print("HP: 30 | ATK: 6 | DEF: 0")
                    print("Racun: 🔐 | Beku: 🔐 | Penghindaran: 🔐")
                    id_berikutnya += 1

            elif menu in ("2", "3", "4", "6"):
                print("\n== INFORMASI KARAKTER ==")
                jumlah = 0
                for id_karakter, data in karakter.items():
                    if peran == "admin" or data["pemilik"] == username:
                        hp_maksimal = 30 + 10 * data["statistik"]["HP"]
                        atk = 6 + 2 * data["statistik"]["ATK"] + data["level_senjata"]
                        pertahanan = 2 * data["statistik"]["DEF"]
                        print("Pemain:", data["pemilik"], "| ID:", id_karakter)
                        print("\nNama Karakter:", data["nama"], "| Level:", data["level"])
                        print("Senjata:", data["senjata"], "| Level:", data["level_senjata"])
                        print("HP:", hp_maksimal, "| ATK:", atk, "| DEF:", pertahanan)
                        print("\nSkill:")
                        for nama_skill, level_skill in data["skill"].items():
                            if level_skill == 0:
                                print("-", nama_skill, "| Level: 🔐 (terkunci)")
                            else:
                                print("-", nama_skill, "| Level:", level_skill)
                        jumlah += 1

                if jumlah == 0:
                    print("\nKarakter tidak ditemukan.")
                elif menu in ("3", "4", "6"):
                    id_teks = input("\nMasukkan ID karakter: ").strip()
                    if id_teks not in karakter:
                        print("\nID tidak ditemukan.")
                    elif peran != "admin" and karakter[id_teks]["pemilik"] != username:
                        print("\nID tidak ditemukan.")

                    elif menu == "3":
                        print("1. Ubah nama | 2. Ganti senjata")
                        ubah = input("\nPilih perubahan: ").strip()
                        if ubah == "1":
                            nama_baru = input("Nama baru: ").strip()
                            if 1 <= len(nama_baru) <= 30:
                                karakter[id_teks]["nama"] = nama_baru
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
                                if senjata_baru == karakter[id_teks]["senjata"]:
                                    print("\nSenjata sudah digunakan.")
                                else:
                                    karakter[id_teks]["senjata"] = senjata_baru
                                    karakter[id_teks]["level_senjata"] = 0
                                    print("\nSenjata berhasil diganti. Level: 0")
                            else:
                                print("\nPilihan senjata tidak valid.")
                        else:
                            print("\nPilihan perubahan tidak valid.")

                    elif menu == "4":
                        konfirmasi = input("Hapus karakter ini? (y/t): ").strip().lower()
                        if konfirmasi == "y":
                            del karakter[id_teks]
                            print("\nKarakter beserta datanya berhasil dihapus.")
                        else:
                            print("\nPenghapusan dibatalkan.")

                    elif menu == "6":
                        print("\n== ⚔️ PETUALANGAN: HUTAN TERLARANG 🌲 ==")
                        print("> Kalahkan monster untuk mendapatkan hadiah.")
                        print("> Skill akan terbuka setelah pemain menyelesaikan petualangan.")
                        print("> Skill yang aktif mempunyai jeda 3 giliran.")
                        print("> Jika pemain kalah/kabur, maka tidak akan mendapatkan hadiah.")
                        level = karakter[id_teks]["level"]
                        hp_pemain = 30 + 10 * karakter[id_teks]["statistik"]["HP"]
                        atk_pemain = (6 + 2 * karakter[id_teks]["statistik"]["ATK"]
                                      + karakter[id_teks]["level_senjata"])
                        def_pemain = 2 * karakter[id_teks]["statistik"]["DEF"]
                        musuh = random.choice(daftar_monster)
                        (nama_musuh, hp_dasar, atk_dasar) = musuh
                        hp_musuh = hp_dasar + 2 * level
                        atk_musuh = atk_dasar + level // 3
                        skill = karakter[id_teks]["skill"]
                        cooldown = {"Racun": 0, "Beku": 0, "Penghindaran": 0}
                        racun_giliran = 0
                        kabur = False

                        print("\nSaat sedang menjelajahi hutan terlarang, kamu bertemu dengan", nama_musuh)
                        print("Segera kalahkan musuh!")
                        
                        while hp_pemain > 0 and hp_musuh > 0:
                            print("\nHP kamu:", hp_pemain, "|", nama_musuh, "HP:", hp_musuh)
                            print("1. Serang dengan", karakter[id_teks]["senjata"])
                            nomor_skill = 2
                            for nama_skill, level_skill in skill.items():
                                print(nomor_skill, ".", nama_skill, "| Level:",
                                      level_skill, "| Cooldown:", cooldown[nama_skill])
                                nomor_skill += 1
                            print("0. Kabur")
                            aksi = input("\nPilih aksi: ").strip()
                            if aksi == "0":
                                kabur = True
                                break
                            if aksi not in ("1", "2", "3", "4"):
                                print("\nAksi tidak valid!")
                                continue

                            skill_dipakai = ""
                            if aksi != "1":
                                skill_dipakai = pilihan_skill[int(aksi) - 2]
                                if skill[skill_dipakai] == 0:
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
                                peluang = min(90, 45 + 5 * skill["Beku"])
                                freeze = random.randint(1, 100) <= peluang
                                if freeze:
                                    print("\nMusuh berhasil dibekukan! Musuh melewatkan giliran ini.")
                                else:
                                    print("\nMusuh gagal dibekukan!")
                            elif aksi == "4":
                                peluang = min(90, 55 + 5 * skill["Penghindaran"])
                                dodge = random.randint(1, 100) <= peluang
                                if dodge:
                                    print("\nPenghindaran berhasil untuk giliran ini!")
                                else:
                                    print("\nPenghindaran gagal!")

                            if racun_giliran > 0 and hp_musuh > 0:
                                dmg_racun = 2 + skill["Racun"]
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

                            for nama_skill in cooldown:
                                if nama_skill == skill_dipakai:
                                    cooldown[nama_skill] = 3
                                elif cooldown[nama_skill] > 0:
                                    cooldown[nama_skill] -= 1

                        if hp_musuh == 0:
                            print("\nPetualangan berhasil! Monster dikalahkan.")
                            karakter[id_teks]["level"] += 1
                            karakter[id_teks]["level_senjata"] += 1
                            print("\n> Level karakter naik menjadi:", karakter[id_teks]["level"])
                            print("> Level senjata naik menjadi:", karakter[id_teks]["level_senjata"])
                            while True:
                                print("> Pilih satu untuk diupgrade: 1. HP | 2. ATK | 3. DEF")
                                hadiah = input("\nPilihan upgrade: ").strip()
                                if hadiah in ("1", "2", "3"):
                                    nama_statistik = jenis_statistik[int(hadiah) - 1]
                                    karakter[id_teks]["statistik"][nama_statistik] += 1
                                    print("\nLevel", nama_statistik,
                                          "naik menjadi:", karakter[id_teks]["statistik"][nama_statistik])
                                    break
                                print("\nPilihan tidak valid!")

                            nama_skill = random.choice(pilihan_skill)
                            sebelumnya = skill[nama_skill]
                            skill[nama_skill] += 1
                            if sebelumnya == 0:
                                print("Skill baru terbuka:", nama_skill)
                            else:
                                print("Skill acak ditingkatkan:", nama_skill)
                            print("Level skill sekarang:", skill[nama_skill])
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
