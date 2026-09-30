# Pertemuan 05 Perulangan Python
Nama: Hitana Rifa Pranaja

NIM: 2225250077

Kelas: 3A

## Tujuan 
Menggunakan for and while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
### Kuis
```bash
python3 kuis/kuis2_deret_aritmetika.py
```
### Latihan
```bash
python3 latihan/01_tabel_perkalian.py
python3 latihan/02_jumlah_bilangan.py
python3 latihan/03_validasi_input.py
python3 latihan/04_hitung_genap.py
```

## Algoritma Kuis 2

1. Masukkan nilai suku pertama `a`.
2. Masukkan nilai beda `d`.
3. Masukkan banyak suku `n`.
4. Jika `n` kurang dari atau sama dengan 0, minta pengguna memasukkan `n` lagi sampai nilainya positif.
5. Siapkan `total` dengan nilai awal 0.
6. Gunakan perulangan `for` sebanyak `n` kali.
7. Hitung setiap suku dengan menggunakan nilai `a`, `d`, dan urutan suku.
8. Tampilkan setiap suku yang sudah dihitung.
9. Tambahkan setiap suku ke dalam `total`.
10. Setelah perulangan selesai, tampilkan jumlah seluruh suku.

## Hasil Pengujian

| No. | Input a | Input d | Input n | Suku yang Dihasilkan | Jumlah | Status |
|---|---:|---:|---:|---|---:|---|
| 1 | 2 | 3 | 5 | 2, 5, 8, 11, 14 | 40 | Berhasil |
| 2 | 10 | -2 | 4 | 10, 8, 6, 4 | 28 | Berhasil |
| 3 | 1.5 | 0.5 | 3 | 1.5, 2.0, 2.5 | 6.0 | Berhasil |

## Refleksi
Saat mengerjakan program untuk menyelesaikan latihan hitung bilangan genap, saya menemukan kesalahan dimana outputnya justru menjadi jumlah dari bilangan genap yang ada di rentang angka n yang di input. Hal itu terjadi karena kesalahan akumulator digunakan untuk menjumlahkan bilangan genap dan bukan menghitung banyaknya bilangan genap. Solusinya adalah mengganti `jumlah_genap += i` menjadi `jumlah_genap += 1`, sehingga setiap bilangan genap yang ditemukan dihitung satu kali.

## Sumber 
- Materi Pertemuan 05
- ChatGPT ai
