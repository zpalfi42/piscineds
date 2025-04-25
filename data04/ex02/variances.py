import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def variances():
    csv_path = "../Train_knight.csv"

    df = pd.read_csv(csv_path)
    df['knight'] = df['knight'].map({'Sith': 1, 'Jedi': 0})

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    pca = PCA()
    pca.fit(df_scaled)

    variances = pca.explained_variance_ratio_ * 100
    print(variances)

    cum_variances = variances.cumsum()
    print(cum_variances)

    plt.figure(figsize=(10, 6))
    plt.plot(cum_variances, marker='', linestyle='-', color='b')
    plt.show()

if __name__ == "__main__":
    variances()