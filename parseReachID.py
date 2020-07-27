import netCDF4
import pandas as pd
import os
import xarray as xr
import shapefile
import wget
from tqdm import tqdm


def parseID():
    #This function saves a CSV of the GPS coords of each Reach ID and appends the river name from the flow_table.txt file
    flowTable = pd.read_csv(os.getcwd()+'\\NWM_parameters\\COMID_Names.csv', index_col=0)
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
    df = df.rename(columns={'link':'feature_id'})
    #add a column for name
    df['name'] = ''
    #COMIDs = df['NHDWaterbodyComID']
    COMIDs = df['feature_id']
    for COMID in tqdm(COMIDs):
        #check if the COMID is in the flowTable & add that to the datafram if it exists
        if COMID in flowTable.COMID.values:
            name = flowTable.loc[flowTable['COMID']==COMID].values.tolist()[0][1]
            df.loc[df['feature_id']==COMID, ['name']] = name
            #SYNTAX FOR REPLACEMENT
            #df.loc[df[<some_column_name>] == <condition>, [<another_column_name>]] = <value_to_add>
            #print(df.loc[df['feature_id']==COMID])
    df.to_csv('reachIDs.csv')
                
    return

#print(flowTable.head())
#name = flowTable.loc[flowTable['COMID']==721640]['GNIS_NAME'].values[0]
#sprint(name)
parseID()








"""


def downloadStateReaches():
#THIS FUNCTION DOWNLOADS THE NHD SHAPEFILES BY STATE (SHAPEFILES NOT AVAILABLE FOR WHOLE COUNTRY)
    directory = os.getcwd()
    #FIRST GET A LIST OF ALL THE STATES
    for root, dirs, files in os.walk(directory): 
        for file in files:
            if file.startswith('stateNames'):
                filePath = os.path.join(root, file)
                states = pd.read_csv(filePath)
    #THEN DOWNLOAD THE THE STATE SHAPEFILES AND XML
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

            #THE FLOW TABLE HAS THE COMID & GNIS_NAME EUREKA!!!
#EXAMPLE BELOW FOR POUDRE RIVER
temp = pd.read_csv('D:\\flowStateStorage\\flow_table.txt')
print(temp.head())
comid = temp['COMID'].values.tolist()
name = temp['GNIS_NAME'].values.tolist()
val = 2900003
ind=comid.index(val)
print(name[ind])

#FIND SIMILARITY BETWEEN TWO STRINGS
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

similar("Apple","Appel")
similar("Apple","Mango")

"""