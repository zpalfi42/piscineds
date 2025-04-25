import matplotlib.pyplot as plt

def confusion_matrix():
    print("Confusion Matrix")
    pred_path = "../ex05/prediction.txt"
    truth_path = "../truth.txt"

    with open(pred_path, "r") as f:
        pred = [line.strip() for line in f.readlines()]
    with open(truth_path, "r") as f:
        truth = [line.strip() for line in f.readlines()]

    matrix = [[0, 0], [0, 0]]
    for i in range(len(truth)):
        if pred[i] == "Jedi" and truth[i] == "Jedi":
            matrix[0][0] += 1
        elif pred[i] == "Jedi" and truth[i] == "Sith":
            matrix[1][0] += 1
        elif pred[i] == "Sith" and truth[i] == "Jedi":
            matrix[0][1] += 1
        elif pred[i] == "Sith" and truth[i] == "Sith":
            matrix[1][1] += 1

    # Precision: Positivos bien / (Positivos bien + Positivos mal) | Que porcentaje de los positivos predichos han sido correctos
    precision_1 = matrix[0][0] / (matrix[0][0] + matrix[1][0])
    precision_2 = matrix[1][1] / (matrix[1][1] + matrix[0][1])

    # Recall: Positivos bien / (Positivos bien + Negativos mal) | Que porcentaje de los positivos reales han sido predichos correctamente
    recall_1 = matrix[0][0] / (matrix[0][0] + matrix[0][1])
    recall_2 = matrix[1][1] / (matrix[1][1] + matrix[1][0])

    # F1-Score: 2 * Precision * Recall / (Precision + Recall) | La media entre la precision y el recall
    f1_score_1 = 2 * precision_1 * recall_1 / (precision_1 + recall_1)
    f1_score_2 = 2 * precision_2 * recall_2 / (precision_2 + recall_2)

    # Accuracy: (Positivos bien + Negativos bien) / (Total de ejemplos) | Que porcentaje de los ejemplos han sido predichos correctamente
    accuracy = (matrix[0][0] + matrix[1][1]) / (matrix[0][0] + matrix[1][1] + matrix[0][1] + matrix[1][0])


    print("\tprecision\trecall\t\tf1-score\ttotal\n")
    print(f"Jedi\t{precision_1:.2f}\t\t{recall_1:.2f}\t\t{f1_score_1:.2f}\t\t{matrix[0][0] + matrix[0][1]}")
    print(f"Sith\t{precision_2:.2f}\t\t{recall_2:.2f}\t\t{f1_score_2:.2f}\t\t{matrix[1][1] + matrix[1][0]}")
    print(f"\naccuracy\t\t\t\t{accuracy:.2f}\t\t{matrix[0][0] + matrix[0][1] + matrix[1][1] + matrix[1][0]}\n")
    print(f"[{matrix[0]}\n {matrix[1]}]")

    fig, ax = plt.subplots()
    cax = ax.matshow(matrix, cmap='YlGnBu_r')

    plt.colorbar(cax)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(['0', '1'])
    ax.set_yticklabels(['0', '1'])
    ax.xaxis.set_ticks_position('bottom')
    count = 0
    for i in range(2):
        for j in range(2):
            count += 1
            if count < 4:
                ax.text(j, i, str(matrix[i][j]), va='center', ha='center', color='black')
            else:
                ax.text(j, i, str(matrix[i][j]), va='center', ha='center', color='white')
    plt.xlabel('')
    plt.ylabel('')
    plt.title('')
    plt.show()

            
if __name__ == "__main__":
    confusion_matrix()