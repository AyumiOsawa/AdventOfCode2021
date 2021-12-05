import pandas as pd
import numpy as np

df = pd.read_csv(
    'data/day3_input.txt',
    delimiter = "\n",
    header = None,
    dtype="str"
    )
dataArray = {0 : 0}
for index, row in df.iterrows():
    location = 0
    for bit in row[0]:
        if (location not in dataArray):
            dataArray[location]  = 0
        if (bit == "1"):
            dataArray[location]  += 1
        else:
            dataArray[location]  -= 1
        location += 1
first_num = ""
second_num = ""
for index in range(len(dataArray)):
    if (dataArray[index] > 0):
        first_num += "1"
        second_num += "0"
    else:
        first_num += "0"
        second_num += "1"
