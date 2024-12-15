import requests
from bs4 import BeautifulSoup
import pandas as pd

import pandas as pd

# Read the Excel file
excel_file = 'product_prices_and_locations.xlsx'

# Read the 'Prices' sheet into a DataFrame
df_prices = pd.read_excel(excel_file, sheet_name='Prices')

# Read the 'Locations' sheet into a DataFrame
df_locations = pd.read_excel(excel_file, sheet_name='Locations')

df_locations["State"] = df_locations["State"].apply(lambda x : x.replace(" ", "-"))

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
categories
# Create the `locations_dict`
locations_dict = df_locations.set_index('Location')['State'].to_dict()

print(categorieswise_price_dict)
print(categories)
print(locations_dict)
# List of cities
# cities = [
#     "Anantapur", "Chittoor", "Eluru",
#     "Guntur", "Kadapa", "Kakinada",
#     "Kurnool", "Machilipatnam", "Nellore",
#     "Ongole", "Srikakulam", "Visakhapatnam",
#     "Vizianagaram"
# ]
cities = list(locations_dict)
categories_list = list(categories)
# Base URL with placeholder for the city
base_url = "https://market.todaypricerates.com/{city}-{category}-price-in-{state}"

# # Create a list of URLs for each city
# urls = [base_url.format(city=city,state= state, category = category) for city,state in locations_dict.items()]
urls= []
for category in categories_list:
    for city, state in locations_dict.items():
        urls.append(base_url.format(city=city,  state= state, category=category.lower()))
# Function to scrape vegetable prices for a given city URL
def scrape_vegetable_prices(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing the vegetable prices
        table = soup.find('table')

        if table:
            # Extract the rows of the table
            rows = []
            for row in table.find_all('tr')[1:]:  # Skip the header row
                columns = row.find_all('td')
                if len(columns) > 1:
                    # Extract vegetable name (first column) and market price (second column)
                    vegetable_name = columns[0].text.strip()
                    market_price = columns[2].text.strip()
                    rows.append([vegetable_name, market_price])

            # Create a DataFrame
            df = pd.DataFrame(rows, columns=["Vegetable Name", "Market Price"])
            return df
        else:
            print(f"No table found on the webpage for {url}.")
            return None
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return None

# Create an Excel writer object to save data to Excel
with pd.ExcelWriter('All_Vegetable_Prices.xlsx') as writer:
    # Loop through each city URL and scrape the vegetable prices
    for url in urls:
        # Correctly extract city name from the URL
        city_name = url.split('/')[-1].split('-')[0]
        category_name = url.split('/')[-1].split('-')[1]
        print(f"Scraping data for {city_name} and {category_name}...")

        # Scrape vegetable prices for the city
        df = scrape_vegetable_prices(url)

        if df is not None:
            # Write the data to a different sheet for each city
            df.to_excel(writer, sheet_name=f"{city_name} {category_name}", index=False)
            print(f"Data for {city_name} {category_name} has been added to the sheet.")
        else:
            print(f"No data found for {city_name}.")

print("All vegetable prices have been saved to 'All_Vegetable_Prices.xlsx'.")
