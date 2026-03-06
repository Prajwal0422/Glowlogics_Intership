import pandas as pd

def save_excel(data):

    df = pd.DataFrame([data])

    df.to_excel("students.xlsx",index=False)

    print("Data saved to Excel")
    print(df)