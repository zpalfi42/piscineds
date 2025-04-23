import pandas as pd

def correlation():
    csv_path = "/home/zpalfi/goinfre/Train_knight.csv"

    df = pd.read_csv(csv_path)
    df['knight'] = df['knight'].map({'Sith': 0, 'Jedi': 1})

    corr = df.corr()
    knight_corr = corr['knight'].abs().sort_values(ascending=False)

    formatted_output = ""
    for col, corr_value in knight_corr.items():
        formatted_output += f"{col:<25} {corr_value:.6f}\n"

    print(formatted_output)

if __name__ == "__main__":
    correlation()