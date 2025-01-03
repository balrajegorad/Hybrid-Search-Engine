import chromadb
import configparser
from sentence_transformers import SentenceTransformer
from scripts.db import get_mysql_conn

config = configparser.ConfigParser()
config.read("config.ini")

# Initialize ChromaDB and Sentence Transformers
chroma_client = chromadb.PersistentClient(path=config['chroma']['chroma_directory'])
collection = chroma_client.get_collection(config['chroma']['collection_name'])
model = SentenceTransformer(config['chroma']['embedding_model'])

# Connect to MySQL
conn = get_mysql_conn()

# Get all existing IDs from the collection
existing_ids = collection.get()['ids']  # Retrieves all IDs in the collection
if existing_ids:
    collection.delete(ids=existing_ids)  # Delete all entries by ID
    print("Previous embeddings deleted.")
else:
    print("No embeddings found to delete.")

# Regenerate embeddings for updated SQL data
with conn.cursor() as cursor:
    cursor.execute("SELECT id, description FROM products")
    products = cursor.fetchall()

    for product_id, description in products:
        embedding = model.encode(description)
        collection.add(
            ids=[str(product_id)],
            embeddings=[embedding],
            metadatas=[{"id": product_id, "description": description}]
        )
        print(f"Created new embedding for Product ID {product_id}")

conn.close()
print("New embeddings added to ChromaDB.")
