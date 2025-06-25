# Data Preprocessing
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mumbai_housing_prices.csv')

# convert price to INR
def convert_price(row):
    if row['price_unit'] == 'L':
        return row['price'] * 1e5
    elif row['price_unit'] == 'Cr':
        return row['price'] * 1e7
    return None

df['price_INR'] = df.apply(convert_price, axis = 1)

# creating categories
def category(row):
    if row['price_INR'] < 50 * 1e5:
        return 'Low'
    elif row['price_INR'] < 2 * 1e7:
        return 'Medium'
    else:
        return 'High'
    
df['price_bin'] = df.apply(category,  axis=1)


for col in ['type', 'status', 'region']:
    le = LabelEncoder()
    df[col + '_encoded'] = le.fit_transform(df[col])

df.to_csv('mumbai_housing_prices_modified.csv', index=False)