import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

import pandas_profiling as pp
import warnings
warnings.filterwarnings('ignore')


pp.ProfileReport(train_df, title = 'Pandas Profiling report of "Train" set', html = {'style':{'full_width': True}})