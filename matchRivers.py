#THIS SCRIPT MATCHES THE GPS COORDINATES OF THE REACHS WITH THE PUTINS
import pandas as pd
import os
from tqdm import tqdm
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Getting the current work directory (cwd)
directory = os.getcwd()
#print(directory)
#+'
riverLevels = []

def loadReachIDs():
    for root, dirs, files in os.walk(directory+'\\NWM_parameters'): 
        for file in files:
            #rint(file)
            if file.startswith("reach"):
                filePath = os.path.join(root, file)
                reachInfo = pd.read_csv(filePath)
                #print(reachInfo.head())
                return(reachInfo)
    return

def loadRiverInfo():
    reachInfo = pd.DataFrame()
    for root, dirs, files in os.walk(directory+'\\riverInfo'):
        for file in files:
            #print(file)
            if file.endswith(".csv"):
                filePath = os.path.join(root, file)
                reachInfoSingle = pd.read_csv(filePath)
                reachInfo = pd.concat([reachInfo,reachInfoSingle])
    reachInfo.reset_index(inplace=True)          
    return(reachInfo)

def makeMatches():
    reachInfo = loadReachIDs()
    reachCoords = reachInfo.values.tolist()
    riverInfo = loadRiverInfo()
    #print(riverInfo.head())
    #print(reachInfo.head())
    riverInfo = riverInfo[['Put In','RiverName','RunName']].values.tolist()
    #print(riverInfo[0])
    putInCoords = []
    for info in riverInfo:
        try:
            coord = info[0]
            river = info[1]
            run = info[2]
            lat = float(coord.strip().split(",")[0].replace('[','').replace(']','').replace("'",''))
            lon = float(coord.strip().split(",")[1].replace('[','').replace(']','').replace("'",''))
            putInCoords.append([lat,lon,river,run])
        except:
            pass
            #print(coord)
    riverMatch = []
    for putInCoord in tqdm(putInCoords):
        distance = 999999999
        i = 0
        #temporary code to test before
        for reachCoord in reachCoords:
            # p = putin r = reach
            plat = putInCoord[0]
            plon = putInCoord[1]
            rlat = reachCoord[2]
            rlon = reachCoord[3]
            featureID = reachCoord[1]
            #print(str(plat)+' '+str(plon)+' '+str(lat)+' '+str(rlon))
            #Distance formulat
            newDistance = math.sqrt(math.pow(plat-rlat,2)+math.pow(plon-rlon,2))
            if newDistance < distance:
                distance = newDistance
                river = putInCoord[2]
                run = putInCoord[3]
                match = [int(featureID),river,run]
                #print(distance)
        riverMatch.append(match)
        #print(match)      
    riverMatch = pd.DataFrame(riverMatch,columns = ['feature_id','river','run'])
    riverMatch.to_csv('riverMatches.csv')

makeMatches()
