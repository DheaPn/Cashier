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

  ![image](https://github.com/user-attachments/assets/94d11c33-6b86-4e5f-88b2-4268e7361519)

- update_item_name()

  ![image](https://github.com/user-attachments/assets/0fbb9ce0-5a57-41fc-9dd1-4f2556f2f596)

- update_item_qty()

  ![image](https://github.com/user-attachments/assets/b04ecb1c-c07a-49e2-bf36-f3dd9bf996e1)

- update_item_price()

  ![image](https://github.com/user-attachments/assets/eac9a901-9105-4f17-b8c1-76bfb0a2de2d)

- delete_item()

  ![image](https://github.com/user-attachments/assets/25627861-05be-4e9b-97d6-64945351c6e5)

- reset_transaction()

  ![image](https://github.com/user-attachments/assets/74bfd0c8-6d11-486b-b05c-5416ca8bfc16)

- check_order()

  ![image](https://github.com/user-attachments/assets/a0540068-1ac3-4b0d-a138-af23f0d3d9ee)

- total_price()

  ![image](https://github.com/user-attachments/assets/d6a821d4-9a9b-48bb-a75e-1b6f46a33ac4)

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

![Image](https://github.com/user-attachments/assets/61d316f2-03dd-4142-bc52-d7610ecfefa3)

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Buka terminal
3. Masuk folder project
4. Jalankan:
   ![image](https://github.com/user-attachments/assets/6b3b8b21-8c2b-4e4d-878a-ef95d825a863)

   Menu program akan muncul:
   ![image](https://github.com/user-attachments/assets/0742fe50-b141-4f18-a0d6-33cbe0cacf91)

## Hasil Test-Case Program

### 1. Input 1 – Tambah Item

![image](https://github.com/user-attachments/assets/4efb712c-f962-4861-91cf-60b7c6f70732)

### 2. Input 4 – Cek Pesanan

![image](https://github.com/user-attachments/assets/4a62b64a-1da3-4d7e-a4a2-9138474ff30a)

### 3. Input 2 – Hapus Item

![image](https://github.com/user-attachments/assets/8ccf7d62-0354-4d64-b7ba-21034a19ac0b)

### 4. Input 3 – Update Nama/Jumlah/Harga Item

![image](https://github.com/user-attachments/assets/e153955f-3af5-43bf-b132-d72be1a0f925)
![image](https://github.com/user-attachments/assets/52c2b678-bfc1-47a4-a8af-202cba89a3c9)
![image](https://github.com/user-attachments/assets/5c4f3818-13d4-4fa4-8ff5-22a4024e9d4c)

### Input 6 - Reset Transaksi

![image](https://github.com/user-attachments/assets/f1c50156-9c79-463e-82fa-197326037abf)
![image](https://github.com/user-attachments/assets/6c039769-2aee-46a1-942f-d2778e734f87)

### 5. Input 1 – Tambah Item Kembali

![image](https://github.com/user-attachments/assets/564dce4f-ccec-44ce-9220-18ab411360b6)
![image](https://github.com/user-attachments/assets/cdd8045f-66d6-4fd7-8a12-2ebc88422dbc)

### 6. Input 5 – Hitung Total Harga

![image](https://github.com/user-attachments/assets/10d4ae7f-58bb-4fe3-b1d3-9b0f534d1744)

## Conclusion / Future Work (Versi Singkat)

Program Self-Service Cashier dapat dijalankan melalui terminal dan telah memenuhi fungsi utama sebagai sistem kasir sederhana.

Ke depannya, program ini dapat dikembangkan lebih jauh dengan beberapa peningkatan, seperti:

- Penyimpanan data transaksi, agar data tidak hilang setelah program ditutup.
- Interface yang lebih interaktif, misalnya dengan menambahkan GUI agar lebih mudah digunakan dan user-friendly.
