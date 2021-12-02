import pandas as pd

df = pd.read_csv(
    'data/day1_input.txt',
    delimiter = "\n",
    header = None
    )
dataArray = []
for index, row in df.iterrows():
    dataArray.append(row[0])

counter = 0
for index, depth in enumerate(dataArray):
    if (index == 0):
        continue
    prevDepth = dataArray[index - 1]
    if depth - prevDepth > 0:
        counter += 1

print(counter)
