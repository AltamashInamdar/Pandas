import pandas as pd
import os

#drop duplicates values in columns 
df = pd.read_excel(r'D:\Tasks\date.xlsx')

df_cleaned = df.drop_duplicates(subset = ['Country'])

output_file = r'D:\Tasks\date.xlsx'
df_cleaned.to_excel(output_file, index = False)

os.startfile(output_file)