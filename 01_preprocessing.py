# loading the dataset
# converting price units
# creating categories/ price bins

import pandas as pd
df = pd.read_csv('Mumbai Housing Price.csv')

# convert price to INR
def convert_price(row):
    if row['price_unit'] == 'L':
        return row['price'] * 1e5
    elif row['price_unit'] == 'Cr':
        return row['price'] * 1e7
    return None

df['price_INR'] = df.apply(convert_price, axis = 1)
