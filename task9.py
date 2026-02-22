import pandas as pd
import os

#sorting file 
df = pd.read_excel(r'D:\Tasks\date.xlsx')

df_sorted = df.sort_values(by =['Company','Salary'], ascending = [False, True])

output_file = r'D:\Tasks\Sorted.xlsx'
df_sorted.to_excel(output_file, index = False)

os.startfile(output_file)