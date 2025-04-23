import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def histogram_1():
    csv_path = "/home/zpalfi/goinfre/Test_knight.csv"
    

    try:
        data = pd.read_csv(csv_path)

        num_cols = len(data.columns)
        plt.figure(figsize=(20, 20))
        
        for i, col in enumerate(data.columns, 1):
            plt.subplot(6, 5, i)
            sns.histplot(data[col], bins=40, alpha=1, color='#7fbf7f', edgecolor=None)
            plt.title(f"{col}", pad=12)
            plt.xlabel('')
            plt.ylabel('')
            plt.legend(["Knight"], loc='upper right')
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def histogram_2():
    csv_path = "/home/zpalfi/goinfre/Train_knight.csv"

    try:
        data = pd.read_csv(csv_path)

        num_cols = len(data.columns) - 1
        plt.figure(figsize=(20, 20))

        unique_knights = data['knight'].unique()
        palettes = sns.color_palette("coolwarm", len(unique_knights))

        for i, col in enumerate(data.columns, 1):
            if col != 'knight':
                plt.subplot(6, 5, i)
                for idx, knight in enumerate(unique_knights):
                    knight_data = data[data['knight'] == knight]
                    sns.histplot(knight_data[col], bins=40, color=palettes[idx], edgecolor=None, label=knight)
                plt.title(f"{col}", pad=12)
                plt.xlabel('')
                plt.ylabel('')
                plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    histogram_1()
    histogram_2()