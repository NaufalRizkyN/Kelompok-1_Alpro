 
def remove_road(self, start_city, end_city):
        if (start_city, end_city) in self.roads:
            del self.roads[(start_city, end_city)]
            print(f"Jalan dari {start_city} ke {end_city} berhasil dihapus.")
        else:
            print("Jalan tidak ditemukan.")
 
def display_cities(self):
        if self.cities:
            print("Kota-kota yang ada:")
            for city in self.cities:
                print("-", city)
        else:
            print("Belum ada kota yang ditambahkan.")
def display_roads(self):
        if self.roads:
            print("Jalan-jalan yang ada:")
            for road, road_name in self.roads.items():
                print(f"- Dari {road[0]} ke {road[1]} ({road_name}), jarak: {self.cities[road[0]][road[1]]}")
        else:
            print("Belum ada jalan yang ditambahkan.")

def dijkstra(self, start_city, end_city):
        if start_city in self.cities and end_city in self.cities:
            distances = {city: float('inf') for city in self.cities}
            distances[start_city] = 0
            visited = set()
            while True:
                current_city = min((city for city in distances if city not in visited), key=distances.get)
                visited.add(current_city)
                if current_city == end_city:
                    break
                for neighbor, distance in self.cities[current_city].items():
                    if neighbor not in visited:
                        new_distance = distances[current_city] + distance
                        if new_distance < distances[neighbor]:
                            distances[neighbor] = new_distance
            return distances[end_city]
        else:
            return "Salah satu atau kedua kota tidak ditemukan."
           