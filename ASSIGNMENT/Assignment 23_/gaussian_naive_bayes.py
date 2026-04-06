import pandas as pd
from sklearn.naive_bayes import GaussianNB

# Dataset
data = {
    'Age': [55,60,45,50,48,52],
    'Chol': [250,240,230,220,210,215],
    'BP': [140,150,130,120,125,135],
    'Target': [1,1,1,0,0,0]
}

df = pd.DataFrame(data)

X = df[['Age','Chol','BP']]
y = df['Target']

# Model
model = GaussianNB()
model.fit(X,y)

# New patient
new_patient = [[54,245,138]]

prediction = model.predict(new_patient)

print("Prediction:", "Disease" if prediction[0]==1 else "No Disease")