# -*- coding: utf-8 -*-
"""E-Commerce Public Analysis

# Proyek Analisis Data: E-Commerce Public Dataset
- **Nama:** Bernardinus Rico Dewanto
- **Email:** dewantobernardinus@gmail.com
- **ID Dicoding:** bernardinus_rico

# Overview

E-commerce adalah proses membeli dan menjual barang atau jasa melalui internet. Ini mencakup berbagai aktivitas yang terjadi secara online, termasuk:
1. B2C (Business-to-Consumer):
Model ini melibatkan transaksi antara perusahaan dan konsumen. Contoh yang paling umum adalah toko online seperti Amazon, eBay, atau Tokopedia.
2. B2B (Business-to-Business):
Dalam model ini, transaksi dilakukan antara dua bisnis. Misalnya, perusahaan yang menjual produk atau jasa kepada perusahaan lain, seperti pemasok bahan baku.
3. C2C (Consumer-to-Consumer):
Model ini melibatkan transaksi antara konsumen, sering kali melalui platform yang memfasilitasi perdagangan, seperti OLX atau marketplace lainnya.
4. C2B (Consumer-to-Business):
Dalam model ini, konsumen menawarkan produk atau jasa kepada perusahaan. Contoh termasuk freelancer yang menawarkan layanan mereka di platform seperti Upwork.

Fitur E-commerce :
- Website atau Platform Online.
- Pembayaran Digital
- Logistik dan Pengiriman.
- Layanan Pelanggan melalui chat, email, atau telepon.

Manfaat E-commerce
- Akses Global.
- Pembeli dapat berbelanja kapan saja dan di mana saja tanpa harus mengunjungi toko fisik.
- Beragam Pilihan.

### Permasalahan
Pada dataset e-commerce ini, dataset memiliki beberapa bagian yang terdiri dari data customers, geolocation, order_items, order_payments, order_review, orders, product_category, products, users.

Dalam konsistensi perusahaan untuk memberikan pelayanan yang terbaik kepada user/pelanggan, **perusahaan akan terus berinovasi dengan meningkatkan pelayanan** pada website dan memperkenalkan fitur-fitur baru yang memudahkan navigasi serta interaksi. Selain itu, perusahaan juga akan fokus pada personalisasi pengalaman pengguna dengan memberikan rekomendasi produk yang relevan berdasarkan riwayat pembelian dan preferensi mereka.  Dengan demikian, masyarakat pengguna E-commerce akan lebih nyaman dalam bertransaksi.

Untuk menjawab permasalahan tersebut saya akan memberikan referensi sebagai berikut :
1. Produk apa yang paling banyak dan sedikit terjual?
2. Wilayah yang paling sering melakukan transaksi
3. Bagaimana tingkatan review yang diberikan oleh pelanggan ke suatu produk?

### stakeholder
E-Commerce yang terletak di Brazil

# Import Library
"""

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib
import matplotlib.image as mpimg
from scipy import stats

"""# Data Wrangling

### Gathering Data
"""

customers = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\customers.csv")
geolocation = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\geolocation.csv")
items = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\order_items.csv")
payments = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\order_payments.csv")
reviews = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\order_reviews.csv")
orders = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\orders.csv", encoding='utf-8')
category = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\product_category_name_translation.csv", encoding='utf-8')
products = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\products.csv", encoding='utf-8')
sellers = pd.read_csv(r"C:\Users\Anonymus\Documents\E-commerce\data\sellers.csv", encoding='utf-8')

data = {'orders': orders,
        'items': items,
        'products': products,
        'payments': payments,
        'reviews': reviews,
        'customers': customers,
        'sellers': sellers,
        'geo': geolocation,
        'category': category}
print('Preview orders')
data['orders'].head()

print('Preview items')
data['items'].head()

print('Preview products \n')
data['products'].head()

print('Preview reviews')
data['reviews'].head()

print('Preview sellers')
data['sellers'].head()

print('Preview customers')
data['customers'].head()

print('Preview geolocation \n')
data['geo'].head()

