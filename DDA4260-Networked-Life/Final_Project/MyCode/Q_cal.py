import numpy as np
import pandas as pd
import collections
TrainData_file = "selected_user_data_modified.csv"
# TrainData = pd.read_table(TrainData_file, sep='\t', header=None)
TrainData = pd.read_csv(TrainData_file, header=None)
TrainData[5] = ''
a = []
for i in range(len(TrainData)):
# for i in range(10):
    t_click = 0
    for item in str(TrainData[4][i]).split(';'):
        visit_info = item.split(':')
        t_click += int(visit_info[1])
    Q = 1/(1+np.exp(-t_click))
    a.append(Q)
TrainData[5] = a
TrainData.to_csv('data.csv',index=False)
print(TrainData)