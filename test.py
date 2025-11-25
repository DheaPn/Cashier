"""
Script contoh modular self-service cashier
File:
- main.py → program utama
- transaction.py → modul berisi class Transaction

Keuntungan modular:
✔ Kode lebih rapi
✔ Mudah diuji (testing)
✔ Lebih mudah dikembangkan (scalable)
✔ Bisa dipisah menjadi beberapa feature
"""

from transaction import Transaction

def jalankan_cashier():
    kasir = Transaction()

    kasir.add_item("Beras", 2, 55000)
    kasir.add_item("Minyak Goreng", 1, 18000)

    kasir.check_order()
    kasir.total_price()

if __name__ == "__main__":
    jalankan_cashier()