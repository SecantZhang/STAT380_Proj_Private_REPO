from googletrans import Translator
import pandas as pd
import numpy as np

"""
import csv
"""
df = pd.DataFrame(pd.read_csv('seg_translate.csv'))

"""
create empty array for placeholder
"""

a = np.empty(df.shape[0], dtype=object)

for i in range(df.shape[0]):
    test = Translator().translate(text=df.iloc[i][0], dest='en').text
    a[i] = str(test)

a = pd.DataFrame(a)
a.to_csv("translate", sep='\t')


"""
test cases
"""
#s = Translator().translate(text='Hello my friend', dest='es').text
#test =  Translator().translate(text=str(df.iloc[0][0]), dest='en').text
#a[0] = str(test)
#print(a)
#df = a.append(df, ignore_index=True)
#print(df.head(5))
#print(text.iloc[1][0])
#print(text.shape[0])




