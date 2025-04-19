import psycopg2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def elbow():
    conn = psycopg2.connect(
        host="localhost",
        database="piscineds",
        user="zpalfi",
        password="mysecretpassword"
    )
    cursor = conn.cursor()

    query = """
        SELECT user_id, SUM(price) as total
        FROM customers
        WHERE event_type = 'purchase'
        GROUP BY user_id
    """

    cursor.execute(query)
    data = cursor.fetchall()
    total = [row[1] for row in data]
    total = np.array(total).reshape(-1, 1)
    wcss = []

    for k in range(1,11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(total)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(10, 8))
    plt.plot(range(1, 11), wcss, marker='o', color='#b1c1d7')
    plt.show()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    elbow()