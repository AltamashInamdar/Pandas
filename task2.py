# only show in data name and age
import pandas as pd
df = pd.read_excel('D:\Tasks\student.xlsx')
print(df['name',], df['age'])
