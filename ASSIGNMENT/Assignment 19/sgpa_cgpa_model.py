import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("sgpa_data.csv")

print(df.describe())

X = df[["SGPA","CGPA"]]
y = df["Result"]

# Accuracy Test 1
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Accuracy Test 1:",accuracy_score(y_test,pred))

# Accuracy Test 2 (different split)
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=10
)

model.fit(X_train,y_train)
pred = model.predict(X_test)

print("Accuracy Test 2:",accuracy_score(y_test,pred))