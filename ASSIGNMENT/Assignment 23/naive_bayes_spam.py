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

# New email prediction
new = [[1,1,0]]   # Yes Yes No
pred = model.predict(new)

print("Prediction:", "Spam" if pred[0]==1 else "Not Spam")