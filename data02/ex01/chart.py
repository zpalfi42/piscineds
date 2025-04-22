import psycopg2
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator

def number_of_customers(cursor):
    query = """
        SELECT DATE(event_time) AS day, COUNT(DISTINCT user_id) AS users
        FROM customers
        WHERE event_type = 'purchase' 
        GROUP BY day
        ORDER BY day;
    """

    cursor.execute(query)
    data=cursor.fetchall()

    days = [row[0] for row in data]
    users = [row[1] for row in data]

    plt.figure(figsize=(10, 8))

    plt.plot(days, users, linestyle='-', color='b')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    plt.gca().set_facecolor('#e7e7ed')

    plt.grid(visible=True, color='white', linestyle='-', linewidth=1.2)

    plt.xlabel('')
    plt.ylabel('Number of customers')
    plt.tick_params(axis='both', which='both', color='none')

    plt.margins(x=0, y=0.1)
    plt.ylim(bottom=0)

    plt.tight_layout()

    plt.show()

def total_sales(cursor):
    query = """
        SELECT DATE_TRUNC('month', event_time) AS month, SUM(price) / 1000000 AS total
        FROM customers
        WHERE event_type = 'purchase' 
        GROUP BY month
        ORDER BY month;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    months = [row[0] for row in data]
    total = [row[1] for row in data]

    plt.figure(figsize=(10, 8))
    plt.bar(months, total, edgecolor='white', color='#b6c2d2', width=20)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    plt.xlabel('month')
    plt.ylabel('total sales in million of ₳')

    plt.gca().set_facecolor('#e7e7ed')
    plt.gca().set_axisbelow(True)

    plt.grid(axis='y', color='white', linestyle='-', linewidth=1.2)
    plt.tick_params(axis='both', which='both', color='none')


    plt.tight_layout

    plt.show()

def average_spend(cursor):
    query = """
        SELECT DATE(event_time) as day, SUM(price) / COUNT (DISTINCT user_id) as avg
        FROM customers
        WHERE event_type = 'purchase' 
        GROUP BY day
        ORDER BY day;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    days = [row[0] for row in data]
    avg = [row[1] for row in data]

    plt.figure(figsize=(10, 8))
    
    plt.plot(days, avg, linestyle='-', color='#b1c1d7')

    plt.fill_between(days, avg, color='#b1c1d7', alpha=1)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    plt.gca().yaxis.set_major_locator(MultipleLocator(5))

    plt.xlabel('')
    plt.ylabel('Average spend/customers in ₳')

    plt.gca().set_facecolor('#e7e7ed')
    plt.gca().set_axisbelow(True)

    plt.grid(visible=True, color='white', linestyle='-', linewidth=1.2)

    plt.ylim(bottom=0)
    plt.margins(x=0, y=0.1)
    plt.tight_layout()
    plt.tick_params(axis='both', which='both', color='none')

    plt.show()

def chart():
    conn = psycopg2.connect(
        host="localhost",
        database="piscineds",
        user="zpalfi",
        password="mysecretpassword",
    )
    cursor = conn.cursor()

    number_of_customers(cursor)
    total_sales(cursor)
    average_spend(cursor)

    cursor.close()
    conn.close()   



if __name__ == "__main__":
    chart()