#!/usr/bin/env python3

import re 

regex= re.compile(r'\d+\.?\d+GB')
res = list(filter(regex.match, data))
