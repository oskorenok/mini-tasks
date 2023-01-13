import pandas as pd
import numpy as np

# Generate a random csv file filled with random numbers

size = 1_000_000
path = './random_table.csv'

dates = pd.date_range(start='1/1/2000', periods=size, freq='H')
values = np.random.randint(0, 100, size=size)

df = pd.DataFrame(zip(dates, values), columns=['date', 'value'])

df.to_csv(path, index_label='id')