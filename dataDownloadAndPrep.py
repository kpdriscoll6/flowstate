from datetime import datetime
#import urllib.request
from tqdm import tqdm
import wget
import os

#website FTP example url
#ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/nwm.20200512/short_range/nwm.t00z.short_range.channel_rt.f001.conus.nc

def downloadNWM(forecastRange):
    urlBase = 'ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/nwm.'
    today = datetime.now().strftime('%Y%m%d')+'/'
    if forecastRange == 'short':
        timeRange = 'short_range/'
        fileStart = 'nwm.t00z.short_range.channel_rt.f'
        fileMiddle = []
        fileEnd = '.conus.nc'
        for fileMiddle in tqdm(range(1,18+1)):
            url = (urlBase+today+timeRange+fileStart+str(fileMiddle).zfill(3)+fileEnd) #build the links (zfill is leading zero fill)
            #file = fileStart+str(fileMiddle).zfill(3)+fileEnd
            if os.path.exists(os.getcwd()+'/short/short'+str(fileMiddle).zfill(3)+'.nc'):
               os.remove(os.getcwd()+'/short/short'+str(fileMiddle).zfill(3)+'.nc')
            wget.download(url, os.getcwd()+'/short/short'+str(fileMiddle).zfill(3)+'.nc')
    elif forecastRange == 'medium':
        timeRange = 'medium_range_mem1/'
        fileStart = 'nwm.t00z.medium_range.channel_rt_1.f'
        fileMiddle = []
        fileEnd = '.conus.nc'
        #TEMPORARILY CHANGING 3 TO 234 FOR TIME SAKE CHANGE BACK
        for fileMiddle in tqdm(range(3,240+1,3)):
            url = (urlBase+today+timeRange+fileStart+str(fileMiddle).zfill(3)+fileEnd) #build the links (zfill is leading zero fill)
            #file = fileStart+str(fileMiddle).zfill(3)+fileEnd
            print(url)
            if os.path.exists(os.getcwd()+'/medium/medium'+str(fileMiddle).zfill(3)+'.nc'):
               os.remove(os.getcwd()+'/medium/medium'+str(fileMiddle).zfill(3)+'.nc')
            print(str(fileMiddle))
            wget.download(url, os.getcwd()+'/medium/medium'+str(fileMiddle).zfill(3)+'.nc')
    elif forecastRange == 'long':
        timeRange = 'long_range_mem1/'
        fileStart = 'nwm.t00z.long_range.channel_rt_1.f'
        fileMiddle = []
        fileEnd = '.conus.nc'
        for fileMiddle in tqdm(range(6,720+1,6)):
            url = (urlBase+today+timeRange+fileStart+str(fileMiddle).zfill(3)+fileEnd) #build the links (zfill is leading zero fill)
            #file = fileStart+str(fileMiddle).zfill(3)+fileEnd
            #print(url)
            if os.path.exists(os.getcwd()+'/long/long'+str(fileMiddle).zfill(3)+'.nc'):
               os.remove(os.getcwd()+'/long/long'+str(fileMiddle).zfill(3)+'.nc')
            wget.download(url, os.getcwd()+'/long/long'+str(fileMiddle).zfill(3)+'.nc')
    else:
        return('error')

downloadNWM('short')
downloadNWM('medium')  
downloadNWM('long')