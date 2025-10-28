import psycopg2
import numpy as np

# Connect to local PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="ai30_db",
    user="postgres",           # or postgres
    password="yourpassword"
)

cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS embeddings (
    id SERIAL PRIMARY KEY,
    text TEXT,
    embedding VECTOR(1536)
);
""")

# Generate and insert a mock embedding
text = "coffee machine leaking water"
embedding = np.random.rand(1536).tolist()

cur.execute("""
INSERT INTO embeddings (text, embedding)
VALUES (%s, %s);
""", (text, embedding))

conn.commit()

# Query similarity (pgvector <-> operator)
query_vec = np.random.rand(1536).tolist()
cur.execute("""
SELECT text, embedding <-> %s::vector AS distance
FROM embeddings
ORDER BY distance
LIMIT 3;
""", (query_vec,))


for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
print("✅ Connection and query successful.")
