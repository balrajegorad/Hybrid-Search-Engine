# Hybrid-Search-Engine
This project implements a Hybrid Product Search Engine using a combination of MySQL for structured queries and ChromaDB for semantic vector-based searches. Users can search products by name, description, or price range through a user-friendly Streamlit web interfa

# Hybrid Product Search Engine

This project implements a **Hybrid Product Search Engine** using a combination of MySQL for structured queries and ChromaDB for semantic vector-based searches. Users can search products by name, description, or price range through a user-friendly Streamlit web interface.

---

## **Features**

- **Search by Product Name:** Retrieve products based on exact or partial name matches.
- **Search by Description:** Perform semantic searches using Sentence Transformers and ChromaDB.
- **Search by Price Range:** Query products within a specified price range.
- **Hybrid Search Engine:** Combines traditional database searches with advanced embedding-based similarity searches.

---

## **Project Structure**

```plaintext
hybrid_search/
│
├── chroma_db/                      # Directory for ChromaDB-related files
├── images/                         # Directory for UI images
│   └── product_search.png          # Placeholder for uploading app screenshots
├── scripts/                        # Directory for Python scripts
│   ├── __init__.py                 # Initializes the scripts folder as a Python module
│   ├── db.py                       # Script for MySQL database connection
│   ├── create_embeddings.py        # Script to generate embeddings and store in ChromaDB
│   ├── query_embeddings.py         # Script to query ChromaDB
├── config.ini                      # Configuration file for database and ChromaDB settings
├── main.py                         # Main Streamlit application file
├── products.sql                    # SQL script for creating the database and tables
├── readme.md                       # Documentation for the project
└── requirements.txt                # Python dependencies
```

---

## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-repo/hybrid_search.git
cd hybrid_search
```

### **2. Install Dependencies**

Install all required Python packages using the following command:

```bash
pip install -r requirements.txt
```

### **3. Set Up MySQL Database**

1. Open MySQL Workbench or your preferred SQL client.
2. Run the SQL script in `products.sql` to create the database and tables.

```sql
source products.sql;
```

3. Update the `config.ini` file with your MySQL credentials.

### **4. Generate Embeddings**

Create embeddings for product descriptions and store them in ChromaDB:

```bash
python scripts/create_embeddings.py
```

### **5. Run the Application**

Launch the Streamlit app:

```bash
streamlit run main.py
```

The app will open in your default web browser. If not, access it via the provided URL (e.g., `http://localhost:8501`).

---

## **Configuration**

The application settings are stored in `config.ini`. Update the file as needed:

```ini
[mysql]
host = localhost
port = 3306
user = your_username
password = your_password
database_name = salesdb1

[chroma]
num_of_results = 3
collection_name = product_descriptions
chroma_directory = chroma_db
embedding_model = all-MiniLM-L6-v2
```

- **MySQL Section:** Configure database connection settings.
- **Chroma Section:** Specify the embedding model and directory for ChromaDB storage.

---

## **Screenshots**

### Upload your app screenshots in the `images/` folder and replace the placeholders below.

1. **Home Screen**

2. **Search Results by Name**

3. **Search Results by Description**

4. **Search Results by Price Range**

---

## **How It Works**

### **1. Hybrid Search**

- **Traditional SQL Search:**
  - Queries product names and prices using structured SQL queries.
- **Semantic Search:**
  - Converts product descriptions into embeddings using a Sentence Transformer model.
  - Stores embeddings in ChromaDB.
  - Retrieves similar descriptions based on cosine similarity.

### **2. User Interface**

The app provides an intuitive interface using Streamlit:

- Select the search method (Name, Description, or Price Range).
- Enter the query and view the results in a table format.

---

## **Technologies Used**

### **Backend**

- MySQL: Relational database for structured data.
- ChromaDB: Embedding database for semantic search.
- Sentence Transformers: Pre-trained transformer model for generating embeddings.

### **Frontend**

- Streamlit: Interactive web application framework.

---

## **Future Improvements**

1. Add more advanced filtering and sorting options.
2. Support for additional embedding models.
3. Expand search capabilities (e.g., by category).



Enjoy using the Hybrid Product Search Engine! 🚀

