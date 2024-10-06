# -*- coding: utf-8 -*-

pip install streamlit babel
pip install -r requirements.txt

# Deploy
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime
import datetime as dt
import urllib
import matplotlib.image as mpimg

customers = pd.read_csv(".\data\customers.csv")
geolocation = pd.read_csv(".\data\geolocation.csv")
items = pd.read_csv(".\data\order_items.csv")
payments = pd.read_csv(".\data\order_payments.csv")
reviews = pd.read_csv(".\data\order_reviews.csv")
orders = pd.read_csv(".\data\orders.csv", encoding='utf-8')
category = pd.read_csv(".\data\product_category_name_translation.csv", encoding='utf-8')
products = pd.read_csv(".\data\products.csv", encoding='utf-8')
sellers = pd.read_csv(".\data\sellers.csv", encoding='utf-8')

data = {'orders': orders,
        'items': items,
        'products': products,
        'payments': payments,
        'reviews': reviews,
        'customers': customers,
        'sellers': sellers,
        'geo': geolocation,
        'category': category}


# Display logo at the top of each menu
def display_logo():
    st.image("Logo.png", width=400)

# Sidebar for navigation
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Menu", ["Deskripsi", "Analisis E-Commerce"])

customers_df = pd.merge(
    left=customers,
    right=orders,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
    )

M1=pd.merge(
    left=customers_df,
    right=payments,
    how='left',
    left_on='order_id',
    right_on='order_id'
)


product_df = pd.merge(
    left=data['products'],
    right=data['category'],
    how="left",
    left_on="product_category_name",
    right_on="product_category_name"
)

M2=pd.merge(
    left=M1,
    right=items,
    how='left',
    left_on='order_id',
    right_on='order_id'
)

M3=pd.merge(
    left=M2,
    right=sellers,
    how='left',
    left_on='seller_id',
    right_on='seller_id'
)

all_data=pd.merge(
    left=M3,
    right=reviews,
    how='left',
    left_on='order_id',
    right_on='order_id'
)

all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'])
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

#maping
other_state_geolocation = data['geo'].groupby(['geolocation_zip_code_prefix'])['geolocation_state'].nunique().reset_index(name='count')
other_state_geolocation[other_state_geolocation['count']>= 2].shape
max_state = data['geo'].groupby(['geolocation_zip_code_prefix','geolocation_state']).size().reset_index(name='count').drop_duplicates(subset = 'geolocation_zip_code_prefix').drop('count',axis=1)

geolocation_silver = data['geo'].groupby(['geolocation_zip_code_prefix','geolocation_city','geolocation_state'])[['geolocation_lat','geolocation_lng']].median().reset_index()
geolocation_silver = geolocation_silver.merge(max_state,on=['geolocation_zip_code_prefix','geolocation_state'],how='inner')

customers_silver = customers_df.merge(geolocation_silver,left_on='customer_zip_code_prefix',right_on='geolocation_zip_code_prefix',how='inner')
customers_silver = customers_silver.drop_duplicates('order_id')

def plot_brazil_map(data):
    # Load the Brazil map image
    brazil = mpimg.imread('brazil.jpg')
    
    # Create a scatter plot on the map
    fig, ax = plt.subplots(figsize=(10, 10))  # Create a figure and axes
    data.plot(kind="scatter", 
               x="geolocation_lng", 
               y="geolocation_lat", 
               alpha=0.3, 
               s=0.3, 
               c='blue', 
               ax=ax)  # Pass ax to plot on the same axes
    
    plt.axis('off')  # Turn off the axis
    ax.imshow(brazil, extent=[-73.98283055, -33.8, -33.75116944, 5.4])  # Display the Brazil map
    st.pyplot(fig)  # Show the plot in Streamlit



if menu == "Deskripsi":
    display_logo()
    st.title("Deskripsi E-Commerce")
    st.write("""E-commerce adalah suatu bentuk transaksi bisnis yang dilakukan secara online melalui internet, di mana barang, jasa, atau informasi diperjualbelikan antara penjual dan pembeli. E-commerce memiliki fitur yaitu :
             """)
    st.markdown("""
        * Kemudahan akses melalui website atau aplikasi.
        * Pembayaran Digital
        * Sering gratis ongkir.
        * Layanan Pelanggan melalui chat, email, atau telepon.
                """)
    st.title("Deskripsi Proyek")
    st.write("""
    ### Proyek Analisis E-Commerce
    Proyek ini bertujuan untuk menganalisis penjualan dan pembelian di suatu E-Commerce yang terletak di Brazil.
    Terdiri dari 9 dataset yaitu customers, geolocation, order_items, order_payments, order_review, orders, product_category, products, users.          
    
    \n Dalam konsistensi perusahaan untuk memberikan pelayanan yang terbaik kepada user/pelanggan, perusahaan akan terus berinovasi dengan meningkatkan pelayanan pada website dan memperkenalkan 
    fitur-fitur baru yang memudahkan navigasi serta interaksi.Selain itu, perusahaan juga akan fokus pada personalisasi pengalaman pengguna dengan memberikan rekomendasi produk yang relevan 
    berdasarkan riwayat pembelian dan preferensi mereka. Dengan demikian, masyarakat pengguna E-commerce akan lebih nyaman dalam bertransaksi.  
    
    \n Untuk menjawab permasalahan tersebut saya akan memberikan referensi sebagai berikut :
        """)
    st.markdown("""
        1. Produk apa yang paling banyak dan sedikit terjual?
        2. Wilayah mana yang paling sering melakukan transaksi?
        3. Bagaimana tingkatan review yang diberikan oleh pelanggan ke suatu produk?
                """)

