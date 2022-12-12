import pandas as pd
import numpy as np
from scipy import stats 
#importing dataset
df = pd.read_csv('data.csv')
#filtering outliers
df['zscore'] = ( df.Calories - df.Calories.mean() ) / df.Calories.std()
df[df['zscore']>3]
