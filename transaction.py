"""
Modul Transaction berisi class untuk mengelola transaksi self-service cashier.
Termasuk menambah item, menghapus item, memperbarui item, menampilkan pesanan,
dan menghitung total harga beserta diskon.
"""

class Transaction:
    def __init__(self):
        """Inisialisasi dictionary untuk menyimpan daftar item belanja."""
        self.items = {}

    def add_item(self, name, qty, price):
        """Menambahkan item baru ke dalam transaksi."""
        self.items[name] = {
            "qty": qty,
            "price": price,
            "total": qty * price
        }
        print(f'Item "{name}" berhasil ditambahkan!')

    def delete_item(self, name):
        """Menghapus item berdasarkan nama."""
        if name in self.items:
            del self.items[name]
            print(f'Item "{name}" berhasil dihapus!')
        else:
            print("Item tidak ditemukan!")

    def update_item_name(self, old_name, new_name):
        """Memperbarui nama item tanpa mengubah qty/harga."""
        if old_name in self.items:
            self.items[new_name] = self.items.pop(old_name)
            print("Nama item berhasil diperbarui!")
        else:
            print("Item tidak ditemukan!")

    def update_item_qty(self, name, new_qty):
        """Memperbarui quantity item."""
        if name in self.items:
            self.items[name]["qty"] = new_qty
            self.items[name]["total"] = new_qty * self.items[name]["price"]
            print("Qty item berhasil diperbarui!")
        else:
            print("Item tidak ditemukan!")

    def update_item_price(self, name, new_price):
        """Memperbarui harga item."""
        if name in self.items:
            self.items[name]["price"] = new_price
            self.items[name]["total"] = new_price * self.items[name]["qty"]
            print("Harga item berhasil diperbarui!")
        else:
            print("Item tidak ditemukan!")

    def check_order(self):
        """Menampilkan daftar pesanan dalam bentuk tabel rapi."""
        if not self.items:
            print("\nBelum ada item dalam transaksi.\n")
            return 0
        
        print("\n=================== DAFTAR PESANAN ===================")
        print("| No | Nama Item       | Jumlah   | Harga     | Total      |")
        print("|----|-----------------|----------|-----------|------------|")

        for i, (name, data) in enumerate(self.items.items(), start=1):
            print(
                f"| {i:<2} | {name:<16} | {data['qty']:<6} | "
                f"{data['price']:<10} | {data['total']:<11} |"
            )

        print("=========================================================\n")

        return sum(item["total"] for item in self.items.values())

    def total_price(self):
        """Menghitung total harga dan menerapkan diskon yang sesuai."""
        total_price = self.check_order()
        if total_price == 0:
            return

        if total_price > 500_000:
            discount = 0.10
        elif total_price > 300_000:
            discount = 0.08
        elif total_price > 200_000:
            discount = 0.05
        else:
            discount = 0

        final_price = total_price - (total_price * discount)

        print(f"Total belanja sebelum diskon : Rp {total_price:,.0f}")
        print(f"Diskon                       : {discount * 100:.0f}%")
        print(f"Total yang harus dibayar     : Rp {final_price:,.0f}\n")

    def reset_transaction(self):
        """Menghapus seluruh item belanja."""
        self.items.clear()
        print("Transaksi berhasil di-reset!")