# 5)two file marged in one create a new file and two file data merged 
import pandas as pd
import os

#merge two excel files

df1 = pd.read_excel(r'D:\Tasks\onek.xlsx')

df2 = pd.read_excel(r'D:\Tasks\fivek.xlsx')

merged_df = pd.concat([df1, df2], ignore_index=True)

output_file = r'D:\Tasks\merged_file.xlsx'
merged_df.to_excel(output_file, index=False)

os.startfile(output_file)