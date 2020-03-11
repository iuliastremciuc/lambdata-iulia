import pandas as pd
import numpy as np

date = pd.DataFrame({"Date": ['01.01.2001', '02.02.2002', '03.03.2003',
                 '04.04.2004', '05.05.2005']})
print(date.head())

def split_dates(X):
    X = X.copy()
    X['Date'] = pd.to_datetime(X['Date'], infer_datetime_format = True)
    X['Month'] = X['Date'].dt.month
    X['Day'] = X['Date'].dt.day
    X['Year'] = X['Date'].dt.year

    X = X.drop('Date', axis = 1)
    return X

print(split_dates(date))
    


