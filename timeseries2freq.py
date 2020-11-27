import pandas as pd
import numpy as np

file_path = r'C:\Users\owner\Downloads\discharge.xlsx'

# =============================================================================
# idx_col is the date column
# header_row is the row with the headers
# skip is skiprows
# dropneg is drop the negative values
# =============================================================================

def ts2frq(path, idx_col, header_row, skip, dropneg, frequency):
    timeseries = pd.read_excel(file_path, header = header_row, index_col = idx_col, skiprows = 0)
    timeseries.index = pd.to_datetime(timeseries.index, format = '%d/%m/%yy') #e.g. 01/02/2005
    if dropneg == True:
        timeseries = timeseries[timeseries.iloc[:, :1] >= 0]
        timeseries = timeseries.dropna(axis = 0)
    timeseries['Sum'] = timeseries.iloc[:, :1].resample(rule = frequency).sum()
    timeseries['Mean'] = timeseries.iloc[:, :1].resample(rule = frequency).mean()
    return timeseries

ts = ts2frq(file_path, 0, 0, 0, True, 'M')

# =============================================================================
# Separate dates
# example = pd.read_csv(file, names = [ 'year' , 'month' , 'day' , 'hour' , 'minute', 'rainfall'])
# example.loc[:, 'dt'] = pd.to_datetime(charlotte_rainfall.loc[:, ['year', 'month', 'day', 'hour', 'minute']])
# example = example.set_index('dt')
# =============================================================================