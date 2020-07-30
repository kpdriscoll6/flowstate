import pandas as pd
import os
from tqdm import tqdm
import numpy as np

directory = os.getcwd()

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
    riverInfo.columns = cols
    riverInfo = riverInfo.assign(featureID=np.nan)

    #print(riverInfo.head())

    #turn riverMatches to a list for easier iterating
    riverMatches = riverMatches.values.tolist()

    for riverMatch in tqdm(riverMatches):
        try:
            #Wrap this in a try block because of unbalanced parentheses. Could probably fix this but I'm bad a regex
            run = riverMatch[3]
            featureID = riverMatch[1]
            featureInsert = riverInfo[riverInfo['RunName'].str.match(run)]
            featureInsert['featureID'] = featureID
            riverInfo[riverInfo['RunName'].str.match(run)] = featureInsert
        except:
            pass
    #drop NA 
    riverInfo.dropna(inplace=True)
    #save to CSV as bacup
    riverInfo.to_csv('riverInfoDB.csv')
    print(riverInfo.head())
buildRiverTable()