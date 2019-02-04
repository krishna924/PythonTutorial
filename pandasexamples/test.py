
import pandas as pd
import numpy as np
import os



s = pd.Series(np.random.random(5), index=['a', 'b', 'c', 'd', 'e'])

d = {'a' : 0., 'b' : 1., 'c' : 2.}
print(d['c'])

pd.Series(d, index=['b', 'c', 'd', 'a'])

data = {
    'order_id' : [1, 2],
    'order_date' : ['2014-01-01 00:00:00', '2014-01-01 00:00:00'],
    'order_customer_id' : [1, 1],
    'order_status' : ['COMPLETE', 'CLOSED']
}

df = pd.DataFrame(data, columns=['order_id', 'order_date', 'order_customer_id', 'order_status'])

#Accessing by column
print(df.order_id)
print(df.order_status)

#Accessing by row index
print(df.iloc[[1]])

#Setting index
df1 = df.set_index(df.order_id)


orders = pd.read_csv

