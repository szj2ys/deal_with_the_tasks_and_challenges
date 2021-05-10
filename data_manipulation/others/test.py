# *_*coding:utf-8 *_*
'''
Descri：
'''
import pandas as pd
import numpy as np


data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}
df = pd.DataFrame(data)
df['score'].to_