# 🛒 Program Kasir Sederhana

Program ini merupakan aplikasi kasir sederhana berbasis terminal yang dapat digunakan untuk mengelola transaksi belanja.  
Pengguna dapat menambah item, menghapus item, memperbarui item, menampilkan daftar belanja, hingga menghitung total harga.

Program terdiri dari dua file utama:

- `main.py` — berisi menu utama dan interaksi dengan pengguna.
- `transaction.py` — berisi class `Transaction` yang mengelola logika dan data transaksi.

## Latar Belakang

Andi ingin membangun sistem kasir self-service yang bisa digunakan oleh customer tanpa bantuan kasir. Dengan sistem ini:

- Customer dapat input nama item, jumlah, dan harga.
- Customer dapat mengubah item jika salah input.
- Customer dapat menghapus item tertentu atau menghapus semua transaksi.
- Customer dapat mengecek apakah order valid.
- Customer dapat menghitung total harga beserta diskon otomatis.

Andi meminta programmer untuk membuatkan fitur-fitur tersebut agar sistem self-service dapat berjalan lancar tanpa error input.

## Requirements / Objectives

Berikut tujuan pembuatan program:

✔️ Membuat sistem transaksi menggunakan OOP:

- Class utama: Transaction
- Menyimpan order dalam bentuk dictionary

✔️ Fitur yang harus dibuat:

- add_item()

  ![image](https://github.com/user-attachments/assets/92350623-3bc7-4d67-ac40-82b01e8903b7)

- update_item_name()

  ![image](https://github.com/user-attachments/assets/346e7099-bf3d-4173-9723-2857180da408)

- update_item_qty()

  ![image](https://github.com/user-attachments/assets/aca599af-9fac-4b06-86ff-eca8e72b9a9e)

- update_item_price()

  ![image](https://github.com/user-attachments/assets/0e67ad7c-6bcf-4a53-8292-e87a47449c89)

- delete_item()

  ![image](https://github.com/user-attachments/assets/c0fc5154-eb98-4c87-98b6-7001bc177c7c)

- reset_transaction()

  ![image](https://github.com/user-attachments/assets/e5118437-e57d-492f-a1a2-a38857ef46bf)

- check_order()

  ![image](https://github.com/user-attachments/assets/2f4104ee-9ef6-4481-b72f-7c21084fe5ba)

- total_price()

  ![image](https://github.com/user-attachments/assets/ebbf674f-d9bd-42a6-baf3-c46dc35edf7e)

✔️ Aturan Diskon:

- Total > 200.000 → diskon 5%
- Total > 300.000 → diskon 8%
- Total > 500.000 → diskon 10%

✔️ Clean Code:

- Modular (transaction.py dan main.py)
- Docstring
- Error handling sederhana
- Tanpa database (sesuai requirement)

## Penjelasan Program

Program ini terdiri dari dua file utama:

## 1. main.py

File utama yang dijalankan oleh user:

Berisi menu interaktif:

- Tambah item belanjaan
- Hapus item
- Reset transaksi
- Cek pesanan
- Hitung total harga
- Update nama item
- Update jumlah item
- Update harga item
- Keluar

main.py akan memanggil class Transaction dari file transaction.py.

## 2. transaction.py

Berisi class Transaction yang menangani seluruh logika transaksi. Method-method utama:

- add_item() → Menambah item: nama, jumlah, harga
- delete_item() → Menghapus item berdasarkan nama
- update_item_name() → Mengubah nama item
- update_item_qty() → Mengubah jumlah item
- update_item_price() → Mengubah harga item
- check_order() → Menampilkan tabel keranjang belanja
- total_price() → Menghitung total + diskon jika memenuhi syarat
- reset_transaction() → Menghapus semua item belanja

## Flowchart Program

![Image](https://github.com/user-attachments/assets/fe3a4543-cfd5-4fb8-831d-d38f4c7419eb)

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Buka terminal
3. Masuk folder project
4. Jalankan:
   ![image](https://github.com/user-attachments/assets/26c9c933-0f8b-4ade-aa54-0fcdb27cd4ed)

   Menu program akan muncul:
   ![image](https://github.com/user-attachments/assets/412302a7-edd8-4049-a6ea-61c752b438bb)

## Hasil Test-Case Program

### 1. Input 1 – Tambah Item

![image](https://github.com/user-attachments/assets/144fc9b9-b6fa-4069-bfd4-edb70826ee39)

### 2. Input 4 – Cek Pesanan

![image](https://github.com/user-attachments/assets/ddb0fa14-1374-4a58-a0b4-f06dd2d6e0f1)

### 3. Input 2 – Hapus Item

![image](https://github.com/user-attachments/assets/a73d876a-f963-47cc-9159-8d819426abfa)

### 4. Input 3 – Update Nama/Jumlah/Harga Item

![image](https://github.com/user-attachments/assets/c4557cfd-a337-4b45-b1bf-9f5586d5a293)
![image](https://github.com/user-attachments/assets/efaef35b-4e11-4582-9be8-ed134543b984)
![image](https://github.com/user-attachments/assets/1b3e1e8f-00aa-4cfe-ba1a-06d74ca23605)

### Input 6 - Reset Transaksi

![image](https://github.com/user-attachments/assets/a9b7b629-128f-4349-b5e8-ec3a2b4101c5)
![image](https://github.com/user-attachments/assets/533b49b2-1b49-479c-899c-47500724584a)

### 5. Input 1 – Tambah Item Kembali

![image](https://github.com/user-attachments/assets/bdcae12c-4ebe-4276-8549-6d85f956639a)
![image](https://github.com/user-attachments/assets/a923ebcd-b5a9-46bb-892c-2f0083e9c4b6)

### 6. Input 5 – Hitung Total Harga

![image](https://github.com/user-attachments/assets/14b9af07-b562-4bdd-b010-99d0009901fc)

## Conclusion / Future Work (Versi Singkat)

Program Self-Service Cashier dapat dijalankan melalui terminal dan telah memenuhi fungsi utama sebagai sistem kasir sederhana.

Ke depannya, program ini dapat dikembangkan lebih jauh dengan beberapa peningkatan, seperti:

- Penyimpanan data transaksi, agar data tidak hilang setelah program ditutup.
- Interface yang lebih interaktif, misalnya dengan menambahkan GUI agar lebih mudah digunakan dan user-friendly.
