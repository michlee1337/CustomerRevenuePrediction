
# import libraries
import scipy
import numpy
import matplotlib
import pandas as pd
import sklearn
import zipfile
import datetime

# import data
zf = zipfile.ZipFile('train.csv.zip')
df = pd.read_csv(zf.open('train.csv')) #, dtype={'channelGrouping': str, 'date': str, 'device': object, 'fullVisitorId': int, 'geoNetwork': object, 'sessionId': int, 'socialEngagementType': str, 'totals': object, 'trafficSource': object, 'visitId': int, 'visitNumber': int, 'visitStartTime': int})

# setting column dtypes
df['channelGrouping'] = df['channelGrouping'].astype('category')
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['device'] = df['device'].astype('object')
df['fullVisitorId'] = df['fullVisitorId'].astype('object')
df['geoNetwork'] = df['geoNetwork'].astype('object')
df['sessionId'] = df['sessionId'].astype('object')
df['socialEngagementType'] = df['socialEngagementType'].astype('category')
df['totals'] = df['totals'].astype('object')
df['trafficSource'] = df['trafficSource'].astype('object')
df['visitId'] = df['visitId'].astype('uint64')
df['visitStartTime'] = df['visitStartTime'].astype('uint64')
# gotta do this with all the columns


# looking at data
#print(df.shape)
print(df.iloc[0:10,11])
