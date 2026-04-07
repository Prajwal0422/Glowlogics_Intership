import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.svm import SVC

# Load data
df = pd.read_csv("student_data.csv")

# Encode result
le = LabelEncoder()
df['Result'] = le.fit_transform(df['Result'])

X = df[['StudyHours','Attendance']]
y = df['Result']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ======================
# 1. Naive Bayes (Categorical approx)
# ======================
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)

print("Naive Bayes Prediction:", nb_pred)

# ======================
# 2. Gaussian Naive Bayes
# ======================
gnb_model = GaussianNB()
gnb_model.fit(X_train, y_train)
gnb_pred = gnb_model.predict(X_test)

print("Gaussian Prediction:", gnb_pred)

# ======================
# 3. SVM
# ======================
svm_model = SVC()
svm_model.fit(X_train, y_train)
svm_pred = svm_model.predict(X_test)

print("SVM Prediction:", svm_pred)