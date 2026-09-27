print("🌟 Welcome to Angkasa Music Streaming! (●'◡'●)")

nama = "Jeny Najla Ariyani"
nim = "46"

biaya_langganan = 1500000

print("\nPlease fill in your name and NIM first (❁´◡`❁)")
nama = input("Your Name: ")
nim = input("NIM: ")

if nama == "Jeny Najla Ariyani" and nim == "46":
    print("\nLogin successful. Welcome,", nama, "o(〃＾▽＾〃)o !")
    print("\nLet's Take A Look to Our PLan(et) (✿ ◡‿◡) ~")
    print("1. Orbit Plan(et) - Fee 1%" + "+ Free access to All Popular Songs")
    print("2. Nebula Plan(et) - Fee 3%" + "+ Free access to All Premium Songs and Playlist Customs")
    print("3. Galaxy Plan(et) - Fee 5%" + "+ Free access to All Premium Songs, Playlist Customs, and Offline Mode")
    print("4. Su-su-supernova Plan(et) - Fee 7%" + "+ Free access to All Featured Songs, Playlist Customs, Offline Mode, and Exclusive Artist Content ")

    1 == "1. Orbit Plan(et) - Fee 1%" + "+ Free access to All Popular Songs"
    2 == "2. Nebula Plan(et) - Fee 3%" + "+ Free access to All Premium Songs and Playlist Customs"
    3 == "3. Galaxy Plan(et) - Fee 5%" + "+ Free access to All Premium Songs, Playlist Customs, and Offline Mode"
    4 == "4. Su-su-supernova Plan(et) - Fee 7%" + "+ Free access to All Featured Songs, Playlist Customs, Offline Mode, and Exclusive Artist Content "

    pilihan = input("\nWe would to like know which one is ur fayyvorite plan(et) [1/2/3/4]: ")
    if pilihan == "1":
        paket = ("Orbit Plan(et)")
        persen_admin = 0.01
        fitur = ("Free access to All Popular Songs")
    elif pilihan == "2":
        paket = ("Nebula Plan(et)")
        persen_admin = 0.03
        fitur = ("Free access to All Premium Songs and Playlist Customs")
    elif pilihan == "3":
        paket = ("Galaxy Plan(et)")
        persen_admin = 0.05
        fitur = ("Free access to All Premium Songs, Playlist Customs, and Offline Mode")
    elif pilihan == "4":
        paket = ("Su-su-supernova Plan(et)")
        persen_admin = 0.07
        fitur = ("Free access to All Featured Songs, Playlist Customs, Offline Mode, and Exclusive Artist Content")
    else:
        print("\nInvalid choice. Please select a valid plan(et).")

    if paket != "":
        biaya_admin = int(biaya_langganan * persen_admin)
        total_bayar = biaya_langganan + biaya_admin

        print("\n📃 Angkasa Payment Details:")

        print("\nYour Name:", nama)
        print("Selected Plan(et):", paket)
        print("Features Included:", fitur)
        print(f"Subscription Fee: Rp {biaya_langganan:,}".replace(",", "."))
        print(f"Admin Fee: Rp {biaya_admin:,}".replace(",", "."))
        print(f"Total Payment: Rp {total_bayar:,}".replace(",", ".")) 
        
        response = input("\nDo you want to proceed with the payment? (yes/no): ")
        if response.lower() == "yes":
            print("\nPayment successful. Thank you for choosing Angkasa's Plan(et) (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        else:
            print("\nPayment cancelled. Please restart the program if you wish to make a new selection.")

    else:
        print("\nNo plan(et) selected. Please restart the program and choose a valid plan(et).")

else:
    print("\nLogin failed. Please check your name and NIM.")