print('Preview category \n')
data['category'].head()

print('Preview payments \n')
data['payments'].head()

"""### Assesing Data

#### Cek data types
"""

data = {'orders': orders,
        'items': items,
        'products': products,
        'payments': payments,
        'reviews': reviews,
        'customers': customers,
        'sellers': sellers,
        'geo': geolocation,
        'category': category}

for df_name, df in data.items():
    print(df_name, '\n', df.info(), '\n')

"""#### cek missing value"""

# Initialize a dictionary to store null value counts for each DataFrame
null_counts = {}

# Calculate and store the null value counts for each DataFrame
data = {'orders': orders,
        'items': items,
        'products': products,
        'payments': payments,
        'reviews': reviews,
        'customers': customers,
        'sellers': sellers,
        'geo': geolocation,
        'category': category}

for name, df in data.items():
    # Memeriksa kolom yang memiliki nilai hilang dan jumlahnya
    missing_values = df.isnull().sum()

    # Memfilter hanya kolom yang memiliki nilai hilang
    missing_columns = missing_values[missing_values > 0]

    if not missing_columns.empty:
        # Mencetak nama Dataset dan kolom dengan jumlah nilai hilang
        print(f"Dataset '{name}' memiliki missing value pada kolom:")
        print(missing_columns)
        print("-" * 50)

# cek missing value (cara 2)
print('customers \n', customers.isnull().sum())
print('\n geolocation \n', geolocation.isnull().sum())
print('\n items \n', items.isnull().sum())
print('\n payments \n', payments.isnull().sum())
print('\n reviews \n', reviews.isnull().sum())
print('\n orders \n', orders.isnull().sum())
print('\n category \n', category.isnull().sum())
print('\n products \n', products.isnull().sum())
print('\n sellers \n', sellers.isnull().sum())

"""#### cek data duplicate"""

print('customers \n', customers.duplicated().sum())
print('\n geolocation \n', geolocation.duplicated().sum())
print('\n items \n', items.duplicated().sum())
print('\n payments \n', payments.duplicated().sum())
print('\n reviews \n', reviews.duplicated().sum())
print('\n orders \n', orders.duplicated().sum())
print('\n category \n', category.duplicated().sum())
print('\n products \n', products.duplicated().sum())
print('\n sellers \n', sellers.duplicated().sum())

"""### Data Cleaning

#### handle data duplicate
"""

data['geo'].head()

data['geo'].value_counts().duplicated()

# remove duplicate data
data['geo'].drop_duplicates(inplace=True)

data['geo'].duplicated().sum()

"""### handle missing value

Missing value terdapat pada dataset 'reviews', 'products', dan 'orders'

#### 'orders'
"""

# Memilih orders yang hanya delivered
print(data['orders']['order_status'].value_counts())

# Hitung jumlah pesanan yang berstatus 'delivered'
delivered_orders = data['orders'].order_status.value_counts()['delivered']

# Hitung persentase pesanan yang 'delivered'
delivered_percentage = round((delivered_orders / len(data['orders'])) * 100, 2)

# Tampilkan hasil dengan f-string
print(f'Taking only delivered orders we still get {delivered_percentage}% of data.')

# Pertama, ambil semua 'order_id' di mana status pesanan tidak 'delivered'
delivered = data['orders']['order_id'][data['orders']['order_status'] != 'delivered'].values

# filter setiap dataframe lain di mana 'order_id' adalah foreign
for key, dataframe in data.items():
    # Periksa apakah kolom 'order_id' ada di dataframe tersebut
    if 'order_id' in dataframe.columns:
        # Hapus baris yang 'order_id'-nya ada di daftar 'delivered'
        rows_to_drop = dataframe['order_id'].isin(delivered)
        dataframe.drop(dataframe[rows_to_drop].index, inplace=True)

