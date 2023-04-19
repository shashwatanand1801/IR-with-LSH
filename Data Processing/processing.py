import pandas as pd
import json

df = pd.read_csv("Shakespeare_data.csv")

# print(df.head())

# print(df['Play'].unique())

plays = df['Play'].unique()

print((df['Play'] == plays[0]))

data = {}

print(df['Play'])


# for i in range(40):
#     print(type(df.loc[i, "PlayerLine"]))

count = 1

for play in plays:
    if count == 10:
        break
    count += 1
    idx = 0
    data[play] = ""
    flag = 0
    counter = 0
    for item in df['Play']:
        if(item == play):
            data[item] += '\n'
            data[item] += df.loc[idx, 'PlayerLine']
            flag = 1
            counter += 1
            if counter== 5:
                break
        elif flag:
            break
        idx += 1


print(data)

# jsonData = json.dumps(data)

# print(jsonData)

with open('../data.json', 'w') as fp:
    json.dump(data, fp)