import pandas as pd
import os
#two files specific columns merge
df = pd.read_excel(r'onek.xlsx')
df1 = pd.read_excel(r'fivek.xlsx')

rank_col1 = df['Rank']
rank_col2 = df1['Rank']

combined_rank = pd.concat([rank_col1,rank_col2], ignore_index = True)

result_df = pd.DataFrame({'Rank' : combined_rank})

output_file = r'D:\Tasks\Side-Side-Date.xlsx'
result_df.to_excel(output_file, index = False)

os.startfile(output_file)