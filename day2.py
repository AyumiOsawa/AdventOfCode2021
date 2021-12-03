import pandas as pd

def up (data, current):
    newCurrent = current.copy()
    newCurrent['y'] -= data['unit']
    return newCurrent

def down (data, current):
    newCurrent = current.copy()
    newCurrent['y'] += data['unit']
    return newCurrent

def forward (data, current):
    newCurrent = current.copy()
    newCurrent['x'] += data['unit']
    return newCurrent

def navigate (data, current):
    if (data['axis'] == axis['DOWN']):
        return down(data, current)
    elif (data['axis'] == axis['FORWARD']):
        return forward(data, current)
    elif (data['axis'] == axis['UP']):
        return up(data, current)

df = pd.read_csv(
    'data/day2_input.txt',
     delimiter = "\n",
     header = None
    )
dataArray = []
for index, row in df.iterrows():
    data = row[0].split()
    dataArray.append({
        'axis': data[0],
        'unit': int(data[1])
    })

current = { 'x': 0, 'y': 0 }
axis = {
    'DOWN': 'down',
    'FORWARD': 'forward',
    'UP': 'up'
}
for data in dataArray:
    current = navigate(data, current)

print(current['x'] * current['y'])
