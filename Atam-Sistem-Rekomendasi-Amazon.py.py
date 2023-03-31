#!/usr/bin/env python
# coding: utf-8

# # Sistem Rekomendasi Produk Dari Amazon

# ## Persiapan Library

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime,timedelta


# In[2]:


# Plotting import
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import MaxNLocator

import seaborn as sns
from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))


# ## Memproses Data

# ### Memasukkan Data

# In[3]:


from pathlib import Path
comp_dir = Path('C:/Users/Atam Rifai S/OneDrive - ITPLN/OneDrive - Komputer/Script/Machine Learning/Dicoding/Rekomendasi sistem')


# In[4]:


lectronics_data_pure=pd.read_csv(comp_dir / "Amazon_Electronics_by_Ratings.csv")
lectronics_data_pure.head(10)


# ### Memberi Nama Kolom

# In[5]:


#Menambahkan dataset dari review electronics
electronics_data=pd.read_csv(comp_dir / "Amazon_Electronics_by_Ratings.csv", dtype={'rating': 'int8'},
                             names=['userId', 'productId','rating','timestamp'], index_col=None, header=0)
#Memperlihatkan head
electronics_data.head(10)


# ### Melihat Info Data

# In[6]:


electronics_data.describe()


# In[7]:


electronics_data.info()


# In[8]:


printmd("**Jumlah dari Ratings**: {:,}".format(electronics_data.shape[0]) )
printmd("**Jenis Kolom Yang Tersedia**: {}".format( np.array2string(electronics_data.columns.values)) )
printmd("**Jumlah dari User**: {:,}".format(len(electronics_data.userId.unique()) ) )
printmd("**Jumlah dari produk**: {:,}".format(len(electronics_data.productId.unique())  ) )


# ### Mengecek Baris Kosong

# In[9]:


printmd('**Jumlah dari baris kosong**:')
pd.DataFrame(electronics_data.isnull().sum().reset_index()).rename( columns={0:"Total Kosong","index":"Kolom"}) 


# ## Persiapan Data

# ### Melihat data berdasarkan waktu dan ratingnya dijumlah

# In[10]:


data_by_date = electronics_data.copy()
data_by_date.timestamp = pd.to_datetime(electronics_data.timestamp, unit="s")#.dt.date
data_by_date = data_by_date.sort_values(by="timestamp", ascending=False).reset_index(drop=True)
printmd("**Number of Ratings each day:**")
data_by_date.groupby("timestamp")["rating"].count().tail(10).reset_index()


# ### Melihat Grafik Trends Berdasarkan Waktu dan Total Pemberian Rating

# In[11]:


data_by_date["year"]  = data_by_date.timestamp.dt.year
data_by_date["month"] = data_by_date.timestamp.dt.month
rating_by_year = data_by_date.groupby(["year","month"])["rating"].count().reset_index()
rating_by_year["date"] = pd.to_datetime(rating_by_year["year"].astype("str")  +"-"+rating_by_year["month"].astype("str") +"-1")
rating_by_year.plot(x="date", y="rating")
plt.title("Number of Rating over years")
plt.show()


# ## Membuat Model

# In[12]:


import numpy as np
import tensorflow as tf
import tensorflow_recommenders as tfrs


# In[13]:


class RankingModel(tf.keras.Model):

    def __init__(self):
        super().__init__()
        embedding_dimension = 32

        self.user_embeddings = tf.keras.Sequential([
                                    tf.keras.layers.experimental.preprocessing.StringLookup(
                                        vocabulary=unique_userIds, mask_token=None),
                                    tf.keras.layers.Embedding(len(unique_userIds)+1, embedding_dimension)
                                    ])

        self.product_embeddings = tf.keras.Sequential([
                                    tf.keras.layers.experimental.preprocessing.StringLookup(
                                        vocabulary=unique_productIds, mask_token=None),
                                    tf.keras.layers.Embedding(len(unique_productIds)+1, embedding_dimension)
                                    ])
        self.ratings = tf.keras.Sequential([
                            tf.keras.layers.Dense(256, activation="relu"),
                            tf.keras.layers.Dense(64,  activation="relu"),
                            tf.keras.layers.Dense(1)
                              ])
    def call(self, userId, productId):
        user_embeddings  = self.user_embeddings (userId)
        product_embeddings = self.product_embeddings(productId)
        return self.ratings(tf.concat([user_embeddings,product_embeddings], axis=1))

# Build a model.
class amazonModel(tfrs.models.Model):

    def __init__(self):
        super().__init__()
        self.ranking_model: tf.keras.Model = RankingModel()
        self.task: tf.keras.layers.Layer   = tfrs.tasks.Ranking(
                                                    loss    =  tf.keras.losses.MeanSquaredError(),
                                                    metrics = [tf.keras.metrics.RootMeanSquaredError()])
            

    def compute_loss(self, features, training=False):
        rating_predictions = self.ranking_model(features["userId"], features["productId"]  )

        return self.task( labels=features["rating"], predictions=rating_predictions)


# In[25]:


userIds    = recent_prod.userId.unique()
productIds = recent_prod.productId.unique()
total_ratings= len(recent_prod.index)


# In[16]:


ratings = tf.data.Dataset.from_tensor_slices( {"userId":tf.cast( recent_prod.userId.values  ,tf.string),
                                "productId":tf.cast( recent_prod.productId.values,tf.string),
                                "rating":tf.cast( recent_prod.rating.values  ,tf.int8,) } )


# In[17]:


tf.random.set_seed(42)
shuffled = ratings.shuffle(100_000, seed=42, reshuffle_each_iteration=False)

train = shuffled.take( int(total_ratings*0.8) )
test = shuffled.skip(int(total_ratings*0.8)).take(int(total_ratings*0.2))

unique_productIds = productIds
unique_userIds    = userIds


# ## Model Aktif Mempelajari Pola

# In[18]:


model = amazonModel()
model.compile(optimizer=tf.keras.optimizers.Adagrad( learning_rate=0.1 ), metrics=['accuracy'])
cached_train = train.shuffle(100_000).batch(8192).cache()
cached_test = test.batch(4096).cache()
model.fit(cached_train, epochs=20)


# In[19]:


# Evaluasi
model.evaluate(cached_test, return_dict=True)


# ## Uji Coba Prediksi

# In[24]:


print("5 Produk ID Teratas untuk user {}: ".format(userIds[123]))
for m in sorted(test_rating, key=test_rating.get, reverse=True):
    print(m.decode())


# In[ ]:




