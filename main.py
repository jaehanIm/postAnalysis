#%%
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# gdLogAddr = sys.argv[1]

gdLogAddr = "/data/220902/220901_142123/gdLog_220901_142123.csv";
data = pd.read_csv(gdLogAddr)

print(data.shape)
print(data.gimbalRpy_deg_0)

plt.plot(data.gimbalRpy_deg_0)
plt.plot(data["gimbalRpy_deg_1"])



# %%
