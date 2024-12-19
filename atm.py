

print("Selamat datang di ATM python")
while True:
    PIN = input("Masukkan PIN anda: ")
    if PIN != "1234":
        print("PIN anda salah")
    else:
        print("Selamat datang di ATM python")
        saldo = 100000
        while True:
            print("Menu:")
            print("1. Cek Saldo")
            print("2. Tarik Tunai")
            print("3. Transfer")
            print("4. Keluar")
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                print("Saldo anda: Rp", saldo)
            elif pilihan == "2":
                nominal = int(input("Masukkan nominal tarik tunai: "))
                if nominal > saldo:
                    print("Saldo anda tidak mencukupi")
                else:
                    saldo -= nominal    
            elif pilihan == "3":
                nominal = int(input("Masukkan nominal transfer: "))
                if nominal > saldo:
                    print("Saldo anda tidak mencukupi")
                else:
                    saldo -= nominal
            elif pilihan == "4":
                print("Terima kasih telah menggunakan ATM python")
                break
            else:
                print("Pilihan menu tidak valid")
                continue
        break

