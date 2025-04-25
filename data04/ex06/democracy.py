import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

def democracy():
    csv_path = "../Train_knight.csv"
    csv_path2 = "../Test_knight.csv"

    df_train = pd.read_csv(csv_path)
    df_test = pd.read_csv(csv_path2)

    X = df_train.drop('knight', axis=1)
    y = df_train["knight"]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    df_test = scaler.transform(df_test)

    
    logistic = LogisticRegression(max_iter=1000, random_state=42)
    decision_tree = DecisionTreeClassifier(random_state=42)
    knn = KNeighborsClassifier(n_neighbors=10)

    voting = VotingClassifier(estimators=[
        ('logistic', logistic),
        ('decision_tree', decision_tree),
        ('knn', knn)
    ], voting='hard')

    voting.fit(X_train, y_train)

    y_pred = voting.predict(X_val)

    print(f"Validation Classification Report:\n{classification_report(y_val, y_pred)}")
    print(f"Validation Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")

    predictions = voting.predict(df_test)
    try:
        with open("prediction.txt", "w") as f:
            for pred in predictions:
                f.write(f"{pred}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
    


if __name__ == "__main__":
    democracy()