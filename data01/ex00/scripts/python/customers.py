"""_summary_
"""

import os
from table_customers import create_table

def create_tables_from_folder(path: str):
    """_summary_

    Args:
        path (str): _description_
    """
    files = [f for f in os.listdir(path) if f[-4:]=='.csv']
    for f in files:
        create_table(path+f)

if __name__ == "__main__":
    create_tables_from_folder("/subject/customer/")