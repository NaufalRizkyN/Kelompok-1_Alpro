# Inisialisasi objek peta
peta_saya = Peta()

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah Kota")
    print("2. Tambah Jalan")
    print("3. Hapus Jalan")
    print("4. Tampilkan Kota-kota")
    print("5. Tampilkan Jalan-jalan")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        nama_kota = input("Masukkan nama kota baru: ")
        peta_saya.tambah_kota(nama_kota)

    elif pilihan == '2':
        kota_awal = input("Masukkan nama kota awal: ")
        kota_tujuan = input("Masukkan nama kota tujuan: ")
        nama_jalan = input("Masukkan nama jalan: ")
        peta_saya.tambah_jalan(kota_awal, kota_tujuan, nama_jalan)

    elif pilihan == '3':
        kota_awal = input("Masukkan nama kota awal: ")
        kota_tujuan = input("Masukkan nama kota tujuan: ")
        peta_saya.hapus_jalan(kota_awal, kota_tujuan)

    elif pilihan == '4':
        peta_saya.tampilkan_kota()

    elif pilihan == '5':
        peta_saya.tampilkan_jalan()

    elif pilihan == '6':
        print("Terima kasih! Sampai jumpa lagi.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")