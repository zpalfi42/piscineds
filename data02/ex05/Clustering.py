import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

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
            DATE_PART('day', AGE(NOW(), MAX(event_time))) AS recency,
            COUNT(*) AS frequency,
            SUM(price) AS monetary
        FROM customers
        WHERE event_type = 'purchase'
        GROUP BY user_id
    """

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    df = pd.DataFrame(data, columns=['user_id', 'recency', 'frequency', 'monetary'])
    df[['recency', 'frequency', 'monetary']] = df[['recency', 'frequency', 'monetary']].apply(pd.to_numeric, errors='coerce').fillna(0)

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['recency', 'frequency', 'monetary']])

    kmeans = KMeans(n_clusters=5, random_state=42)
    df['cluster'] = kmeans.fit_predict(df_scaled)

    cluster_stats = df.groupby('cluster')[['recency', 'frequency', 'monetary']].mean()
    print(cluster_stats)

    # Adjust the cluster_labels mapping based on your actual cluster statistics
    cluster_labels = {
        0: 'Inactive users',       # Moderate recency, low frequency/monetary
        1: 'New users',            # Very recent but low activity
        2: 'Loyalty Platinum',     # High frequency and monetary
        3: 'Loyalty Gold',         # Medium frequency and monetary
        4: 'Loyalty Silver'        # Low frequency and monetary but somewhat recent
    }

    df['segment'] = df['cluster'].map(cluster_labels)

    # Verify the mapping
    segment_stats = df.groupby('segment')[['recency', 'frequency', 'monetary']].mean()
    print(segment_stats)

    # Visualize the segments
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df, x='frequency', y='monetary', hue='segment', palette='viridis', size='recency')
    plt.title('Customer Segments by Frequency, Monetary Value, and Recency (size)')
    plt.show()

if __name__ == "__main__":
    clustering()
