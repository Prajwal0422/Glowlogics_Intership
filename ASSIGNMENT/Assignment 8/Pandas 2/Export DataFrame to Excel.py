import pandas as pd

info_marks = pd.DataFrame({
    'name':['Parker','Smith','William','Terry'],
    'Maths':[78,84,67,72],
    'Science':[89,92,61,77],
    'English':[72,75,64,82]
})

info_marks.to_excel("output.xlsx", index=False)

print("DataFrame exported successfully.")