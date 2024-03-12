class Node:
    def init(self, menu, harga):
        self.menu = menu
        self.harga = harga
        self.next = None

class LinkedList:
    def init(self):
        self.head = None

    def tambah_pesanan(self, menu, harga):
        new_node = Node(menu, harga)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def tampilkan_pesanan(self):
        if not self.head:
            print("Keranjang pesanan kosong")
        else:
            current = self.head
            index = 1
            while current:
                print(f"{index}. {current.menu} -> {current.harga} rupiah")
                current = current.next
                index += 1

   