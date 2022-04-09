#!/usr/bin/env python3

import re 
data = ['Data', 'Usage', '19.7GB', 'Remaining', 'Expires', 'On:', '3', 'Jun', '2022', '2:21', 'PM']

regex= re.compile(r'\d+\.?\d+GB')
res = list(filter(regex.match, data))
#res =re.findall(r'\w',data)
print(res)
