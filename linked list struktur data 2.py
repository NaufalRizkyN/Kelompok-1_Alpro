def hitung_total_harga(self):
        total_harga = 0
        current = self.head
        while current:
            total_harga += current.harga * current.jumlah
            current = current.next
        return total_harga

# Menu Miexue
menu_miexue = {
    'Miexue Ice Cream' : 5000,
    'Boba Shake'       : 16000,
    'Mi Sundae'        : 14000,
    'Mi Ganas'         : 11000,
    'Creamy Mango Boba': 22000
}

# Inisialisasi linked list
keranjang_pesanan = LinkedList()

# Daftar menu 
print("    Selamat Datang Di Warkop D4 MIE      ")
print("        Tersedia Menu Ice & Mie          ")

print("====================================")
print("       Menu Aplikasi Pemesanan      ")
print("             D4 MIE&XUE             ")
print("====================================")

print("1. Miexue Ice Cream     : Rp 5.000 ")
print("2. Boba Shake           : Rp 16.000")
print("3. Mi Sundae            : Rp 14.000")
print("4. Mi Ganas             : Rp 11.000")
print("5. Creamy Mango Boba    : Rp 22.000")

print("====================================")

# Fungsi untuk menambah pesanan ke keranjang
def tambah_pesanan_ke_keranjang(menu):
    for nama_menu, harga in menu.items():
        pesan = input(f"Apakah Ingin Memesan {nama_menu}? (y/n): ")
        if pesan.lower()=='y':
            Jumlah = int(input(f"Jumlah pesanan {nama_menu} "))
            keranjang_pesanan.tambahkan_pesanan(nama_menu, harga, Jumlah)
        