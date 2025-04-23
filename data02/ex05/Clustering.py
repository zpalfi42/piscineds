import pandas as pd
import psycopg2
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def chart1(df, centroids):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='scaled_frequency', y='scaled_monetary', hue='cluster', data=df, palette='viridis', s=50)
        plt.scatter(centroids[:, 1], centroids[:, 2], marker='o', s=200, color='yellow', label='Centroids') # Indices 1 and 2 correspond to scaled_frequency and scaled_monetary
        plt.title('Clusters of Customers (Scaled Frequency vs. Scaled Monetary)')
        plt.xlabel('Scaled Frequency')
        plt.ylabel('Scaled Monetary')
        plt.legend(title='Cluster')
        plt.grid(True)
        plt.show()

def chart2(df):
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(data=df, x='segment', order=df['segment'].value_counts().index,
                    palette='viridis')
    plt.xticks(rotation=45, ha='right')
    plt.title('Number of Customers in Each Segment')

    for p in ax.patches:
        ax.annotate(f'{p.get_height():.0f}', 
                    (p.get_x() + p.get_width()/2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')

    plt.tight_layout()
    plt.show()

def clustering_and_plotting_raw_rf():
    db_config = {
        "host": "localhost",
        "database": "piscineds",
        "user": "zpalfi",
        "password": "mysecretpassword"
    }

    try:
        conn = psycopg2.connect(**db_config)
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
        df_scaled = pd.DataFrame(df_scaled, columns=['scaled_recency', 'scaled_frequency', 'scaled_monetary'])
        df = pd.concat([df, df_scaled], axis=1)

        n_clusters = 5
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        df['cluster'] = kmeans.fit_predict(df[['scaled_recency', 'scaled_frequency', 'scaled_monetary']])

        centroids = kmeans.cluster_centers_

        chart1(df, centroids)
        cluster_labels = {
            0: 'New users',       # Moderate recency, low frequency/monetary
            1: 'Inactive users',            # Very recent but low activity
            2: 'Loyalty Platinum',     # High frequency and monetary
            3: 'Loyalty Gold',         # Medium frequency and monetary
            4: 'Loyalty Silver'        # Low frequency and monetary but somewhat recent
        }

        df['segment'] = df['cluster'].map(cluster_labels)
        chart2(df.copy())

    except psycopg2.Error as e:
        print(f"Error connecting to or querying the database: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clustering_and_plotting_raw_rf()