elif menu == "Analisis E-Commerce":
    display_logo()
    # Define your Streamlit app
    st.title("E-Commerce Analysis Dashboard")
    
    # ========================================================================================
    # =============================== Mapping Most Transaction ===============================
    # ========================================================================================

    st.subheader("Mapping Most Transaction")
    plot_brazil_map(customers_silver.drop_duplicates(subset='customer_unique_id'))

    with st.expander("See Explanation"):
        st.write('According to the graph that has been created, there are more customers in the southeast and south. Other information, there are more customers in cities that are capitals (São Paulo, Rio de Janeiro, Porto Alegre, and others).')


    # ========================================================================================
    # ======================================== RFM ===========================================
    # ========================================================================================
    st.subheader("RFM")

    #colors
    colors = ["#FF5733", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # beri comentar pada ax[index].set_xticks([]) bila ingin melihat customer nya by id

    #####################################3
    tab1, tab2, tab3 = st.tabs(["Recency", "Frequency", "Monetary"])

    with tab1:
        plt.figure(figsize=(16, 8))
        sns.barplot(
            y="Recency",
            x="customer_id",
            data=rfm.sort_values(by="Recency", ascending=True).head(5),
            palette=colors,

            )
        plt.title("By Recency (Day)", loc="center", fontsize=18)
        plt.ylabel('')
        plt.xlabel("customer")
        plt.tick_params(axis ='x', labelsize=15)
        plt.xticks([])
        st.pyplot(plt)

    with tab2:
        plt.figure(figsize=(16, 8))
        sns.barplot(
            y="Frequency",
            x="customer_id",
            data=rfm.sort_values(by="Frequency", ascending=False).head(5),
            palette=colors,

            )
        plt.ylabel('')
        plt.xlabel("customer")
        plt.title("By Frequency", loc="center", fontsize=18)
        plt.tick_params(axis ='x', labelsize=15)
        plt.xticks([])
        st.pyplot(plt)

    with tab3:
        plt.figure(figsize=(16, 8))
        sns.barplot(
            y="Monetary",
            x="customer_id",
            data=rfm.sort_values(by="Monetary", ascending=False).head(5),
            palette=colors,
            )
        plt.ylabel('')
        plt.xlabel("customer")
        plt.title("By Monetary", loc="center", fontsize=18)
        plt.tick_params(axis ='x', labelsize=15)
        plt.xticks([])
        st.pyplot(plt)

    # ========================================================================================
    # ================================ Most & Least Products =================================
    # ========================================================================================
    category_products = pd.merge(
        left=products,
        right=category,
        how="left",
        left_on="product_category_name",
        right_on="product_category_name"
    )
    def create_by_product_df(df):
        product_id_counts = df.groupby(category_products['product_category_name_english'])['product_id'].count().reset_index()
        sorted_df = product_id_counts.sort_values(by='product_id', ascending=False)
        return sorted_df

    most_and_least_products_df=create_by_product_df(all_data)

    st.subheader("Most And Least Product")
    col1, col2 = st.columns(2)
    with col1:
        highest_product_sold=most_and_least_products_df['product_id'].max()
        st.markdown(f"Higest Number : **{highest_product_sold}**")

    with col2:
        lowest_product_sold=most_and_least_products_df['product_id'].min()
        st.markdown(f"Lowest Number : **{lowest_product_sold}**")

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    #sns.barplot(x="product_id", y="product_category_name_english", data=most_and_least_products_df.head(5),hue="product_category_name_english", palette=colors, ax=ax[0],)


    sns.barplot(
        x="product_id",
        y="product_category_name_english",
        data=most_and_least_products_df.head(5),
        palette=colors,
        ax=ax[0],
        )
    ax[0].set_ylabel('')
    ax[0].set_xlabel('')
    ax[0].set_title("products with the highest sales", loc="center", fontsize=18)
    ax[0].tick_params(axis ='y', labelsize=15)

    sns.barplot(
        x="product_id",
        y="product_category_name_english",
        data=most_and_least_products_df.sort_values(by="product_id", ascending=True).head(5),
        palette=colors,
        ax=ax[1],)
    ax[1].set_ylabel('')
    ax[1].set_xlabel('')
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("products with the lowest sales", loc="center", fontsize=18)
    ax[1].tick_params(axis='y', labelsize=15)

    plt.suptitle("most and least sold products", fontsize=20)
    st.pyplot(fig)

    # ========================================================================================
    # ===================================== Review Score =====================================
    # ========================================================================================
    st.subheader("Review Rating")
    rating_service = reviews['review_score'].value_counts().sort_values(ascending=False)

    max_score = rating_service.idxmax()

    sns.set(style="darkgrid")

    plt.figure(figsize=(10, 5))
    sns.barplot(
        x=rating_service.index,
        y=rating_service.values,
        order=rating_service.index,
        palette=["#72BCD4" if score == max_score else "#D3D3D3" for score in rating_service.index]
    )

    plt.title("Rating customers for service", fontsize=15)
    plt.xlabel("Rating")
    plt.ylabel("Customer")
    plt.xticks(fontsize=12)

    st.pyplot(plt)
    
    with st.expander("See Explanation"):
        st.write('Some customers show a good level of satisfaction, as shown in the histogram above. Most customers give a perfect rating of 5, with the average rating being around 4.')


    st.caption('Copyright (C) Bernardinus Rico 2024')
