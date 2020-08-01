import pandas as pd
import os
from tqdm import tqdm
import numpy as np
import netCDF4
import xarray as xr

directory = os.getcwd()

def backCheckGPS(featureID):
    filePath = os.getcwd()+ '\\NWM_parameters\\RouteLink_NHDPLUS.nc'
    nc = netCDF4.Dataset(filePath, mode='r')
    ds = xr.open_dataset(filePath)
    df = ds.to_dataframe()
    #print(df.head())
    df.reset_index(inplace = True)
    #print(df.head())
    ##FOR SOME REASON THE INDEX RESET SHIFTS THE FEATURE ID IN THE LINK COLUMN (MAYBE XARRAY ISSUE)
    ##going to rename columns to account for it
    df = df.filter(['link','NHDWaterbodyComID','lat','lon'], axis=1)
    df = df.loc[df['link']==featureID]
    return df
 

def loadMatches():
    for root, dirs, files in os.walk(directory): 
        for file in files:
            if file.startswith('riverMatches'):
                filePath = os.path.join(root, file)
                riverMatches = pd.read_csv(filePath)
                #print(reachInfo.head())
                return(riverMatches)
def loadRiverInfo():
    riverInfo = pd.DataFrame()
    for root, dirs, files in os.walk(directory+'\\riverInfo'): 
        for file in files:
            if file.endswith('.csv'):
                filePath = os.path.join(root, file)
                singleRiverInfo = pd.read_csv(filePath)
                riverInfo = pd.concat([riverInfo,singleRiverInfo])
    return(riverInfo)
    
def buildRiverTable():
    riverMatches = loadMatches()
    #run = riverMatches.iloc[0,3]
    #do some data cleaning here (drop NA) then add NA's to featureId
    riverInfo = loadRiverInfo()
    riverInfo.dropna(inplace=True)
    cols = list(riverInfo.columns)
    cols[0] = 'featureID'
    cols.append('nameNWM')
    cols.append('distance')
    riverInfo = riverInfo.reindex(columns = cols)
    riverInfo = riverInfo.assign(featureID=np.nan)
    #print(riverInfo.head())

    #turn riverMatches to a list for easier iterating
    riverMatches = riverMatches.values.tolist()

    for riverMatch in tqdm(riverMatches):
        try:
            #Wrap this in a try block because of unbalanced parentheses. Could probably fix this but I'm bad a regex
            run = riverMatch[3]
            featureID = riverMatch[1]
            nameNWM = riverMatch[4]
            distance = riverMatch[5]
            featureInsert = riverInfo[riverInfo['RunName'].str.match(run)]
            featureInsert['featureID'] = featureID
            featureInsert['nameNWM'] = nameNWM
            featureInsert['distance']  =distance
            riverInfo[riverInfo['RunName'].str.match(run)] = featureInsert
            #print("added the river info")
        except:
            pass
    #drop NA 
    riverInfo.dropna(inplace=True)
    #save to CSV as bacup
    riverInfo.to_csv('riverInfoDB.csv')
    print(riverInfo.head())


#buildRiverTable()

db = riverMatches = pd.read_csv('C:\\Users\\Kevin\\Desktop\\flowStateV2\\riverInfoDB.csv')

#NEED TO FIGURE OUT HOW TO DROP REPEATED VALUES BUT KEET THE FIRST(DUPLICATED PANDAS)
#print(db.head())
print(len(db['featureID'].unique()))
print(len(db['featureID']))
print(db['RunName'].nunique())
print(len(db['RunName']))
print(db['featureID'].unique())
print(db.loc[db.duplicated(subset = 'RunName')]['RunName'])