# PROGRAM ATM SEDERHANA MENGGUNAKAN BAHASA PEMROGRAMAN PYTHON
pin = '123456'
saldo = 0
saldoTab = 0

print('========= APLIKASI PENCATATAN UANG DIGITAL ========= ')

for i in range(3):
    print()
    inPin = input("Silahkan masukkan 6 digit pin anda : ")
    if inPin == pin :
        print()
        print("==== PIN yang Anda masukkan benar === ")
        print()
        break

    else :
        print("PIN salah")
        if i == 2 :
            print("============================================")
            print(" Akun anda kami tangguhkan selama 24 jam")
            print("============================================")
            quit()

pilihan = 'y'
while (pilihan == 'y'):
    print('01. Silahkan pilih 1 untuk informasi saldo')
    print('02. Silahkan pilih 2 untuk Tambah saldo ')
    print('03. Silahkan pilih 3 untuk Ambil Saldo')
    print('04. Silahkan pilih 4 untuk keluar Aplikasi')
    print()

    menu = input('Silahkan pilih menu yang anda inginkan : ')
    print("===================================================")

    if menu == '1':
        print(f"[1] Sisa saldo umum anda saat ini adalah : Rp. {saldo}")
        print(f"[2] Sisa saldo tabungan anda saat ini adalah : Rp.{saldoTab}")
        print("===================================================")
    
    elif menu == '2':

        print('01. Silahkan pilih 1 untuk tambah saldo umum')
        print('02. Silahkan pilih 2 untuk tambah saldo tabungan')
        print("===================================================")

        menu = input('Silahkan pilih menu penyimpanan :  ')
        print("===================================================")

        if menu=='1':
                setor = int(input("Silahkan masukkan nominal yang ingin di tambahkan : Rp. "))
                saldo = saldo + setor
                print()
                print(f" Tambah saldo sebesar : Rp. { setor} , Berhasil.")
                print(f"[1] Sisa saldo umum anda saat ini adalah : Rp. {saldo}")
                print(f"[1] Sisa saldo tabungan anda saat ini adalah : Rp.{saldoTab}")

        elif menu=='2':
                setorTab = int(input("Silahkan masukkan nominal yang ingin di tambahkan : Rp."))
                saldoTab = saldoTab + setorTab
                print()
                print(f" Tambah saldo sebesar : Rp. { setorTab} , Berhasil.")
                print(f"[1] Sisa saldo umum anda saat ini adalah : Rp.{saldo}")
                print(f"[1] Sisa saldo tabungan anda saat ini adalah : Rp. {saldoTab}")

        
    elif menu == '3':

        print('01. Silahkan pilih 1 untuk ambil saldo umum')
        print('02. Silahkan pilih 2 untuk ambil saldo tabungan')

        menu = input('Silahkan pilih menu penyimpanan : ')
        print("===================================================")

        if menu=='1':
                tunai = int(input("Jumlah ambil saldo anda pada penyimpanan umum: Rp. "))
                saldo == saldo - tunai
                print()    
                print(f" Ambil saldo sebesar : Rp. { tunai} , Berhasil.")
                print(f"[1] Sisa saldo umum anda saat ini adalah : Rp.{saldo - tunai}")
                print(f"[1] Sisa saldo tabungan anda saat ini adalah : Rp. {saldoTab}")
                
        
        elif menu=='2':
                tunaiTab = int(input("Jumlah penarikan anda pada penyimpanan tabungan: Rp. "))
                saldoTab == saldoTab - tunaiTab
                print()
                print(f"Ambil saldo sebesar : Rp. { tunaiTab}")
                print(f"[1] Sisa saldo umum anda saat ini adalah : Rp. {saldo-tunai}")
                print(f"[1] Sisa saldo tabungan anda saat ini adalah : Rp. {saldoTab -tunaiTab}")
                 
    elif menu == '4':
        print("=========================================================")
        print("========= KARTU ANDA AKAN KELUAR DARI APLIKASI ==========")
        print()
        print("=== TERIMA KASIH SUDAH MENGGUNAKAN LAYANAN APLIKASI PENCATATAN UANG DIGITAL ===")
        print()
        print("=========================================================")


    print()
    print("=========================================================")
    pilihan = input("Apakah ingin melanjutkan program (y/n)? ")
    print("=========================================================")