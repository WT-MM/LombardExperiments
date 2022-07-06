import pandas as pd
import matplotlib.pyplot as plt

def plotData(data, marker, subplot, color="blue"):
    for i in data:
        subplot.scatter(i[0], i[1], i[2], color=color,marker=marker)

df = pd.read_csv("processed_results.csv")

listed = df.values.tolist()

lombard = []

plain = []

for i in listed:
    if i[0].split("_")[1] == "p":
        plain.append(i[1:])
    elif i[0].split("_")[1] == "l":
        lombard.append(i[1:])
    else:
        print(i)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')


plotData(lombard, ".", ax, color="blue")
plotData(plain, ".", ax, color="red")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
