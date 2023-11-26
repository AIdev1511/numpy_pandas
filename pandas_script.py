import pandas as pd

columnn  = ['Mariya', 'Batman', 'Spongebob']

titled_columns = {'name' : columnn,
                 'height': [1.67, 1.9, 0.25],
                 'weight': [54, 100, 1]}
data = pd.DataFrame(titled_columns)

data.to_csv('bmi.csv', index = False, sep = "\t")

print(data)