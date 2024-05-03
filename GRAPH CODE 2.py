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
            