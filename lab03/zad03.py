import pandas as pd
from zad02 import drzewoDecyzyjne
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

# podział na zbiór testowy i treningowy 70% /30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=50)

def nn (X_train, X_test, y_train, y_test, k):
    # Klasyfikator k-NN dla k=3
    knn3 = KNeighborsClassifier(n_neighbors=k)
    knn3.fit(X_train, y_train)

    # Predykcja na zbiorze testowym
    y_pred = knn3.predict(X_test)

    # Obliczenie dokładności
    dokladnosc = accuracy_score(y_test, y_pred)
    print(f'Dokładność dla k={k}: {dokladnosc:.2f}')

    # Macierz błędu
    macierz_bledu = confusion_matrix(y_test, y_pred)
    sns.heatmap(macierz_bledu, annot=True, cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.xlabel("Przewidywane")
    plt.ylabel("Rzeczywiste")
    plt.title(f"Macierz błędu dla k={k}")
    plt.show()



def nb (X_train, X_test, y_train, y_test):
    # Klasyfikator Naive Bayes
    nb_classifier = GaussianNB()
    nb_classifier.fit(X_train, y_train)

    # Predykcja na zbiorze testowym
    y_pred = nb_classifier.predict(X_test)

    # Obliczenie dokładności
    dokladnosc = accuracy_score(y_test, y_pred)
    print(f'Dokładność dla Naive Bayes: {dokladnosc:.2f}')

    # Macierz błędu
    macierz_bledu = confusion_matrix(y_test, y_pred)
    sns.heatmap(macierz_bledu, annot=True, cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.xlabel("Przewidywane")
    plt.ylabel("Rzeczywiste")
    plt.title(f"Macierz błędu dla NB")
    plt.show()

def main():
    print("DD:")
    drzewoDecyzyjne(X_train, X_test, y_train, y_test)
    print("\n")

    print("NN3:")
    nn(X_train, X_test, y_train, y_test, 3)
    print("\n")

    print("NN5:")
    nn(X_train, X_test, y_train, y_test, 5)
    print("\n")

    print("NN11:")
    nn(X_train, X_test, y_train, y_test, 11)
    print("\n")

    print("NB:")
    nb(X_train, X_test, y_train, y_test)
    print("\n")

if __name__ == "__main__":
    main()
