keranjang_pesanan = LinkedList()

while True:
    print("\nMenu:")
    print("1. Tambah pesanan ke keranjang")
    print("2. Tampilkan pesanan yang sudah ditambahkan")
    print("3. Jumlah Harga yang dibayarkan")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        menu = input("Masukkan nama menu: ")
        if menu in menu_miexue:
            harga = menu_miexue[menu]
            keranjang_pesanan.tambah_pesanan(menu, harga)
            print(f"{menu} sudah ditambahkan ke keranjang")
        else:
            print("Menu tidak tersedia")
    
    elif pilihan == "2":
        print("Pesanan yang sudah ditambahkan:")
        keranjang_pesanan.tampilkan_pesanan()
    
    elif pilihan == "3":
        total_harga = keranjang_pesanan.hitung_total()
        print(f"Total biaya yang harus dibayarkan adalah {total_harga} rupiah")
        break
    
    elif pilihan == "4":
        break
    
    else:
        print("Pilihan tidak valid")