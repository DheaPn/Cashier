from transaction import Transaction

def main():
    tr = Transaction()

    while True:
        print("""
=========== SELF-SERVICE CASHIER ===========
1. Tambah Item
2. Hapus Item
3. Update Nama/Jumlah/Harga Item
4. Cek Pesanan
5. Hitung Total Harga
6. Reset Transaksi
0. Keluar
============================================
        """)

        pilihan = input("Pilih menu: ")

        # tambah item
        if pilihan == "1":
            nama = input("Nama item: ")
            qty = int(input("Jumlah item: "))
            harga = int(input("Harga item: "))
            tr.add_item(nama, qty, harga)

        # hapus item
        elif pilihan == "2":
            nama = input("Nama item yang ingin dihapus: ")
            tr.delete_item(nama)

        # update nama/qty/harga item
        elif pilihan == "3":
            print("""
            --- Update Item ---
            1. Update Nama
            2. Update Jumlah
            3. Update Harga
            """)
            up = input("Pilih update: ")

            if up == "1":
                old = input("Nama item lama: ")
                new = input("Nama item baru: ")
                tr.update_item_name(old, new)

            elif up == "2":
                name = input("Nama item: ")
                new_qty = int(input("Jumlah baru: "))
                tr.update_item_qty(name, new_qty)

            elif up == "3":
                name = input("Nama item: ")
                new_price = int(input("Harga baru: "))
                tr.update_item_price(name, new_price)

        elif pilihan == "4":
            tr.check_order()

        elif pilihan == "5":
            tr.total_price()

        elif pilihan == "6":
            tr.reset_transaction()

        elif pilihan == "0":
            print("Terima kasih telah berbelanja!")
            break

        else:
            print("Input tidak valid! Coba lagi.\n")

if __name__ == "__main__":
    main()