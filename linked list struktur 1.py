class Node:
    def _init_(self, nama_menu, harga, jumlah):
        self.nama_menu = nama_menu
        self.harga = harga
        self.jumlah = jumlah
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def tambahkan_pesanan(self, nama_menu, harga, jumlah):
        new_node = Node(nama_menu, harga, jumlah)
        new_node.next = self.head
        self.head = new_node

    def menampilkan_pesanan(self):
        current = self.head
        while current:
            print(f"{current.jumlah} {current.nama_menu} - Rp{current.harga * current.jumlah}")
            current = current.next

    