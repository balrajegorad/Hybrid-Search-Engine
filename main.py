import chromadb
import configparser
import pandas as pd
import streamlit as st
from scripts.db import get_mysql_conn
from sentence_transformers import SentenceTransformer

# Load configuration
config = configparser.ConfigParser()
config.read("config.ini")

# ChromaDB and embedding model configuration
chroma_directory = config['chroma']['chroma_directory']
collection_name = config['chroma']['collection_name']
num_of_results = int(config['chroma']['num_of_results'])
embedding_model_name = config['chroma']['embedding_model']

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path=chroma_directory)
collection = chroma_client.get_collection(collection_name)

# Load embedding model
embedding_model = SentenceTransformer(embedding_model_name)

# Establish MySQL connection
conn = get_mysql_conn()


# Streamlit configuration
st.set_page_config(
    page_title="Hybrid Product Search",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar setup
st.sidebar.header("Semantic Search")
st.sidebar.image("images/product_search.png", use_column_width=True, caption="Product Semantic Search")


# Main header
st.header("Hybrid Product Semantic Search")

# Dropdown for query type
query_type = st.selectbox("Search by:", ["Product Name", "Description", "Price Range"])

# Search by Product Name
if query_type == "Product Name":
    product_name = st.text_input("Enter product name:")
    if st.button("Search"):
        if not product_name.strip():
            st.warning("Please enter a valid product name.")
        else:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM products WHERE name LIKE %s", ('%' + product_name + '%',))
                    results = cursor.fetchall()

                    if results:
                        columns = ['ID', 'Name', 'Price', 'Category', 'Description']
                        df_results = pd.DataFrame(results, columns=columns)
                        st.subheader("Results from MySQL:")
                        st.table(df_results)
                    else:
                        st.write("No products found.")
            except Exception as e:
                st.error(f"Error while querying the database: {e}")

# Search by Description
elif query_type == "Description":
    description_query = st.text_input("Enter product description:")
    if st.button("Search"):
        if not description_query.strip():
            st.warning("Please enter a valid description.")
        else:
            try:
                query_vector = embedding_model.encode(description_query)
                results = collection.query(query_vector, n_results=num_of_results)

                if results['metadatas']:
                    st.write("Results from Chroma DB:")
                    for result in results['metadatas']:
                        st.table(result)
                else:
                    st.write("No products found in Chroma DB.")
            except Exception as e:
                st.error(f"Error while querying ChromaDB: {e}")

# Search by Price Range
elif query_type == "Price Range":
    min_price = st.number_input("Minimum Price:", min_value=0.0, step=0.01, format="%.2f")
    max_price = st.number_input("Maximum Price:", min_value=0.0, step=0.01, format="%.2f")
    if st.button("Search"):
        if min_price > max_price:
            st.warning("Minimum price cannot be greater than maximum price.")
        else:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM products WHERE price BETWEEN %s AND %s", (min_price, max_price))
                    results = cursor.fetchall()

                    if results:
                        columns = ['ID', 'Name', 'Price', 'Category', 'Description']
                        df_results = pd.DataFrame(results, columns=columns)
                        st.subheader("Results from MySQL:")
                        st.table(df_results)
                    else:
                        st.write("No products found within the specified price range.")
            except Exception as e:
                st.error(f"Error while querying the database: {e}")
