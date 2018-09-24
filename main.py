
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

print(df)
