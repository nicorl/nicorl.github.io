import pandas as pd
import numpy as np

csv_file = pd.read_csv('top50.csv', sep = None, engine = 'python')

print (csv_file)