import pandas as pa

s = pa.Series([10, 20, 30, 40, 50])  ### single dimensional array (single row with multiple coloumn)
print(s)

scores = pa.Series([85, 70, 60, 80, 90], index=['Maths','Science','physiscs','biology','English'])
print(scores)
print(f"second index :{s[2]}\n")

filtered = scores[scores > 70]

print(f"print scores greater than 70 : \n{filtered}.sort_values()")
#print(f"print the scores greater than 70 : {scores[scores > 70]}")

print(scores['Science'])

############## Dictinory data ###############

data = {'Monday': 100, 'Tuesday': 200, 'Wednesday': 300}   ### dict structure
sales = pa.Series(data)      ###### converting dict to series
print(f"converting dict to series : \n{sales}\n\n")

#data frame

data1 = {
    'Name': ['Mugil', 'Tamil', 'Sanjeev', 'Agil'],
    'Age': [35, 30, 8, 3],
    'City': ['Chennai', 'Delhi', 'Munbai', 'kolkata'],
}
df = pa.DataFrame(data1)
print(f"converting data to series : \n{df}\n\n")
print(f"print only the name in dict as series : \n{df['Name']}\n\n")
print(f"Printing multiple coloumn in dict as series : \n{df[['Name', 'Age']]}")