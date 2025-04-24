import matplotlib.pyplot as plt

def confusion_matrix():
    print("Confusion Matrix")
    pred_path = "../predictions.txt"
    truth_path = "../truth.txt"

    with open(pred_path, "r") as f:
        pred = [line.strip() for line in f.readlines()]
    with open(truth_path, "r") as f:
        truth = [line.strip() for line in f.readlines()]

    matrix = [[0, 0], [0, 0]]
    for i in range(len(pred)):
        if pred[i] == "Jedi" and truth[i] == "Jedi":
            matrix[0][0] += 1
        elif pred[i] == "Jedi" and truth[i] == "Sith":
            matrix[1][0] += 1
        elif pred[i] == "Sith" and truth[i] == "Jedi":
            matrix[0][1] += 1
        elif pred[i] == "Sith" and truth[i] == "Sith":
            matrix[1][1] += 1

    print("\tprecision\trecall\t\tf1-1score\ttotal\n")
    print(f"Jedi\t{matrix[0][0] / (matrix[0][0] + matrix[1][0]):.2f}\t\t{matrix[0][0] / (matrix[0][0] + matrix[0][1]):.2f}\t\t{2 * matrix[0][0] / (2 * matrix[0][0] + matrix[1][0] + matrix[0][1]):.2f}\t\t{matrix[0][0] + matrix[0][1]}")
    print(f"Sith\t{matrix[1][1] / (matrix[1][1] + matrix[0][1]):.2f}\t\t{matrix[1][1] / (matrix[1][1] + matrix[1][0]):.2f}\t\t{2 * matrix[1][1] / (2 * matrix[1][1] + matrix[1][0] + matrix[0][1]):.2f}\t\t{matrix[1][1] + matrix[1][0]}")
    print(f"\naccuracy\t\t\t\t{(matrix[0][0] + matrix[1][1]) / (matrix[0][0] + matrix[1][1] + matrix[0][1] + matrix[1][0]):.2f}\t\t{matrix[0][0] + matrix[0][1] + matrix[1][1] + matrix[1][0]}\n")

    print(f"[{matrix[0]}\n {matrix[1]}]")

    # Plotting the confusion matrix
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