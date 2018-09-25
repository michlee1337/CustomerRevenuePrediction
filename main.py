
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
df = pd.read_csv(zf.open('train.csv'))

# setting column dtypes
df['channelGrouping'].astype('category')
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['device'] = df['device'].astype('object')
df['fullVisitorId'] = df['fullVisitorId'].astype('str')
df['geoNetwork'] = df['geoNetwork'].astype('object')
df['sessionId'] = df['sessionId'].astype('object')
df['socialEngagementType'] = df['socialEngagementType'].astype('category')
df['totals'] = df['totals'].astype('object')
df['trafficSource'] = df['trafficSource'].astype('object')
df['visitId'] = df['visitId'].astype('uint64')
df['visitStartTime'] = df['visitStartTime'].astype('uint64')


# looking at data
print(df.shape)

# ________________________ WIP _______________________________
# extract the revenue from total
# eh this can wait
import re
hi = df.loc[752,'totals']
m = re.search('tr.*\\,',hi).group(0)

print(m)
print(type(m))
# ________________________ WIP _______________________________
