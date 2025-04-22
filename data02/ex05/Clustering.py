import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def clustering():
    conn = psycopg2.connect(
        host="localhost",
        database="piscineds",
        user="zpalfi",
        password="mysecretpassword"
    )
    cursor = conn.cursor()

    query = """
        SELECT user_id,
            DATE_PART('month', AGE(NOW(), MAX(event_time))) AS recency,
            COUNT(*) AS frequency,
            SUM(price) AS monetary
        FROM your_table
        WHERE event_type = 'purchase'
        GROUP BY user_id
    """

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    df = pd.DataFrame(data, columns=['user_id', 'recency', 'frequency', 'monetary'])
    df[['recency', 'frequency', 'monetary']] = StandardScaler().fit_transform(df[['recency', 'frequency', 'monetary']]).fillna(0)

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['recency', 'frequency', 'monetary']])


if __name__ == "__main__":
    clustering()
