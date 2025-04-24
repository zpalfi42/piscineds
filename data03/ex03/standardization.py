import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def standarization():
    csv_path = "/home/zpalfi/goinfre/Train_knight.csv"
    csv_path2 = "/home/zpalfi/goinfre/Test_knight.csv"

    df = pd.read_csv(csv_path)
    df2 = pd.read_csv(csv_path2)

    df['knight'] = df['knight'].map({'Sith': 0, 'Jedi': 1})

    features = df.drop(columns=['knight'])
    features2 = df2

    scaler = StandardScaler()

    standarized_data = scaler.fit_transform(features)
    standarized_data2 = scaler.transform(features2)

    standarized_df = pd.DataFrame(standarized_data, columns=features.columns)
    standarized_df2 = pd.DataFrame(standarized_data2, columns=features2.columns)

    print(df.drop(columns=['knight']).head(1))
    print(standarized_df.head(1))
    # print(df2.head(1))
    # print(standarized_df2.head(1))

    sith_data = standarized_df[df['knight'] == 0]
    jedi_data = standarized_df[df['knight'] == 1]
    
    plt.figure(figsize=(12,8 ))
    
    plt.scatter(sith_data['Empowered'].values, sith_data['Stims'].values, 
                color='blue', marker='o', alpha=0.4)
    
    plt.scatter(jedi_data['Empowered'].values, jedi_data['Stims'].values,
                color='red', marker='o', alpha=0.4)
    
    plt.legend(["Sith", "Jedi"], loc='upper left')
    plt.show()

if __name__ == "__main__":
    standarization()
