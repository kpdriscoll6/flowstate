#THIS SCRIPT JUST PLOTS THE DATA FOR EASY VISUALIZATION
import xarray as xr
import pandas as pd
import os
from tqdm import tqdm

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Getting the current work directory (cwd)
directory = os.getcwd()+'\\medium\\'
#print(directory)

riverLevels = []

# r=root, d=directories, f = files
for root, dirs, files in os.walk(directory): 
    for file in tqdm(files):
        if file.endswith(".nc"):
            #print(os.path.join(root, file))
            filePath = os.path.join(root, file)
            ds = xr.open_dataset(filePath)
            df = ds.to_dataframe()
            #reset the index so the feature ID becomes a column
            df.reset_index(inplace = True)
            #that feature ID is the poudre
            flow = df.loc[df['feature_id'] == 6269342]
            time =  df.loc[df['feature_id'] == 6269342].time.values[0]
            referenceTime = df.loc[df['feature_id'] == 6269342].reference_time.values[0]
            #print(float(test.streamflow)) #M^3/SEC
            riverLevels.append(float(flow.streamflow*35.31485))
            print(float(flow.streamflow*35.31485))
            print(referenceTime)
            print(time)

# data
#print(len(riverLevels))
#print(len(range(1,len(riverLevels)+1)))
df=pd.DataFrame({'x': range(1,len(riverLevels)+1), 'y': riverLevels })
 
# plot
plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
plt.show()
6269342