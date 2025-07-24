import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import datasets

# Wczytanie danych
df = pd.read_csv("iris.csv")
X_data = df.iloc[:, :-1]
y_labels = df.iloc[:, -1]

# PCA z trzema składowymi
pca = PCA(n_components=3)
X_pca_transformed = pca.fit_transform(X_data)

# Wyświetlenie wyjaśnionej wariancji
explained_var_ratio = pca.explained_variance_ratio_
cum_var_ratio = explained_var_ratio.cumsum()
print("Wyjaśniona wariancja dla każdej składowej:", explained_var_ratio)
print("Skumulowana wariancja:", cum_var_ratio)

# Funkcja do obliczania straty informacji
def info_loss(removed_features):
    total_var = sum(explained_var_ratio)
    lost_var = sum(explained_var_ratio[-removed_features:])
    return lost_var / total_var

# Wyświetlenie strat informacji
for i in range(1, 4):
    print(f"Strata informacji po usunięciu {i} składowej: {info_loss(i):.4f}")

# Liczba składowych dla 95% wariancji
num_components_95 = next(idx + 1 for idx, value in enumerate(cum_var_ratio) if value >= 0.95)
print("Minimalna liczba składowych do zachowania 95% wariancji:", num_components_95)

# Definiowanie kolorów dla gatunków
species_colors = {'Setosa': 'blue', 'Versicolor': 'aqua', 'Virginica': 'orange'}
unique_species = df.iloc[:, -1].unique()

# Wizualizacja PCA - 2 składowe
def plot_2d():
    plt.figure()
    for specie in unique_species:
        mask = y_labels == specie
        plt.scatter(X_pca_transformed[mask, 0], X_pca_transformed[mask, 1], color=species_colors[specie], label=specie)
    plt.xlabel('Składowa główna 1')
    plt.ylabel('Składowa główna 2')
    plt.title('PCA - 2 Składowe')
    plt.legend()
    plt.show()

# Wizualizacja PCA - 3 składowe
def plot_3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for specie in unique_species:
        mask = y_labels == specie
        ax.scatter(X_pca_transformed[mask, 0], X_pca_transformed[mask, 1], X_pca_transformed[mask, 2], 
                   color=species_colors[specie], label=specie)
    ax.set_xlabel('Składowa główna 1')
    ax.set_ylabel('Składowa główna 2')
    ax.set_zlabel('Składowa główna 3')
    ax.set_title('PCA - 3 Składowe')
    ax.legend()
    plt.show()

# Wykresy
plot_2d()
# plot_3d()


