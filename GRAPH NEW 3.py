# Inisialisasi objek peta
my_map = Map()
# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah Kota")
    print("2. Tambah Jalan")
    print("3. Hapus Jalan")
    print("4. Tampilkan Kota-kota")
    print("5. Tampilkan Jalan-jalan")
    print("6. Temukan Jarak Terpendek antar Kota")
    print("7. Keluar")

    choice = input("Pilih menu: ")

    if choice == '1':
        city_name = input("Masukkan nama kota baru: ")
        my_map.add_city(city_name)

    elif choice == '2':
        start_city = input("Masukkan nama kota awal: ")
        end_city = input("Masukkan nama kota tujuan: ")
        road_name = input("Masukkan nama jalan: ")
        distance = float(input("Masukkan jarak antara kota (dalam kilometer): "))
        my_map.add_road(start_city, end_city, road_name, distance)

    elif choice == '3':
        start_city = input("Masukkan nama kota awal: ")
        end_city = input("Masukkan nama kota tujuan: ")
        my_map.remove_road(start_city, end_city)

    elif choice == '4':
        my_map.display_cities()

    elif choice == '5':
        my_map.display_roads()

    elif choice == '6':
        start_city = input("Masukkan nama kota awal: ")
        end_city = input("Masukkan nama kota tujuan: ")
        shortest_distance = my_map.dijkstra(start_city, end_city)
        if isinstance(shortest_distance, float):
            print(f"Jarak terpendek dari {start_city} ke {end_city} adalah {shortest_distance} kilometer.")
        else:
            print(shortest_distance)

    elif choice == '7':
        print("Terima kasih! Sampai jumpa lagi.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")