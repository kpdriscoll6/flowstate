#THIS SCRIPT MATCHES THE GPS COORDINATES OF THE REACHS WITH THE PUTINS
import pandas as pd
import os
from tqdm import tqdm
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from difflib import SequenceMatcher


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

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
                #dropNA only want values that have names
                reachInfo.dropna(inplace=True)
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
    #don't know if I really want to do this but leaving it in for now to speed things up
    reachInfo.reset_index(inplace=True)          
    return(reachInfo)

def makeMatches():
    reachInfo = loadReachIDs()
    reachCoords = reachInfo.values.tolist()
    riverInfo = loadRiverInfo()
    print(riverInfo.head())
    print(reachInfo.head())
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
        newReachName = ''
        for reachCoord in reachCoords:
            # p = putin r = reach
            plat = float(putInCoord[0])
            plon = float(putInCoord[1])
            rlat = float(reachCoord[3])
            rlon = float(reachCoord[4])
            featureID = reachCoord[1]
            river = putInCoord[2]
            run = putInCoord[3]
            #print('coords: '+str(plat)+' '+str(plon)+' '+str(rlat)+' '+str(rlon))
            #Distance formula
            newDistance = math.sqrt(math.pow(plat-rlat,2)+math.pow(plon-rlon,2))
            #if the distance is less and the name similarity is greater than or equal --> replace
            if newDistance < distance and similarity(reachCoord[5],river)>=similarity(newReachName,river):
                distance = newDistance
                #save the new reachName
                newReachName = reachCoord[5]
                match = [int(featureID),river,run,newReachName]
        #print(match)
        riverMatch.append(match)   
    riverMatch = pd.DataFrame(riverMatch,columns = ['feature_id','river','run','riverNWM'])
    riverMatch.to_csv('riverMatches.csv')

makeMatches()