# Memeriksa nilai NaN di setiap dataset
for dataset_name, dataset in data.items():
    for column in dataset.columns:
        # Jika kolom memiliki nilai NaN, cetak nama kolom dan persentase NaN
        nan_count = dataset[column].isnull().sum()
        if nan_count > 0:
            nan_percentage = (nan_count / len(dataset)) * 100
            print(f'{column} (%): {nan_percentage:.2f}')

# Tangani NaN di data orders
# Perhatikan bahwa NaN dalam daftar orders tidak terlalu banyak (setelah diambil hanya yang delivered sebelumnya)
# yang penting adalah 'order_delivered_customer_date'.
missing_delivery_dates = data['orders'].order_delivered_customer_date.isnull().sum()

# Tampilkan jumlah pesanan yang tidak memiliki tanggal pengiriman
print(f'There are only {missing_delivery_dates} orders that are missing delivery dates.')

# Kita bisa menghapusnya dengan cara yang sama seperti sebelumnya
# Pertama, ambil semua 'order_id' yang tidak memiliki 'order_delivered_customer_date'
null_deliveries = data['orders']['order_id'][data['orders']['order_delivered_customer_date'].isnull()].values

# Sekarang filter setiap dataframe lain di mana 'order_id' adalah kunci asing
for dataset_name, dataframe in data.items():
    # Periksa apakah kolom 'order_id' ada di dataframe tersebut
    if 'order_id' in dataframe.columns:
        # Hapus baris di mana 'order_id'-nya ada dalam daftar 'null_deliveries'
        rows_to_drop = dataframe['order_id'].isin(null_deliveries)
        dataframe.drop(dataframe[rows_to_drop].index, inplace=True)

# Saya lebih tertarik pada apakah pesanan dikirim tepat waktu daripada tanggal pengirimannya
data['orders']['delivered_on_time'] = np.where(
    data['orders']['order_delivered_customer_date'] < data['orders']['order_estimated_delivery_date'],
    'On Time',
    'Late')

#fillna
data['orders']['order_approved_at'].fillna(value='0', inplace=True)

"""#### 'reviews'"""

# Tampilkan nama kolom di dataframe reviews
print('Review columns:', data['reviews'].columns.values)

# Kolom review_comment_title memiliki 88% nilai NaN, jadi saya akan menghapusnya.
# Nilai NaN untuk data review berarti data tersebut memang tidak ada.

# Kolom yang akan dihapus
review_drop_cols = ['review_comment_title']
data['reviews'].drop(columns=review_drop_cols, inplace=True)

data['reviews'].isnull().sum()

# Mungkin jika kita sedang membahas sentiment classifier kita akan fokus ke data ini.
# Namun, disini saya tidak terlalu tertarik dengan comment.
# dari yang saya liat, Review_comment_mesaage NaN kalau seseorang tidak komentar.
# saya tidak ingin menghapusnya, jadi saya isi review_comment_message yang Nan dengan 0, dan yang leave komentar dengan 1
data['reviews']['review_comment_message'] = np.where(data['reviews']['review_comment_message'].isnull(), 0, 1)

"""#### 'products'"""

print('Product cols: ' , data['products'].columns.values)

products.columns

"""product_weight_g                2
product_length_cm               2
product_height_cm               2
product_width_cm   
"""

# saya tidak bisa memikirkan yang harus dilakukan terhadap kolom missing di produc
product_drop_cols = ['product_name_lenght',
                     'product_description_lenght',
                     'product_weight_g',
                     'product_length_cm',
                     'product_height_cm',
                     'product_width_cm']

data['products'].drop(product_drop_cols, axis= 1, inplace= True)

#fillna dilakukan.
# setelah melihat di dataset 'products' yang cukup banyak rownya, saya pikir aman untukk fillna
# products_category_name dengan outro dan
# product_photos_qty dengan 0. product_photos_qty tidak mungkin bernilai 0
data['products']['product_category_name'].fillna(value='outro', inplace=True)
data['products']['product_photos_qty'].fillna(value=0, inplace=True)

print('\n reviews \n', reviews.isnull().sum())
print('\n orders \n', orders.isnull().sum())
print('\n products \n', products.isnull().sum())

