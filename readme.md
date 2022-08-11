# Laporan Proyek Machine Learning - Atam Rifa'i Sujiwanto

## Project Overview
Konsep sistem rekomendasi telah digunakan oleh berbagai bisnis online seperti amazon.com dan ebay.com sebagai alat bisnis. Sistem rekomendasi dilaporkan telah meningkatkan penjualan produk dan membangun loyalitas pembeli [1]. Dengan begitu, ketika kita melakukan pencarian pada suatu website ini memberikan sistem rekomendasi yang tepat sasaran, seperti halnya pada penelitian sebelumnya [2]. Dengan menggunakan algoritma KNN _clustering_ penulis ingin menciptakan sistem rekomendasi yang dapat merekomendasikan kelompok-kelompok dari hasil pencarian tersebut


## Business Understanding

Pelanggan yang mengunjungi website tentu ingin pengalaman yang terbaik. Hal tersebut memicu sistem _e-commerce_ untuk terus beradaptasi dan terus menyesuaikan keinginan pelanggan. Ketika pelanggan melakukan pencarian tanpa adanya rekomendasi lainnya, pelanggan akan cenderung langsung meninggalkan _e-commerce_ dan ini tentu mengancap roda bisnis yang terus berputar

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah:
- Pelanggan yang meninggalkan website setelah barang yang diinginkan terpenuhi
- Tingkat pengunjung yang rendah karena tidak adanya sistem rekomendasi
- Kurang efektifnya tingkat rekomendasi secara manual

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Dapat merekomendasikan barang lain sehingga pelanggan tidak cepat cepat untuk pergi dari website kita
- Meningkatkan tingkat pengunjung website dengan menampilkan rekomendasi sehingga pelanggan tetap betah di dalma website
- Menanamkan algoritma _clustering_ pada sistem rekomendasi sehingga sistem jauh lebih efektif

## Data Understanding
Data yang didapatkan berasal dari deskripsi produk _amazon.com_ dalam kata kunci berbahasa inggris. yang terdiri dari 2 x 124427 data dengan masing memiliki deskripsi dari setiap produk yang ditautkan dengan ID produk. data dapat diunduh di [sini](https://sellercentral-europe.amazon.com/forums/t/csv-product-download/358218) beberapa variable dalam data yang saya gunakan :

Variabel-variabel pada Deskripsi data dataset adalah sebagai berikut:
- product_uid	= ID dari setiap produk deskripsi
- product_description = deskripsi lengkap dari penjabaran id

Menggunakan pemahaaman pada deskripsi pasti memiliki keterkaitan sehingga penulis menggunakan tokenizer nantinya yang akan di jelaskan pada data preparation.

## Data Preparation
Dalam mengelola data penulis melakukan beberapa pembersihan pada data, mengubah string menjadi list hingga menyusun algoritma knn untuk clustering, detailnya :

- Tahap 1 : Data akan dijadikan object python terlebih dahulu dengan bantuan pandas 


## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

## Referensi
[1] ALKHATIB, K., NAJADAT, H., HMEIDI, I. & SHATNAWI, M.K.A. 2013. Stock price prediction using k-nearest neighbor (kNN) algorithm. International Journal of Business, Humanities and Technology, 3(3), 32-44.
[2] VAINIONPÄÄ, I., & DAVIDSSON, S. 2014. Stock market prediction using the K Nearest Neighbours algorithm and a comparison with the moving average formula. 
_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
