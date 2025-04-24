import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def normalization():
    csv_path = "/home/zpalfi/goinfre/Train_knight.csv"
    csv_path2 = "/home/zpalfi/goinfre/Test_knight.csv"

    df = pd.read_csv(csv_path)
    df2 = pd.read_csv(csv_path2)

    df['knight'] = df['knight'].map({'Sith': 0, 'Jedi': 1})

    features = df.drop(columns=['knight'])
    features2 = df2

    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(features)
    normalized_data2 = scaler.transform(features2)

    normalized_df = pd.DataFrame(normalized_data, columns=features.columns)
    normalized_df2 = pd.DataFrame(normalized_data2, columns=features2.columns)

    print(df.drop(columns=['knight']).head(1))
    print(normalized_df.head(1))

    sith_data = normalized_df[df['knight'] == 0]
    jedi_data = normalized_df[df['knight'] == 1]

    plt.figure(figsize=(12, 8))
    plt.scatter(sith_data['Push'].values, sith_data['Deflection'].values,
                color='blue', marker='o', alpha=0.4)
    plt.scatter(jedi_data['Push'].values, jedi_data['Deflection'].values,
                color='red', marker='o', alpha=0.4)
    plt.legend(["Sith", "Jedi"], loc='upper right')
    plt.show()

if __name__ == "__main__":
    normalization()