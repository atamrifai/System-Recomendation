# Laporan Proyek Machine Learning - Atam Rifa'i Sujiwanto

## Project Overview
Konsep sistem rekomendasi telah digunakan oleh berbagai bisnis online seperti amazon.com dan ebay.com sebagai alat bisnis. Sistem rekomendasi dilaporkan telah meningkatkan penjualan produk dan membangun loyalitas pembeli [1]. Dengan begitu, ketika kita melakukan pencarian pada suatu website ini memberikan sistem rekomendasi yang tepat sasaran, seperti halnya pada penelitian sebelumnya [2]. Namun, pada kali ini penulis menggunakan algoritma CNN dengan menggunakan tensorflow dengan evaluasi model _Loss_, _accuracy_ dan _MSE_


## Business Understanding

Pelanggan yang mengunjungi website tentu ingin pengalaman yang terbaik. Hal tersebut memicu sistem _e-commerce_ untuk terus beradaptasi dan terus menyesuaikan keinginan pelanggan. Ketika pelanggan melakukan pencarian tanpa adanya rekomendasi lainnya, pelanggan akan cenderung langsung meninggalkan _e-commerce_ dan ini tentu mengancap roda bisnis yang terus berputar

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah:
- Pelanggan yang meninggalkan website setelah barang yang diinginkan terpenuhi
- Tingkat pengunjung yang rendah karena tidak adanya sistem rekomendasi
- Kurang efektifnya tingkat rekomendasi secara Clustering

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Dapat merekomendasikan barang lain sehingga pelanggan tidak cepat cepat untuk pergi dari website kita
- Meningkatkan tingkat pengunjung website dengan menampilkan rekomendasi sehingga pelanggan tetap betah di dalma website
- Menanamkan algoritma CNN untuk mencoba mengevaluasi model dengan Metriks MSE dan LOSS sehingga lebih cepat

## Data Understanding
Data yang didapatkan berasal dari deskripsi produk _amazon.com_ dalam kata kunci berbahasa inggris. yang terdiri dari 2 x 124427 data dengan masing memiliki deskripsi dari setiap produk yang ditautkan dengan ID produk. data dapat diunduh di [sini](https://sellercentral-europe.amazon.com/forums/t/csv-product-download/358218) beberapa variable dalam data yang saya gunakan :

Variabel-variabel pada Deskripsi data dataset adalah sebagai berikut:
- userId    = ID user yang telah melakukan pembelian pada produk di website
- productId = ID produk yang telah dibeli oleh user
- rating    = Rating dari produk yang dinilai oleh user pada produk
- timestamp = Tanggal terjadinya transaksi


