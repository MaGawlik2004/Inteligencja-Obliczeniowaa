from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def mlpFunc(hidden_layer):
    iris = load_iris()
    X = iris.data
    y = iris.target

    # podział na zbiór testowy i treningowy 70% /30%
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    mlp = MLPClassifier(hidden_layer_sizes=hidden_layer, max_iter=1500, random_state=50 )
    mlp.fit(X_train, y_train)

    y_pred = mlp.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"{accuracy:.2f}")

def main():
    print("Przykład 1: Siatka z 2 hidden layers")
    mlpFunc((2, ))
    print("\nPrzykład 2: Siatka z 3 hidden layers")
    mlpFunc((3, ))
    print("\nPrzykład 3: Siatka z 3 i 3 hidden layers")
    mlpFunc((3, 3))



if __name__ == "__main__":
    main()
