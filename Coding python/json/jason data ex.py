# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:48:38 2020

@author: aftab
"""

import numpy as np
np.set_printoptions(threshold=np.inf)

import requests
import json
params={'links':'href'}
page = requests.get("https://data.townofcary.org/api/v2/catalog/datasets/rdu-weather-history",params={'dataset':'fields'})

print(page.text)

data_set = page.json()
json_data=json.dumps(data_set, indent=4)
print(json_data)

# write the output  in the file
with open('out.txt', 'w') as f:
    print('Filename:', json_data, file=f)
    

    


