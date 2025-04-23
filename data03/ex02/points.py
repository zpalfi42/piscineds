import pandas as pd
import matplotlib.pyplot as plt

def points():
    csv_path = "/home/zpalfi/goinfre/Train_knight.csv"
    csv_path2 = "/home/zpalfi/goinfre/Test_knight.csv"

    df = pd.read_csv(csv_path)
    df2 = pd.read_csv(csv_path2)
    df['knight'] = df['knight'].map({'Sith': 0, 'Jedi': 1})

    colors = df['knight'].map({0: 'blue', 1: 'red'})

    plt.figure(figsize=(8, 12))
    plt.subplot(2,1,1)
    plt.scatter(df['Empowered'].values, df['Stims'].values, 
                c=colors, marker='o', alpha=0.4)
    plt.subplot(2,1,2)
    plt.scatter(df2['Empowered'].values, df2['Stims'].values,
                c='green', marker='o', alpha=0.4)
    plt.show()
    
    plt.figure(figsize=(8, 12))
    plt.subplot(2,1,1)
    plt.scatter(df['Push'].values, df['Deflection'].values, 
                c=colors, marker='o', alpha=0.4)
    plt.subplot(2,1,2)
    plt.scatter(df2['Push'].values, df2['Deflection'].values,
                c='green', marker='o', alpha=0.4)
    plt.show()

if __name__ == "__main__":
    points()