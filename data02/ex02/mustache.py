import psycopg2
import matplotlib.pyplot as plt

def first_box(cursor, prices):
    plt.figure(figsize=(10, 8))
    box = plt.boxplot(
        prices,
        vert=False,
        widths=0.8,
        notch=True,
        patch_artist=True,
        boxprops=dict(facecolor='#5c5c5b', color='#5c5c5b', linewidth=1.3),
        medianprops=dict(color='#5c5c5b', linewidth=1.3),
        flierprops=dict(marker='D', markerfacecolor='#5c5c5b', color=None, markersize=8))
    for patch in box['boxes']:
        patch.set_facecolor('#82ad7c')

    plt.gca().set_facecolor('#e7e7ed')
    plt.gca().set_axisbelow(True)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.grid(axis='x', color='white', linestyle='-', linewidth=1.2)
    
    plt.tick_params(axis='both', which='both', color='none')
    plt.xlabel('price')

    plt.margins(x=0.1, y=0)
    plt.xlim(left=-100, right=350)

    x_ticks = plt.gca().get_xticks()
    plt.xticks(x_ticks[1:-1])

    plt.show()

def second_box(cursor, prices):
    plt.figure(figsize=(10, 8))
    box = plt.boxplot(prices,
        vert=False,
        widths=0.8,
        showfliers=False,
        boxprops=dict(facecolor='#5c5c5b', color='#5c5c5b', linewidth=1.5),
        medianprops=dict(color='#5c5c5b', linewidth=1.5),
        patch_artist=True,)

    for patch in box['boxes']:
        patch.set_facecolor('#82ad7c')

    plt.gca().set_facecolor('#e7e7ed')
    plt.gca().set_axisbelow(True)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.grid(axis='x', color='white', linestyle='-', linewidth=1.2)
    
    plt.tick_params(axis='both', which='both', color='none')
    plt.xlabel('price')

    plt.margins(x=0.1, y=0)

    x_ticks = plt.gca().get_xticks()
    plt.xticks(x_ticks[1:-1])

    plt.show()

def mustache():
    conn = psycopg2.connect(
        host="localhost",
        database="piscineds",
        user="zpalfi",
        password="mysecretpassword"
    )

    cursor = conn.cursor()
    query = """
        SELECT price FROM customers
        WHERE event_type = 'purchase'
    """

    cursor.execute(query)
    data = cursor.fetchall()
    prices = [row[0] for row in data]
    mean = sum(prices) / len(prices)
    print(f"Mean price: {mean}")
    std = (sum((x - mean) ** 2 for x in prices) / len(prices)) ** 0.5
    print(f"Standard deviation: {std}")
    min_price = min(prices)
    print(f"Minimum price: {min_price}")
    first_quartile = sorted(prices)[len(prices) // 4]
    print(f"First quartile: {first_quartile}")
    median = sorted(prices)[len(prices) // 2]
    print(f"Median: {median}")
    third_quartile = sorted(prices)[3 * len(prices) // 4]
    print(f"Third quartile: {third_quartile}")
    max_price = max(prices)
    print(f"Maximum price: {max_price}")

    #first_box(cursor, prices)
    #second_box(cursor, prices)

    query = """
        SELECT SUM(price) as avg_price
        FROM customers
        WHERE event_type = 'cart'
        GROUP BY user_id;
    """

    cursor.execute(query)
    data = cursor.fetchall()
    avg_prices = [row[0] for row in data]
    
    plt.figure(figsize=(10, 8))
    plt.boxplot(avg_prices,
        vert=False,
        widths=0.8,
        notch=True,
        patch_artist=True,
        boxprops=dict(facecolor='#5c5c5b', color='#5c5c5b', linewidth=1.3),
        medianprops=dict(color='#5c5c5b', linewidth=1.3),
        flierprops=dict(marker='D', markerfacecolor='#5c5c5b', color=None, markersize=8))
    plt.show()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    mustache()