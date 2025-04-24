import pandas as pd
import matplotlib.pyplot as plt

def heatmap():
    csv_file = "../Train_knight.csv"

    df = pd.read_csv(csv_file)
    df['knight'] = df['knight'].map({'Sith': 0, 'Jedi': 1})


    co_mtx = df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    cax = ax.matshow(co_mtx, cmap='hot')
    plt.colorbar(cax)
    ax.set_xticks(range(len(co_mtx.columns)))
    ax.set_yticks(range(len(co_mtx.columns)))
    ax.set_xticklabels(co_mtx.columns, rotation=90)
    ax.set_yticklabels(co_mtx.columns)
    ax.xaxis.set_ticks_position('bottom')
    plt.show()

if __name__ == "__main__":
    heatmap()