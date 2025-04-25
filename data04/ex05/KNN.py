import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def knn():
    csv_path = "../Train_knight.csv"
    csv_path2 = "../Test_knight.csv"

    df_train = pd.read_csv(csv_path)
    df_test = pd.read_csv(csv_path2)
    X = df_train.drop('knight', axis=1)
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    df_test = scaler.transform(df_test)

    y = df_train["knight"]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    k_values = range(1, 31)
    accuracies = []

    for i in k_values:
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        accuracies.append(accuracy_score(y_val, y_pred))

    model = KNeighborsClassifier(n_neighbors=10)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    print(f"Validation Classification Report:\n{classification_report(y_val, y_pred)}")
    print(f"Validation Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")

    plt.figure(figsize=(10, 6))
    plt.plot(k_values, accuracies)
    plt.show()

    predictions = model.predict(df_test)
    try:
        with open("prediction.txt", "w") as f:
            for pred in predictions:
                f.write(f"{pred}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    knn()
