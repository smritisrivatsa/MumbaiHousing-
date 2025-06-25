# loading the dataset
import pandas as pd
df = pd.read_csv('Mumbai Housing Price.csv')
# converting price units

# creating categories
def category(p):
    if p < 50 * 1e5:
        return 'Low'
    elif df.p < 2 * 1e7:
        return 'Medium'
    else:
        return 'High'
    
df['price_bin'] = df['price_INR'].apply(category, axis = 1)

