import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./diabetes.csv")
X = df.drop(columns='class')
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(6, 3), activation="relu", max_iter=500, random_state=50 )
mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"{accuracy:.2f}")

# Macierz błędu
macierz_bledu = confusion_matrix(y_test, y_pred)
labels = y.unique()
sns.heatmap(macierz_bledu, annot=True, cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.xlabel("Przewidywane")
plt.ylabel("Rzeczywiste")
plt.title(f"Macierz błędu")
plt.show()