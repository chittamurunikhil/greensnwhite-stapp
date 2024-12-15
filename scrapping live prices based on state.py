import requests
from bs4 import BeautifulSoup


def scrape_vegetable_prices(state):
    url = f"https://vegetablemarketprice.com/market/{state}/today"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {state}: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing vegetable data
    table = soup.find('table', {'class': 'table table-bordered table-striped'})

    if not table:
        print(f"Table not found for {state}")
        return

    # Extract vegetable names and prices
    vegetable_data = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) >= 2:  # Ensure there are at least two columns (name and price)
            vegetable_name = columns[0].text.strip()
            price = columns[1].text.strip()
            vegetable_data.append((vegetable_name, price))

    return vegetable_data

# Example usage:
state = "andhrapradesh"  # Replace with the desired state
vegetable_data = scrape_vegetable_prices(state)

if vegetable_data:
    for vegetable, price in vegetable_data:
        print(f"{vegetable}: {price}")
else:
    print(f"No data found for {state}")