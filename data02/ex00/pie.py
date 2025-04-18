import psycopg2
import matplotlib.pyplot as plt

def pie():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="zpalfi",
            password="mysecretpassword"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT event_type, COUNT(*) FROM customers GROUP BY event_type")
        data = cursor.fetchall()
        desired_order = ['view', 'cart', 'remove_from_cart', 'purchase' ]
        data = sorted(data, key=lambda x: desired_order.index(x[0]) if x[0] in desired_order else len(desired_order))
        labels = [row[0] for row in data]
        sizes = [row[1] for row in data]

        color_map = {
            'view': '#4c72b0',
            'remove_from_cart': '#55a868',
            'purchase': '#c44e52',
            'cart': '#dd8452'
        }

        colors = [color_map.get(label, "gray") for label in labels]

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=0)
        plt.title('Event Type Distribution')
        plt.show()

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pie()