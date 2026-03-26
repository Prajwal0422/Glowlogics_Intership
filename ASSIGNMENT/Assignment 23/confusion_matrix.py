from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("dataset.csv")

le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df[['Offer','Money','Meeting']]
y = df['Class']

model = CategoricalNB()
model.fit(X,y)

pred = model.predict(X)

cm = confusion_matrix(y,pred)

print("Confusion Matrix:")
print(cm)

print("Accuracy:",accuracy_score(y,pred))
print("Precision:",precision_score(y,pred))
print("Recall:",recall_score(y,pred))