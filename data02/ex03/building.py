import psycopg2
import matplotlib.pyplot as plt
import numpy as np

def frequency(freq):
    plt.hist(freq, bins=range(0,41,8), edgecolor='white', color='#b1c1d7')
    
    plt.gca().set_facecolor('#e7e7ed')
    plt.gca().set_axisbelow(True)
    plt.grid(color='white', linestyle='-', linewidth=1.2)
    
    plt.tick_params(axis='both', which='both', color='none')
    plt.xticks(range(0, 41, 10))

    plt.xlabel('frequency')
    plt.ylabel('customers')

    plt.show()

def monetary_value(total):
    plt.hist(total, bins=range(-30, 240, 50), edgecolor='white', color='#b1c1d7')

    plt.gca().set_facecolor('#e7e7ed')
    plt.gca().set_axisbelow(True)
    plt.grid(color='white', linestyle='-', linewidth=1.2)

    plt.tick_params(axis='both', which='both', color='none')
    
    plt.xticks(range(0, 250, 50))
    plt.yticks(range(0, 45000, 5000))

    plt.ylim(0, 45000)

    plt.xlabel('monetary value in ₳')
    plt.ylabel('customers')

    plt.show()

def building():
    conn = psycopg2.connect(
        host="localhost",
        database="piscineds",
        user="zpalfi",
        password="mysecretpassword"
    )
    cursor = conn.cursor()

    query = """
        SELECT user_id, COUNT(price) as freq, SUM(price) as total
        FROM customers
        WHERE event_type = 'purchase'
        GROUP BY user_id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    freq = [row[1] for row in data]
    total = [row[2] for row in data]

    frequency(freq)
    monetary_value(total)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    building()