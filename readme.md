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

![image](https://user-images.githubusercontent.com/58683035/184065823-3f5eed4d-5ad0-4d36-8058-d192d67dd812.png)

- Tahap 2 : Memahami persebaran isi data karena kebetulan object yang kita ingin analisis string, maka deskripsnua sebagai berikut

![image](https://user-images.githubusercontent.com/58683035/184065986-60b076f3-896f-4eae-9af4-0c6e073fa0d5.png)

- Tahap 3 : Melakukan pembersihan data, pada data-data yang null, sehingga tidak ada data null dengan code 

```
amazon_desc = product_descriptions.dropna()
```

- Tahap 4 : Melakukan sampeling data pada 2000 data, supaya tidak membenani kinerja mesin saat tokenizer nantinya dengan code

```
product_descriptions1 = product_descriptions.head(2000)
```

Pengeolahan data sampai di tahap ini, selanjutnya data yang sudah bersih ini akan diolah pada segment modelling


## Modeling
Pada tahap modelling ini penulis menggunakan algoritma KNN dengan tambahan tokenizer untuk mengidentifikasi kata kata yang sekolompok. Tidak hanya itu untuk memerbaiki kinerja dari program, penulis menambahkan stop-word supaya kata kata yang diambil dalam bahasa inggris ini bukan kata kata penghubung dasar dan kata kerja dasar, melainkan benar benar objek. Beberapa tahapan saat modelling :

- Tahap 1: Melakukan tokenizer dan stop word supaya kata kata di saring untuk mendapatkan kata kata yang objek saja, dengan code :

```
vectorizer = TfidfVectorizer(stop_words='english')
X1 = vectorizer.fit_transform(product_descriptions1["product_description"])
X1
```

- Tahap 2: Menganalisa hasil persebaran kata kata ketika sudah dilakukan clustering. _Fitting_ dengan KNN sehingga hasilnya seperti berikut :

![image](https://user-images.githubusercontent.com/58683035/184066553-ed90791d-50e0-4035-90bf-4351e076e3e3.png)

- Tahap 3: Menampilkan hasil clustering dari deskripsi produk yang sejenis : 

![image](https://user-images.githubusercontent.com/58683035/184066625-4cb966d9-41a0-42ce-ae61-2c26764b8cec.png)

- Tahap 4: Membangun function untuk menampilkan prediksi rekomendasi dengan code :

```
def show_recommendations(product):
    #print("Cluster ID:")
    Y = vectorizer.transform([product])
    prediction = model.predict(Y)
    #print(prediction)
    print_cluster(prediction[0])
```



## Evaluation
Ketika menjalankan sistem rekomendasi menggunakan metode clustering metrik dapat disususn dengan fungsi tokenizer, sehingga data yang tadinya perkalimat akan dipecah pecah menjadi perkata dan menghilangkan kata kata yang tidak mengandung unsur objek. Kemudian hasil dari tokenizer tadi dimasukkan kendalam KNN clustering untuk machinelearning membangun kesamaan antara kata kata teresbut. Sehingga klustering dapat berjalan dengan lancar dengan bantuan Tokenizer dan Stop-words

**---Ini adalah bagian akhir laporan---**

## Referensi
[1] ALKHATIB, K., NAJADAT, H., HMEIDI, I. & SHATNAWI, M.K.A. 2013. Stock price prediction using k-nearest neighbor (kNN) algorithm. International Journal of Business, Humanities and Technology, 3(3), 32-44.

[2] VAINIONPÄÄ, I., & DAVIDSSON, S. 2014. Stock market prediction using the K Nearest Neighbours algorithm and a comparison with the moving average formula. 

