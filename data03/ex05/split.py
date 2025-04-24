import pandas as pd
from sklearn.model_selection import train_test_split

def split():
    csv_path = "/home/zpalfi/goinfre/Train_knight.csv"

    df = pd.read_csv(csv_path)

    train, val = train_test_split(df, test_size=0.2, random_state=42)

    train.to_csv("/home/zpalfi/goinfre/Training_knight.csv", index=False)
    val.to_csv("/home/zpalfi/goinfre/Validation_knight.csv", index=False)

if __name__ == "__main__":
    split()