      
# Fungsi untuk menampilkan pesanan yang sudah ditambahkan
def tampilkan_pesanan_ditambahkan():
    print("-------------------------------------------")
    print("\nTotal Pesanan anda :")
    keranjang_pesanan.menampilkan_pesanan()

# Fungsi untuk menampilkan jumlah harga yang dibayarkan
def tampilkan_jumlah_harga():
    total_harga = keranjang_pesanan.hitung_total_harga()
    print("-------------------------------------------")
    print(f"\nTotal harga pesanan: Rp{total_harga}")

# Fungsi untuk pembayaran
def bayar_pesanan():
    total_harga = keranjang_pesanan.hitung_total_harga()
    print(f"Total harga yang harus dibayarkan: Rp{total_harga}")
    
    while True:
        uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: Rp"))
        if uang_bayar >= total_harga:
            kembalian = uang_bayar - total_harga
            print(f"Pembayaran berhasil. Kembalian: Rp{kembalian}")
            print("-------------------------------------------")
            print("")
            print("-----Terima Kasih Telah Memesan Warkop D4 MIE------")
            break
        else:
            print("Uang yang dibayarkan kurang. Mohon masukkan jumlah uang yang cukup.")

# Main program
tambah_pesanan_ke_keranjang(menu_miexue)
tampilkan_pesanan_ditambahkan()
tampilkan_jumlah_harga()
bayar_pesanan()