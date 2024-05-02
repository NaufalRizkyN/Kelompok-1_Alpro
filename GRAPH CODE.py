class Peta:
    def _init_(self):
        self.kota = {}
        self.jalan = {}

    def tambah_kota(self, nama_kota):
        if nama_kota not in self.kota:
            self.kota[nama_kota] = set()
            print(f"Kota {nama_kota} berhasil ditambahkan.")
        else:
            print("Kota sudah ada.")

    def tambah_jalan(self, kota_awal, kota_tujuan, nama_jalan):
        if kota_awal in self.kota and kota_tujuan in self.kota:
            if kota_tujuan not in self.kota[kota_awal]:
                self.kota[kota_awal].add(kota_tujuan)
                self.jalan[(kota_awal, kota_tujuan)] = nama_jalan
                print(f"Jalan dari {kota_awal} ke {kota_tujuan} ({nama_jalan}) berhasil ditambahkan.")
            else:
                print(f"Jalan dari {kota_awal} ke {kota_tujuan} sudah ada.")
        else:
            print("Salah satu atau kedua kota tidak ditemukan.")

    def hapus_jalan(self, kota_awal, kota_tujuan):
        if (kota_awal, kota_tujuan) in self.jalan:
            del self.jalan[(kota_awal, kota_tujuan)]
            print(f"Jalan dari {kota_awal} ke {kota_tujuan} berhasil dihapus.")
        else:
            print("Jalan tidak ditemukan.")

    def tampilkan_kota(self):
        if self.kota:
            print("Kota-kota yang ada:")
            for kota in sorted(self.kota):
                print("-", kota)
        else:
            print("Belum ada kota yang ditambahkan.")

    def tampilkan_jalan(self):
        if self.jalan:
            print("Jalan-jalan yang ada:")
            for jalan, nama_jalan in sorted(self.jalan.items()):
                print(f"- Dari {jalan[0]} ke {jalan[1]} ({nama_jalan})")
        else:
            print("Belum ada jalan yang ditambahkan.")

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