import pandas as pd 
import numpy as np
new_data = pd.DataFrame({'name': ['Aby', 'Carla', 'Bob', 'Sally'],
                        'car': ['Honda', np.nan, 'BMW', 'Chevrolete'],
                        'year': ['2003', np.nan, '2007', np.nan]})


print(new_data.head())
## this function will print missin values in particular column and
## will return rows which contain nans 
def report_nan(X, col):
    X = X.copy()
    col_with_nan = pd.isnull(X[col])
    
    return X[col_with_nan]
print(report_nan(new_data, 'car'))

print(report_nan(new_data, 'year'))