import pandas as pd                    #### importing pandas as pd alias
df = pd.read_csv('sample.csv')         #### reading csv file trough pandas call the alias pd.
print(f"printing output through a csv file : \n{df}\n\n")
print(f"printing the top two coloumns : \n{df.head(2)}\n\n")
print(f"printing the last two coloumns : \n{df.tail(2)}\n\n")
print(f"printing the total number of rows and coloumns : \n{df.shape}\n\n")