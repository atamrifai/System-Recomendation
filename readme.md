


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

## Data Preparation
Dalam mengelola data penulis melakukan beberapa pembersihan pada data, mengubah string menjadi list hingga menyusun algoritma knn untuk clustering, detailnya :

- Tahap 1: Memasukkan data, sebelumnya tabel yang ada tidak ada nama kolomnya tampil seperti ini :

![image](https://user-images.githubusercontent.com/58683035/184104837-76c81711-80d0-4766-af53-13199e9ea0bc.png)

- Tahap 2: Dengan melihat dokumentasi sumber data, penulis melakukan rename kolom sehingga tanpak seperti ini :

![image](https://user-images.githubusercontent.com/58683035/184105009-dd72ae45-1dce-468a-bb3f-e0a2fb8d56b7.png)

- Tahap 3: Seperti yang diajarkan dalam modul, pada tahap ini penulis berusaha untuk mempelajari distribusi data dan isinya dengan melakukan sintaks berikut ini:

![image](https://user-images.githubusercontent.com/58683035/184105118-dc4c45d9-54f9-4944-a083-7188c722d677.png)

- Tahap 4: Setelah data muncul, tahap selanjutnya adalah mengecek ketersediaan isi pada kolom, karena ketika ada missing kolom ini akan menyebabkan sistem rekomendasi kurang optimal

![image](https://user-images.githubusercontent.com/58683035/184105303-671c6624-1982-475f-8906-93652379c7f8.png)

- Tahap 5: Mempelajari data dari parameter waktu dan rating, dengan begitu bisa dilihat bahwa untuk pemberian rating terbanyak itu pada tahun 2014  (gambar dibawah)

![image](https://user-images.githubusercontent.com/58683035/184105720-d8a72c44-b7f5-4626-8253-588f36295d32.png)



Pengeolahan data sampai di tahap ini, selanjutnya data yang sudah bersih ini akan diolah pada segment modelling


## Modeling
Pada tahap modelling ini penulis menggunakan algoritma KNN dengan tambahan tokenizer untuk mengidentifikasi kata kata yang sekolompok. Tidak hanya itu untuk memerbaiki kinerja dari program, penulis menambahkan stop-word supaya kata kata yang diambil dalam bahasa inggris ini bukan kata kata penghubung dasar dan kata kerja dasar, melainkan benar benar objek. Beberapa tahapan saat modelling :

- Tahap 1: Mendefinisikan ranking model merupakan library dari tensorflow untuk tiap tiap kolom Rating, UserID, dan ProdukID, dengan bantuan tensorflow

- Tahap 2: Setting untuk setiap model yang dilatih, supaya saat model pelatihan tidak terdapat duplikat yang menyebabkan memori berlebih dengan code ini :

```
userIds    = recent_prod.userId.unique()
productIds = recent_prod.productId.unique()
total_ratings= len(recent_prod.index)
```

- Tahap 3: Lakukan model training berdasarkan metriks RMSE, Loss yang sudah dituliskan pada code menjadi seperti dibawah ini. Untuk penjelasan metriks akan ada di tahap evaluation

![image](https://user-images.githubusercontent.com/58683035/184107647-8f16d788-d685-4447-91bd-ae09bf885f5a.png)


- Tahap 4: Uji coba prediksi dengan memanggil function model dengan parameter user id, sehingga menjadi :

![image](https://user-images.githubusercontent.com/58683035/184107799-ae69b6b9-388d-441e-a025-5b5df95bcba5.png)

Keterangan : untuk produk ID yang tampil 

```
B002FFG6JC
B004ABO7QI
B006YW3DI4
B0012YJQWQ
B006ZBWV0K
```

Diatas hanya berupa ID, karena pada dataset awal tidak ada penjelasan dari setiap kode dari ID tersebut.


## Evaluation
Untuk meningkatkan dari code dalam jurnal [1] sistem rekomendasi penulis menggunakan metode CNN dengan bantuan tensorflow dan tensorflow_rankings. Untuk pelatihan modelnya penulis menggunakan metriks RMSE. RMSE merupakan _(Root Means Squared Error)_ [4]. 
 
 ![image](https://user-images.githubusercontent.com/58683035/184137073-e56cc754-6793-4f55-8eb2-82bc87d5fd2f.png)


Dalam penggunaan machine learning rekomendasi sistem ini RMSE berperan untuk mencari bobot besar berdasarkan loss yang besar. Penulis menggunakan RMSE karena tidak menginginkan _outlier_ pada model. Hasil yang didapat dari RMSE cukup memuaskan ( _tahap 4 Modeling_ ). Dengan begitu, goals diawal untuk membuat rekomendasi yang sebelumnya menggunakan clustering berhasil dibuat dengan performa yang baik. Sehingga, ketika diterapkan di dalam model bisnis _e-commerce_ user tidak akan langsung meninggalkan platform _e-commerce_ dengan cepat karena muncul item yang direkomendasikan pada layar. Tetapi, user dapat melihat lihat rekomendasi dari produk yang bersangkutan. hal itu, dapat meningkatkam tingkat keramaian website. Untuk peningkatan performa kepedannya dapat mengubah arsitektur model pada bagian penambahan filtering dari CNN, dan mendapatkan hasil yang lebih efektif

## Referensi
[1] ALKHATIB, K., NAJADAT, H., HMEIDI, I. & SHATNAWI, M.K.A. 2013. Stock price prediction using k-nearest neighbor (kNN) algorithm. International Journal of Business, Humanities and Technology, 3(3), 32-44.

[2] VAINIONPÄÄ, I., & DAVIDSSON, S. 2014. Stock market prediction using the K Nearest Neighbours algorithm and a comparison with the moving average formula. 

[3] Wan Song, Liu Sun, Wei Fan, Jun Sun 2017. An Automated CNN Recommendation System for Image Classification Tasks, Conference: International Conference on Multimedia and Expo 2017

[4] T. Chai1,R. R. Draxler, 2014. Root mean square error (RMSE) or mean absolute error (MAE)? Arguments against avoiding RMSE in the literature. Copernicus Publications on behalf of the European Geosciences Union.

