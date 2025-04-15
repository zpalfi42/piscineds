import psycopg2
import pandas as pd

def get_matching_tables(conn, pattern):
    """_summary_
    """
    query = f"""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public' AND table_name LIKE '{pattern}'
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return [row[0] for row in cursor.fetchall()]

def combine_tables_to_customers(conn, tables, target_table):
    """_summary_
    """
    dataframes = []
    for table in tables:
        query = f"SELECT * FROM {table};"
        try:
            df = pd.read_sql(query, conn)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading table {table}: {e}")

    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        combined_df.to_sql(target_table, conn, if_exists='replace', index=False)
        print(f"Combined data from {len(tables)} tables into {target_table}.")

def main():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="zpalfi",
            password="mysecretpassword"
        )
        pattern = 'data_202%_%%%'
        tables = get_matching_tables(conn, pattern)

        if not tables:
            print(f"No tables found matching pattern: {pattern}")
            return
        
        combine_tables_to_customers(conn, tables, 'customers')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()