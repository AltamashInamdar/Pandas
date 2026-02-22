# two file open in a at time
import pandas as pd
df1 = pd.read_excel('D:\\Tasks\\onek.xlsx')
df2 = pd.read_excel('D:\\Tasks\\fivek.xlsx')
print("Contents of onek.xlsx:")
print(df1)
print("\nContents of fivek.xlsx:")
print(df2)