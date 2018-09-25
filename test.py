# random test code
# just feels cleaner on a separate doc

import re

t = '{"visits": "1", "hits": "11", "pageviews": "11", "transactionRevenue": "37860000", "newVisits": "1"}'

hi = re.search('tr.*\\,',t)

print(hi.group(0))
