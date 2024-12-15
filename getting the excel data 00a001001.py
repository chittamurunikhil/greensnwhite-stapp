# import pandas as pd
#
# # Read the Excel file
# excel_file = 'product_prices_and_locations.xlsx'
#
# # Read the 'Prices' sheet into a DataFrame
# df_prices = pd.read_excel(excel_file, sheet_name='Prices')
#
# # Read the 'Locations' sheet into a DataFrame
# df_locations = pd.read_excel(excel_file, sheet_name='Locations')
#
# # Convert DataFrame to dictionaries
# categorieswise_price_dict = df_prices.groupby('Category').apply(lambda x: x.set_index('Item')['Price'].to_dict()).to_dict()
# locations = df_locations['Location'].tolist()
#
# # Print the dictionaries
# print(categorieswise_price_dict)
# print(locations)
import pandas as pd

# Read the Excel file
excel_file = 'product_prices_and_locations.xlsx'

# Read the 'Prices' sheet into a DataFrame
df_prices = pd.read_excel(excel_file, sheet_name='Prices')

# Read the 'Locations' sheet into a DataFrame
df_locations = pd.read_excel(excel_file, sheet_name='Locations')

# Create the `categorieswise_price_dict`
categorieswise_price_dict = {}
for index, row in df_prices.iterrows():
    category = row['Category']
    item = row['Item']
    price = row['Price']
    if category not in categorieswise_price_dict:
        categorieswise_price_dict[category] = {}
    categorieswise_price_dict[category][item] = price

# Create the `categories` dictionary without prices
categories = {}
for category, items in categorieswise_price_dict.items():
    categories[category] = list(items.keys())

# Create the `locations_dict`
locations_dict = df_locations.set_index('Location')['State'].to_dict()

print(categorieswise_price_dict)
print(categories)
print(locations_dict)