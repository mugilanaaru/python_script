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