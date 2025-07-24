import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

iris = load_iris()
X = iris.data
y = iris.target

# podział na zbiór testowy i treningowy 70% /30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=50)

def drzewoDecyzyjne (X_train, X_test, y_train, y_test):
    # Tworzenie drzewa decyzyjnego
    clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42) # criterion="gini" - 

    # Uczenie drzewa
    clf.fit(X_train, y_train)

    # Tworzenie wizualizacji drzewa
    plt.figure(figsize=(12,8))
    tree.plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
    plt.show()

    # Obliczanie predykcji
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Dokładność klasyfikatora: {accuracy:.2f}')

    # Obliczenie macierzy błędów
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Wyświetlenie macierzy błędów w formie tabeli
    macierz_bledu = confusion_matrix(y_test, y_pred)
    sns.heatmap(macierz_bledu, annot=True, cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.xlabel("Przewidywane")
    plt.ylabel("Rzeczywiste")
    plt.title(f"Macierz błędu dla DD")
    plt.show()

    # Wizualizacja macierzy błędów
    disp = ConfusionMatrixDisplay(conf_matrix, display_labels=iris.target_names)
    disp.plot(cmap='Blues')


def main():
    drzewoDecyzyjne(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()