import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

def tree():
    csv_file = "../Train_knight.csv"
    csv_file2 = "../Test_knight.csv"

    df_train = pd.read_csv(csv_file)
    df_test = pd.read_csv(csv_file2)

    X = df_train.drop('knight', axis=1)
    y = df_train["knight"]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred_val = model.predict(X_val)

    accuracy = accuracy_score(y_val, y_pred_val)
    print(f"Validation Accuracy: {accuracy:.2f}")
    print(f"Validation Classification Report:\n{classification_report(y_val, y_pred_val)}")
    print(f"Validation Confusion Matrix:\n{confusion_matrix(y_val, y_pred_val)}")

    plt.figure(figsize=(20, 10))
    plot_tree(
        model, 
        filled=True,
        feature_names=X_train.columns,
        class_names=["Sith", "Jedi"],)
    plt.show()

    predictions = model.predict(df_test)
    
    try:
        with open("prediction.txt", "w") as f:
            for pred in predictions:
                f.write(f"{pred}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    tree()