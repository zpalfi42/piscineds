import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from matplotlib.ticker import ScalarFormatter

def elbow():
    conn = psycopg2.connect(
        host="localhost",
        database="piscineds",
        user="zpalfi",
        password="mysecretpassword"
    )
    cursor = conn.cursor()

    query = """
        SELECT user_id, COUNT(*) as frequency, SUM(price) as total
        FROM customers
        WHERE event_type = 'purchase'
        GROUP BY user_id
    """

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    df = pd.DataFrame(data, columns=['user_id', 'frequency', 'total'])
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['frequency', 'total']])

    wcss = []
    for k in range(1,11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df_scaled)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(10, 8))
    plt.plot(range(1, 11), wcss, color='blue')

    plt.gca().set_facecolor('#e7e7ed')
    plt.gca().set_axisbelow(True)
    plt.grid(color='white', linestyle='-', linewidth=1.2)
    
    plt.tick_params(axis='both', which='both', color='none')

    plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
    plt.gca().yaxis.get_major_formatter().set_scientific(False)
    
    plt.xlabel('Number of clusters')
    plt.ylabel('')

    plt.ylim(bottom=0)

    
    plt.show()

if __name__ == "__main__":
    elbow()