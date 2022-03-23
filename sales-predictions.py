import pandas as pd

filename = '/Users/ollign/Desktop/Projects/pythonProject/Coding_Dojo/Pandas/sales-predictions/sales_predictions.csv'

df = pd.read_csv(filename)

print(df.head())