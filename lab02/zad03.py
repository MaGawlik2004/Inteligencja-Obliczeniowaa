import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Wczytanie danych irysów
irises = datasets.load_iris()  # Poprawiona nazwa zmiennej
df = pd.DataFrame(data=irises.data, columns=irises.feature_names)
df['species'] = irises.target

# Przypisanie nazw gatunków
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Wybór zmiennych do analizy
x_col, y_col = 'sepal length (cm)', 'sepal width (cm)'

# Normalizacja min-max
min_max_scaler = MinMaxScaler()
df_minmax = df.copy()
df_minmax[[x_col, y_col]] = min_max_scaler.fit_transform(df[[x_col, y_col]])

# Normalizacja z-score
zscore_scaler = StandardScaler()
df_zscore = df.copy()
df_zscore[[x_col, y_col]] = zscore_scaler.fit_transform(df[[x_col, y_col]])

# Funkcja do rysowania wykresów
def plot_iris(df, title, ax):
    sns.scatterplot(
        data=df, x=x_col, y=y_col, hue='species', ax=ax
    )
    ax.set_title(title)
    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Sepal Width')

# Tworzenie wykresów
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
plot_iris(df, "Original Dataset", axes[0])
plot_iris(df_zscore, "Z-Core Scaled Dataset", axes[1])
plot_iris(df_minmax, "Min-Max Normalised Dataset", axes[2])

plt.tight_layout()
plt.show()
