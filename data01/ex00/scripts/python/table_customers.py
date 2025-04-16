"""_summary_
"""

import psycopg2
import pandas as pd

def existing_table(conn, table):
    """_summary_
    """
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT * FROM information_schema.tables"\
                   " WHERE table_name=%s)", (table,))
    return cursor.fetchone()[0]

def create_table(path: str):
    """_summary_
    """
    print(path[-17:-4])
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="zpalfi",
            password="mysecretpassword"
        )
        if existing_table(conn, path[-17:-4]) is True:
            raise AssertionError("Table already exists")
        print(f"Creating table {path[-17:-4]}")
        df = pd.read_csv(path)
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE {path[-17:-4]} (" \
                       f"{df.columns.values[0]} TIMESTAMP WITH TIME ZONE," \
                       f"{df.columns.values[1]} VARCHAR(100)," \
                       f"{df.columns.values[2]} INT," \
                       f"{df.columns.values[3]} FLOAT," \
                       f"{df.columns.values[4]} INT," \
                       f"{df.columns.values[5]} UUID )" \
                    )
        with open(path, 'r', encoding='UTF8') as csvfile:
            cursor.copy_expert(f"COPY {path[-17:-4]} FROM STDIN WITH CSV HEADER", csvfile)
        cursor.close()
        conn.commit()
        cursor.close()
        conn.close()
    except  AssertionError as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     create_table('/subject/customer/data_2022_oct.csv')