"""# Exploratory Data Analysis (EDA)"""

# Memeriksa apakah setiap DataFrame memiliki kolom 'order_id'
for name, df in data.items():
    if 'order_id' in df.columns:
        print(f"{name} memiliki kolom 'order_id'")
    else:
        print("")

# Memeriksa apakah setiap DataFrame memiliki kolom 'seller_id'
for name, df in data.items():
    if 'seller_id' in df.columns:
        print(f"{name} memiliki kolom 'seller_id'")
    else:
        print("")

"""### Explore customer"""

data['customers'].groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)

"""customer_id (jumlah akun) paling banyak terletak di Sao Paolo dengan jumlah 15540"""

data['customers'].groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False)

#menghitung berapa banyak jumlah city di dalam suatu state

state_city_counts = data['customers'].groupby('customer_state')['customer_city'].nunique().reset_index(name='City Count')
# Menampilkan hasil
print(state_city_counts)

"""### Explore Orders"""

data['orders'].columns

# menghitung persebaran (waktu lama)
# Mengubah kolom date menjadi tipe datetime
data['orders']['order_delivered_customer_date'] = pd.to_datetime(data['orders']['order_delivered_customer_date'], errors='coerce')
data['orders']['order_delivered_carrier_date'] = pd.to_datetime(data['orders']['order_delivered_carrier_date'], errors='coerce')

delivery_time = orders["order_delivered_customer_date"] - orders["order_delivered_carrier_date"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())
orders["delivery_time"] = round(delivery_time/86400)

# Membuat histogram
plt.hist(orders['delivery_time'],
         bins=8,  # Jumlah interval/bins
         alpha=0.7,  # Transparansi warna
         color='blue',  # Warna histogram
         edgecolor='black')  # Warna tepi bin

