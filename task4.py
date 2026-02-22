#  open directly XLSX file 
import pandas as pd
import os
# Load the first Excel file
df1 = pd.read_excel(r'D:\Tasks\onek.xlsx')
# Save the modified DataFrames to a new Excel file if needed
df1.to_excel(r'D:\Tasks\modified_onek.xlsx', index=False)
# Open the modified Excel files
os.startfile(r'D:\Tasks\modified_onek.xlsx')
#os.startfile(r'D:\Tasks\modified_fivek.xlsx')

