import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plotData(data, marker, subplot, color="blue"):
    for i in data:
        subplot.scatter(i[0], i[1], i[2], color=color,marker=marker)

def getMean(dat):
    return sum(dat)/len(dat)

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


fig, ((mean, std), (hnr, _)) = plt.subplots(nrows=2, ncols=2)


#ax = fig.add_subplot(projection='3d')
#plotData(lombard, ".", ax, color="blue")
#plotData(plain, ".", ax, color="red")
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

meanLombard = [i[0] for i in lombard]
meanPlain = [i[0] for i in plain]
meanData = [meanLombard, meanPlain]
mean.hist(meanData, label=["Lombard", "Plain"])
mean.legend(prop={'size': 10})
mean.set_title('Mean F0')
mean.axvline(getMean(meanLombard), color='blue', linestyle='dashed', linewidth=1)
mean.axvline(getMean(meanPlain), color='orange', linestyle='dashed', linewidth=1)


stdLombard = [i[1] for i in lombard]
stdPlain = [i[1] for i in plain]
stdData = [stdLombard, stdPlain]
std.hist(stdData, label=["Lombard", "Plain"])
std.legend(prop={'size': 10})
std.set_title('Std F0')
std.axvline(getMean(stdLombard), color='blue', linestyle='dashed', linewidth=1)
std.axvline(getMean(stdPlain), color='orange', linestyle='dashed', linewidth=1)

hnrLombard = [i[2] for i in lombard]
hnrPlain = [i[2] for i in plain]
hnrData = [hnrLombard, hnrPlain]
hnr.hist(hnrData, label=["Lombard", "Plain"])
hnr.legend(prop={'size': 10})
hnr.set_title("HNR")
hnr.axvline(getMean(hnrLombard), color='blue', linestyle='dashed', linewidth=1)
hnr.axvline(getMean(hnrPlain), color='orange', linestyle='dashed', linewidth=1)




fig.tight_layout()
plt.show()