# Menambahkan label dan judul
plt.title('Histogram of Delivery Time', fontsize=16)
plt.xlabel('Delivery Time (days)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Menampilkan grid
plt.grid(axis='y', alpha=0.75)

# Menampilkan histogram
plt.show()

total_delivery_above_50 = orders[orders['delivery_time'] > 50]['delivery_time'].sum()
print("Total delivery_count yang lebih besar dari 50:", int(total_delivery_above_50))

"""### Explore Customers and Orders"""

# Memeriksa apakah setiap DataFrame memiliki kolom 'customer_id'
for name, df in data.items():
    if 'customer_id' in df.columns:
        print(f"{name} memiliki kolom 'customer_id'")
    else:
        print("")

orders.sample(2)

customers.sample(2)

customers_df = pd.merge(
    left=customers,
    right=orders,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
customers_df.head(5)

"""### Explore Reviews"""

reviews.sample(2)

# Memeriksa apakah setiap DataFrame memiliki kolom 'order_id'
for name, df in data.items():
    if 'order_id' in df.columns:
        print(f"{name} memiliki kolom 'order_id'")
    else:
        print("")

customer_reviews =pd.merge(
    left=customers_df,
    right=reviews,
    how='left',
    left_on='order_id',
    right_on='order_id'
)
customer_reviews.sample(2)

"""### Explore Payments"""

data['payments'].groupby(by="payment_type").order_id.nunique().sort_values(ascending=False)

"""### Explore Items"""

# Memeriksa apakah setiap DataFrame memiliki kolom 'seller_id'
for name, df in data.items():
    if 'seller_id' in df.columns:
        print(f"{name} memiliki kolom 'seller_id'")
    else:
        print("")

sellers.sample(5)

items.sample(5)

item_seller_df = pd.merge(
    left=data['items'],
    right=data['sellers'],
    how="left",
    left_on="seller_id",
    right_on="seller_id"
)
item_seller_df.head()

# mau liat dari seller_state total harga ongkirnya berapa
ongkir_price_counts = item_seller_df.groupby('seller_state')['price'].sum().reset_index(name='Ongkir Price Total Count')
print (ongkir_price_counts)

"""### Explore sellers"""

sellers.sample(5)

#total penjualan di kota tempat asal si penjual
sellers.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False).head(10)

"""### Explore Products and Category"""

products.sample(5)

category.sample(5)

# Memeriksa apakah setiap DataFrame memiliki kolom 'product_category_name'
for name, df in data.items():
    if 'product_category_name' in df.columns:
        print(f"{name} memiliki kolom 'product_category_name'")
    else:
        print("")

# gabungkan products and category. left join karna saya ingin product_category_name_english yang bergabung ke
# kolom data 'products'.
product_df = pd.merge(
    left=data['products'],
    right=data['category'],
    how="left",
    left_on="product_category_name",
    right_on="product_category_name"
)
product_df.head()

product_df.groupby(by="product_category_name_english").product_id.nunique().sort_values(ascending=False).head(10)

# Merge item_seller_df & product_df
sellers_df = pd.merge(
    left=product_df,
    right=item_seller_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)
sellers_df.head()

sellers_df.groupby(by="product_category_name_english").agg({
    "order_id": "nunique",
    "price":  ["min", "max"]
})

"""### Explore Geo"""

data['geo'].sample(5)

data['geo'].groupby('geolocation_zip_code_prefix').size().sort_values(ascending=False)

data['geo'][data['geo']['geolocation_zip_code_prefix'] == 24220].head()

"""### Explore Keseluruhan"""

customers_df.sample(2)

customers_df = pd.merge(
    left=customers,
    right=orders,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
customers_df.head(2)

M1=pd.merge(
    left=customers_df,
    right=payments,
    how='left',
    left_on='order_id',
    right_on='order_id'
)
M1.head()

product_df = pd.merge(
    left=data['products'],
    right=data['category'],
    how="left",
    left_on="product_category_name",
    right_on="product_category_name"
)
product_df.head()

M2=pd.merge(
    left=M1,
    right=items,
    how='left',
    left_on='order_id',
    right_on='order_id'
)
M2.head()

M3=pd.merge(
    left=M2,
    right=sellers,
    how='left',
    left_on='seller_id',
    right_on='seller_id'
)
M3.head()

all_data=pd.merge(
    left=M3,
    right=reviews,
    how='left',
    left_on='order_id',
    right_on='order_id'
)
all_data

"""# RFM"""

all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'])
all_data['order_purchase_timestamp'].max()

all_data['order_purchase_timestamp'].min()

all_data['order_purchase_timestamp'].max()

now = pd.to_datetime('2018-10-30 00:00:00')

all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'])

# Group by 'customer_id' and calculate Recency, Frequency, and Monetary
recency = (now - all_data.groupby('customer_id')['order_purchase_timestamp'].max()).dt.days
frequency = all_data.groupby('customer_id')['order_id'].count()
monetary = all_data.groupby('customer_id')['price'].sum()

# Create a new DataFrame with the calculated metrics
rfm = pd.DataFrame({
    'customer_id': recency.index,
    'Recency': recency.values,
    'Frequency': frequency.values,
    'Monetary': monetary.values
})

col_list = ['customer_id','Recency','Frequency','Monetary']
rfm.columns = col_list

# jumlah uang terbanyak yang dibabiskan oleh customer
rfm.sort_values(by='Monetary',ascending=False)

#customer dengan jumlah pembelian belanja terbanyak
rfm.sort_values(by='Frequency',ascending=False)

# Customer terakhir yang melakukan pembelian
rfm.sort_values(by='Recency',ascending=False)

"""# Visualisasi

### 1. Produk apa yang paling banyak dan sedikit yang terjual?
"""

category.sample()

products.sample()

category_products = pd.merge(
    left=products,
    right=category,
    how="left",
    left_on="product_category_name",
    right_on="product_category_name"
)

product_id_counts = category_products.groupby('product_category_name_english')['product_id'].count().reset_index()
sorted_df = product_id_counts.sort_values(by='product_id', ascending=False)

sorted_df

import seaborn as sns
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="product_id", y="product_category_name_english", data=sorted_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("products with the highest sales", loc="center", fontsize=18)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="product_id", y="product_category_name_english", data=sorted_df.sort_values(by="product_id", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("products with the lowest sales", loc="center", fontsize=18)
ax[1].tick_params(axis='y', labelsize=15)

plt.suptitle("most and least sold products", fontsize=20)
plt.show()

all_data.sample(2)

"""### Wilayah yang paling sering melakukan transaksi"""

other_state_geolocation = data['geo'].groupby(['geolocation_zip_code_prefix'])['geolocation_state'].nunique().reset_index(name='count')
other_state_geolocation[other_state_geolocation['count']>= 2].shape
max_state = data['geo'].groupby(['geolocation_zip_code_prefix','geolocation_state']).size().reset_index(name='count').drop_duplicates(subset = 'geolocation_zip_code_prefix').drop('count',axis=1)

geolocation_silver = data['geo'].groupby(['geolocation_zip_code_prefix','geolocation_city','geolocation_state'])[['geolocation_lat','geolocation_lng']].median().reset_index()
geolocation_silver = geolocation_silver.merge(max_state,on=['geolocation_zip_code_prefix','geolocation_state'],how='inner')

customers_silver = customers_df.merge(geolocation_silver,left_on='customer_zip_code_prefix',right_on='geolocation_zip_code_prefix',how='inner')

customers_silver.head(5)

customers_silver = customers_silver.drop_duplicates('order_id')

def plot_brazil_map(data):
    # Load the Brazil map image
    brazil = mpimg.imread(urllib.request.urlopen('https://i.pinimg.com/originals/3a/0c/e1/3a0ce18b3c842748c255bc0aa445ad41.jpg'), 'jpg')

    # Create a scatter plot on the map
    ax = data.plot(kind="scatter",
                   x="geolocation_lng",
                   y="geolocation_lat",
                   figsize=(10, 10),
                   alpha=0.3,
                   s=0.3,
                   c='blue')  # Change the color to blue

    plt.axis('off')  # Turn off the axis
    plt.imshow(brazil, extent=[-73.98283055, -33.8, -33.75116944, 5.4])  # Display the Brazil map
    plt.show()  # Show the plot

plot_brazil_map(customers_silver.drop_duplicates(subset='customer_unique_id'))

"""### Bagaimana tingkatan review yang diberikan oleh pelanggan?"""

rating_service = reviews['review_score'].value_counts().sort_values(ascending=False)

max_score = rating_service.idxmax()

sns.set(style="darkgrid")

plt.figure(figsize=(10, 5))
sns.barplot(x=rating_service.index,
            y=rating_service.values,
            order=rating_service.index,
            palette=["#72BCD4" if score == max_score else "#D3D3D3" for score in rating_service.index]
            )

plt.title("Rating customers for service", fontsize=15)
plt.xlabel("Rating")
plt.ylabel("Customer")
plt.xticks(fontsize=12)
plt.show()

"""# Kesimpulan

1. Berdasarkan rangkaian step visualisasi yang telah dilakukan sebelumnya, **bed_bath_table** adalah barang yang **paling banyak terjual**. Sedangkan barang yang paling sedikit terjual adalah produk security_and_services


2. Dilihat dari map visualization sebelumnya, kebanyakan transaksi dilakukan di negara bagian tenggara, dan selatan.


3. Sebagian pelanggan menunjukkan tingkat kepuasan yang memuaskan, yang dapat dibuktikan melalui data histogram di atas. Sebagian besar pelanggan memberikan rating sempurna, yaitu nilai 5, dengan rata-rata yang dibulatkan berada di angka 4.


4. Dari analisis RFM yang telah dilakukan sebelumnya, dapat diketahui bahwa Jumlah pembelian tersebar dalam sekali transasksi sebesar 21 produk.Customer terakhir yang melakukan pembelian terakhir 774 hari yang lalu (dengan asumsi waktu sekarang 2018-10-30).Jumlah uang terbanyak yang dibabiskan oleh customer  terbesar 13440.00
"""