import os
import pandas as pd
import numpy as np

path = "/Users/mac/Desktop/repos/codecartography/ExampleFile.py"

##Open .py file and read line by line
with open (path) as f:
    content = f.readlines()

print(content)

lines = []

for line in content:
    x = line.replace('  ', 'TAB')
    lines.append(x)


parents = []
children = []
items = []
values = []

for line in lines:

    counter = 0
    temp = []

    if ("#" in line):
        continue

    if ('TAB' not in line):
        parents.append("NA")
        items.append(line)
        values.append(line)

        for x in lines:

            print(x)
            if lines.index(x) <= lines.index(line): 
                
                continue

            print(x)
            if ('TAB' in x):

                temp.append(x)

            else:
                break

        children.append(temp)


    

    




df = pd.DataFrame(columns=['Item', 'Parent', 'Children', 'Value'])

data = pd.DataFrame({'Item': items, 'Parent': parents, 'Children': children, 'Value': values})

df = df.append(data)

pd.set_option("display.max_rows", None, "display.max_columns", None)


print(df)

df.to_csv("/Users/mac/Desktop/repos/codecartography/output.csv")


##how to structure this dataframe


#Item Parent Children Value

