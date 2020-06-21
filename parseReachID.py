import netCDF4
import pandas as pd
import os
import xarray as xr
import shapefile
import wget


def parseID():
    #This function saves a CSV of the GPS coords of each Reach ID
    directory = os.getcwd()+'\\NWM_parameters\\'
    for root, dirs, files in os.walk(directory): 
        for file in files:
            if file.startswith('Route'):
                filePath = os.path.join(root, file)
                nc = netCDF4.Dataset(filePath, mode='r')
                #print(nc.variables.keys())
                ds = xr.open_dataset(filePath)
                df = ds.to_dataframe()
                df.reset_index(inplace = True)
                ##FOR SOME REASON THE INDEX RESET SHIFTS THE FEATURE ID IN THE LINK COLUMN (MAYBE XARRAY ISSUE)
                ##going to rename columns to account for it
                df = df.filter(['link','lat','lon'], axis=1)
                df = df.rename(columns={'link':'feature_id'})

                ##losing information with Xarray i think...
                #fh = filehandle
                reachData = Dataset(filePath, mode='r')
                #print(fh.variables)
                #FROM VARIABLE IS INTERESTING...
                lat  = reachData.variables['lat'][:]
                lon = reachData.variables['lon'][:]
                altitude = reachData.variables['alt'][:]
                slope = reachData.variables['slope'][:]
                print(len(vals))
                #for val in vals:
                    #print(val)
                #print(fh.variables['link'][:])
                #df.to_csv('reachIDs.csv')
    return
#parseID()



directory = os.getcwd()
for root, dirs, files in os.walk(directory): 
    for file in files:
        if file.startswith('stateNames'):
            filePath = os.path.join(root, file)
            states = pd.read_csv(filePath)
states = states['State'].values.tolist()
for state in states:
    try:
        url1 = 'https://prd-tnm.s3.amazonaws.com/StagedProducts/Hydrography/NHD/State/HighResolution/Shape/NHD_H_'+state+'_State_Shape.xml'
        url2 = 'https://prd-tnm.s3.amazonaws.com/StagedProducts/Hydrography/NHD/State/HighResolution/Shape/NHD_H_'+state+'_State_Shape.zip'
        wget.download(url1, 'D:\\NHD DataSet\\'+state+'.xml')
        wget.download(url2, 'D:\\NHD DataSet\\'+state+'.zip')
        
    except Exception as e:
        print(e)
        print(state+' failed')

"""
#TO DO 
#READ THE FLOWLINES BY ID AND GET THE NAME
#COMPARE THE NAME FOR SIMILARITY TO THE CLOSEST PUT IN GPS
#IF COMPARISON IS TOO LOW GO BACK TO THE ORIGINAL

sf = shapefile.Reader("D:\\NHD DataSet\\Shape\\NHDFlowline")
shapes = sf.shapes()
print(len(shapes))
print(sf.fields)
print(sf.record(0)[5])
print
for i in range(0,len(sf)):
    print(sf.record(i)[5])


#FIND SIMILARITY BETWEEN TWO STRINGS
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

>>> similar("Apple","Appel")
0.8
>>> similar("Apple","Mango")
0.0

"""