import pandas as pd

df = pd.read_csv('iris_with_errors.csv')

# Podpunkt a
def check_what_is_missing():
    missing_values = df.isnull().sum()

    print("Brakujące wartości w każdej kolumnie:")
    print(missing_values)

# Podpunkt b
def correct_outliers(column):
    mean_value = df[column].mean()
    df[column] = df[column].apply(lambda x: mean_value if (x < 0 or x > 15) else x)

def change_num():
    numeric_columns = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
        correct_outliers(column)
        print(f'Change numer in {column}')

# Podpunkt c
valid_varieties = ['Setosa', 'Versicolor', 'Virginica']
def correct_variety(value):
    if value not in valid_varieties:
        return 'Unknown'  # Możesz zastosować inną metodę, np. przypisać najbliższy poprawny gatunek
    return value

df['variety'] = df['variety'].apply(correct_variety)

check_what_is_missing()
change_num()

print("\nUnikalne wartości w kolumnie 'variety' po poprawkach:")
print(df['variety'].unique())




