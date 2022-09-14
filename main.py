#%%
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# gdLogAddr = sys.argv[1]

gdLogAddr = "gdLog_220825_113829.csv";

rootAddr = "root_220825_113829.txt"

data = pd.read_csv(gdLogAddr)
rootLog = open(rootAddr,"r")
#test = rootLog.readline(2)

for i in range(5):
    test = rootLog.readline(i)
    print(test)

#print(data.shape)
#print(data.gimbalRpy_deg_0)

time = data.rosTime - data.rosTime[0]

plt.plot(time,data.gimbalRpy_deg_0)
plt.plot(time,data["gimbalRpy_deg_1"])
plt.xlabel("time [s]")
plt.ylabel("degree [deg]")

rpy_0 = data["rpy_deg_0"]
rpy_1 = data["rpy_deg_1"]
rpy_2 = data["rpy_deg_2"]

inspectThis = [rpy_0,rpy_1,rpy_2]
thresholdList = [1,2,1]

recordList = np.zeros([len(inspectThis),len(data)])

# Check abnormality
for i in range(len(data)):
    for dat in range(len(inspectThis)):
        if inspectThis[dat][i] >= thresholdList[dat]:
            recordList[dat][i] = 1

plt.figure(2)
plt.plot(time,recordList[0])
plt.plot(time,recordList[1])
plt.plot(time,recordList[2])

# %%