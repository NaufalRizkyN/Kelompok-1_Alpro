class Map:
    def __init__(self):
        self.cities = {}
        self.roads = {}

    def add_city(self, city_name):
        if city_name not in self.cities:
            self.cities[city_name] = {}
            print(f"Kota {city_name} berhasil ditambahkan.")
        else:
            print("Kota sudah ada.")

    def add_road(self, start_city, end_city, road_name, distance):
        if start_city in self.cities and end_city in self.cities:
            if end_city not in self.cities[start_city]:
                self.cities[start_city][end_city] = distance
                self.roads[(start_city, end_city)] = road_name
                print(f"Jalan dari {start_city} ke {end_city} ({road_name}) berhasil ditambahkan.")
            else:
                print(f"Jalan dari {start_city} ke {end_city} sudah ada.")
        else:
            print("Salah satu atau kedua kota tidak ditemukan.")
