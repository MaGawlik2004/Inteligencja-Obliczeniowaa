import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('iris.csv')

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]

test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

# print(train_set[train_set[:, 4].argsort()], "\n")

def classify_iris(sl, sw, pl, pw):
    if sl < 5.5 or 3.8 < sw or 1 < pl < 1.9 or 0.1 < pw < 0.6 or (sl < 5.8 and 3.2 < sw < 4.4):
        return ("Setosa")
    elif 7 <= sl < 7.9 or 5.1 < pl or 1.8 < pw or (5.8 < sl < 7.9 and 2.2 < sw < 3.8 and 4.5 < pl < 6.9 and 1.4 < pw < 2.5):
        return ("Virginica")
    else:
        return ("Versicolor")


good_predictions = 0
len = test_set.shape[0]

for i in range(len):
    if classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]) == test_set[i][4]:
        good_predictions = good_predictions + 1

# print(good_predictions)
print(good_predictions/len*100, "%")

    
