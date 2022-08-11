#!/usr/bin/env python
# coding: utf-8

# # Sistem Rekomendasi

# Cara kerja sistem rekomendasi ini adalah merekomendasikan barang barang lain berdasarkan disrkipsi produk yang ada, jadi ibaratkan kita berbelanja di toko atamstore, kemudian mencari dengan kata kunci **'water'** maka benda benda lain yang berhubungan dengan **'water'** akan muncul berdasarkan _clustering_

# ## _Import Library_

# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import pandas as pd
import matplotlib.pyplot as plt


# ## Persiapan Data

# ### Menampilkan Data

# In[21]:


amazon_desc = pd.read_csv('C:/Users/Atam Rifai S/OneDrive - ITPLN/OneDrive - Komputer/Script/Machine Learning/Dicoding/Rekomendasi sistem/product_descriptions.csv')
amazon_desc


# ### Memahami Isi Data

# In[22]:


amazon_desc.describe()


# ### Membersihkan Data

# In[24]:


amazon_desc = product_descriptions.dropna()
product_descriptions.head()


# In[5]:


product_descriptions1 = product_descriptions.head(2000)
# product_descriptions1.iloc[:,1]

product_descriptions1["product_description"].head(50)


# ## Menyusun Algoritma Sistem Rekomendasi

# ### Mengubah Kata Menjadi Vector Berdasarkan Kata Kunci

# In[6]:


vectorizer = TfidfVectorizer(stop_words='english')
X1 = vectorizer.fit_transform(product_descriptions1["product_description"])
X1


# ### Membuat Klustering Pada Setiap Kata Kunci

# In[7]:


# Fitting K-Means to the dataset

X=X1

kmeans = KMeans(n_clusters = 10, init = 'k-means++')
y_kmeans = kmeans.fit_predict(X)
plt.plot(y_kmeans, ".")
plt.show()


# In[8]:


def print_cluster(i):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print


# In[9]:


# # Optimal clusters is 

true_k = 10

model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X1)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print_cluster(i)


# ### Membuat Fungsi Untuk Menjalankan Prediksi

# In[10]:


def show_recommendations(product):
    #print("Cluster ID:")
    Y = vectorizer.transform([product])
    prediction = model.predict(Y)
    #print(prediction)
    print_cluster(prediction[0])


# ## Menjalankan Prediksi

# In[14]:


show_recommendations("water")


# In[19]:


show_recommendations("paint")


# ## Kesimpulan

# Sistem rekomendasi dapat berjalan **dengan baik** dengan mengklasifikasi dan _cluster_ dari setiap kata kunci menggunakan algoritma **K-Means**. Dengan begini, ketika kita ingin mencari satu kata kunci maka sistem akan memberikan rekomendasi kata kunci lain. _Ini berguna pada sistem e-commerce, supaya pembeli terus melakukan pembelian_
