import pandas as pd

# Define your data structures

# Define categories and locations
categories = {
    "Vegetables": ["Bangalore Tomato", "Beans", "Beet Root", "Bitter Gourd", "Bottle Gourd", "Brinjal",
                   "Broad Beans", "Cabbage", "Capsicum", "Carrot", "Cauliflower", "Chayote(Seema Vankaya)",
                   "Colocasia(Chamagadda)", "Coriander Leaves", "Cucumber(Kira Dosakaya)", "Drum Stick(Munaga Kaaya)",
                   "Ginger", "Green Chilli", "Green Plantain(Kuura Aratikaaya)", "Kohlrabi", "Ladies Finger", "Mint",
                   "Onion(Big)", "Plantain Flower(Arati Puvvu)", "Plantain Stem(Arati Gadda)", "Potato", "Pumpkin",
                   "Radish",
                   "Ridge Gourd(Beera Kaaya)", "Scarlet Gourd(Donda Kaaya)", "Snake Gourd(Potla Kaaya)",
                   "Sweet Potato(Genisi Gadda)",
                   "Tapioca", "Tomato", "Yam(Kandagadda)"],
    "Eggs": ["Chicken Egg", "Country Egg", "Duck Egg", "Emu Bird Egg", "Quail Egg", "Turkey Egg"],

    "Fruits": ["Apple", "Avocado", "Black Grape", "Cherry", "Coconut", "Custard Apple", "Dates", "Fig(Atthi Kaaya)",
               "Gooseberry(Usiri Kaaya)", "Green Banana", "Jack Fruit", "Lemon", "Litchi", "Mango", "Mosambi", "Orange",
               "Papaya", "Peach", "Pear", "Pine Apple", "Plum", "Pomegranate", "Sapota", "Strawberry", "Watermelon",
               "Yellow Banana"],

    "Flowers": ["Anthurium", "Carnation", "Chamanthi", "Jasmine(Malle Puvvu)", "Marigold(Banthi Puvvu)", "Orchid",
                "Rose"],

    "Fish": ["Anchovy", "Barracuda", "Crab", "King Mackerel", "Pomfret", "Prawn", "Red Snapper", "Salmon", "Sardine",
             "Shark", "Tilapia"],

    "Chicken": ["Boneless Chicken", "Chicken", "Chicken Liver", "Country Chicken", "Live Chicken", "Skinless Chicken"],

    "Hens and Birds": ["Natu Kodi (Indian Chicken)", "Kadaknath", "Kamju Pitta", "Duck", "Broiler Kodi", "Emu Bird",
                       "Ostrich", "Guinea Kodi", "Pigeons"],

    # ... other categories
}

categorieswise_price_dict = {
    "Vegetables": {
        "Bangalore Tomato": 30,
        "Beans": 30,
        "Beet Root": 30,
        "Bitter Gourd": 30,
        "Bottle Gourd": 30,
        "Brinjal": 30,
        "Broad Beans": 30,
        "Cabbage": 30,
        "Capsicum": 30,
        "Carrot": 30,
        "Cauliflower": 30,
        "Chayote(Seema Vankaya)": 30,
        "Colocasia(Chamagadda)": 30,
        "Coriander Leaves": 30,
        "Cucumber(Kira Dosakaya)": 30,
        "Drum Stick(Munaga Kaaya)": 30,
        "Ginger": 30,
        "Green Chilli": 30,
        "Green Plantain(Kuura Aratikaaya)": 30,
        "Kohlrabi": 30,
        "Ladies Finger": 30,
        "Mint": 30,
        "Onion(Big)": 30,
        "Plantain Flower(Arati Puvvu)": 30,
        "Plantain Stem(Arati Gadda)": 30,
        "Potato": 30,
        "Pumpkin": 30,
        "Radish": 30,
        "Ridge Gourd(Beera Kaaya)": 30,
        "Scarlet Gourd(Donda Kaaya)": 30,
        "Snake Gourd(Potla Kaaya)": 30,
        "Sweet Potato(Genisi Gadda)": 30,
        "Tapioca": 30,
        "Tomato": 30,
        "Yam(Kandagadda)": 30
    },
    # ... other categories
    "Eggs": {
        "Chicken Egg": 6,
        "Country Egg": 6,
        "Duck Egg": 6,
        "Emu Bird Egg": 6,
        "Quail Egg": 6,
        "Turkey Egg": 6
    },

    "Fruits": {
        "Apple": 100,
        "Avocado": 100,
        "Black Grape": 100,
        "Cherry": 100,
        "Coconut": 100,
        "Custard Apple": 100,
        "Dates": 100,
        "Fig(Atthi Kaaya)": 100,
        "Gooseberry(Usiri Kaaya)": 100,
        "Green Banana": 100,
        "Jack Fruit": 100,
        "Lemon": 100,
        "Litchi": 100,
        "Mango": 100,
        "Mosambi": 100,
        "Orange": 100,
        "Papaya": 100,
        "Peach": 100,
        "Pear": 100,
        "Pine Apple": 100,
        "Plum": 100,
        "Pomegranate": 100,
        "Sapota": 100,
        "Strawberry": 100,
        "Watermelon": 100,
        "Yellow Banana": 100
    },

    "Flowers": {
        "Anthurium": 200,
        "Carnation": 200,
        "Chamanthi": 200,
        "Jasmine(Malle Puvvu)": 200,
        "Marigold(Banthi Puvvu)": 200,
        "Orchid": 200,
        "Rose": 200
    },
    "Fish": {
        "Anchovy": 600,
        "Barracuda": 600,
        "Crab": 600,
        "King Mackerel": 600,
        "Pomfret": 600,
        "Prawn": 600,
        "Red Snapper": 600,
        "Salmon": 600,
        "Sardine": 600,
        "Shark": 600,
        "Tilapia": 600
    },

    "Chicken": {
        "Boneless Chicken": 350,
        "Chicken": 250,
        "Chicken Liver": 200,
        "Country Chicken": 600,
        "Live Chicken": 250,
        "Skinless Chicken": 300
    },

    "Hens and Birds": {
        "Natu Kodi (Indian Chicken)": 600,
        "Kadaknath": 800,
        "Kamju Pitta": 800,
        "Duck": 600,
        "Broiler Kodi": 200,
        "Emu Bird": 900,
        "Ostrich": 900,
        "Guinea Kodi": 600,
        "Pigeons": 200
    },
}
# locations = ["Gudur", "Nellore", "Amaravati", "Tirunelvelli", "Theni", "Rameswaram", "Pudukottai", "Dehradun",
#              "Erode", "Dindigul", "Dharmapuri", "Dhanbad", "Ariyalur", "Fariabad", "Cuddalore", "Nammakal", "Gangtok",
#              "Pammal",
#              "Goa", "Pollachi", "Gurgaon", "Raipur", "Guwahati", "Arakkonam", "Hosur", "Thane", "Imphal",
#              "Thiruvottiyur", "Varnasi",
#              "Ambur", "Manali", "Indore", "Chengalpattu", "Alandur", "Mohali", "Maraimalai Nagar", "Bhopal",
#              "Nagercoil", "Avadi",
#              "Nagapattinam", "Jayankondam", "Kodaikanal", "Srinagar", "Kovilpatti", "Tambaram", "Krishnagir",
#              "Thanjavur",
#              "Kumbakonam", "Thiruthani", "Tiruvallur", "Tiruppur", "Ambattur", "Thiruvannamalai", "Ludhiana", "Trichy",
#              "Madhavaram", "Tuticorin", "Virudhu Nagar", "Valasaravakkam", "Agra", "Ooty", "Kallakuridhi", "Arcot",
#              "Noida",
#              "Kanchipuram", "Palani", "Kanpur", "Paramakudi", "Kanyakumari", "Perambur", "Karaikudi", "Poonamallee",
#              "Karur",
#              "Kilakarai", "Salem", "RamananthaPuram", "Sivagangai", "Ranchi", "Anakapthur", "Shimla", "Vellore",
#              "Aizawl", "Villupuram",
#              "Madurantakam", "Maduravoyal", "Agartala"]
locations_dict = {'Gudur': 'Andhra Pradesh', 'Nellore': 'Andhra Pradesh', 'Amaravati': 'Andhra Pradesh', 'Tirunelvelli': 'Tamil Nadu',
             'Theni': 'Tamil Nadu', 'Rameswaram': 'Tamil Nadu', 'Pudukottai': 'Tamil Nadu', 'Dehradun': 'Uttarakhand',
             'Erode': 'Tamil Nadu', 'Dindigul': 'Tamil Nadu', 'Dharmapuri': 'Tamil Nadu', 'Dhanbad': 'Jharkhand', 'Ariyalur': 'Tamil Nadu',
             'Fariabad': 'Haryana', 'Cuddalore': 'Tamil Nadu', 'Nammakal': 'Tamil Nadu', 'Gangtok': 'Sikkim', 'Pammal': 'Tamil Nadu', 'Goa': 'Goa',
             'Pollachi': 'Tamil Nadu', 'Gurgaon': 'Haryana', 'Raipur': 'Chhattisgarh', 'Guwahati': 'Assam', 'Arakkonam': 'Tamil Nadu',
             'Hosur': 'Tamil Nadu', 'Thane': 'Maharashtra', 'Imphal': 'Manipur', 'Thiruvottiyur': 'Tamil Nadu', 'Varnasi': 'Uttar Pradesh',
             'Ambur': 'Tamil Nadu', 'Manali': 'Himachal Pradesh', 'Indore': 'Madhya Pradesh', 'Chengalpattu': 'Tamil Nadu', 'Alandur': 'Tamil Nadu',
             'Mohali': 'Punjab', 'Maraimalai Nagar': 'Tamil Nadu', 'Bhopal': 'Madhya Pradesh', 'Nagercoil': 'Tamil Nadu', 'Avadi': 'Tamil Nadu',
             'Nagapattinam': 'Tamil Nadu', 'Jayankondam': 'Tamil Nadu', 'Kodaikanal': 'Tamil Nadu', 'Srinagar': 'Jammu and Kashmir', 'Kovilpatti': 'Tamil Nadu',
             'Tambaram': 'Tamil Nadu', 'Krishnagir': 'Tamil Nadu', 'Thanjavur': 'Tamil Nadu', 'Kumbakonam': 'Tamil Nadu', 'Thiruthani': 'Tamil Nadu',
             'Tiruvallur': 'Tamil Nadu', 'Tiruppur': 'Tamil Nadu', 'Ambattur': 'Tamil Nadu', 'Thiruvannamalai': 'Tamil Nadu', 'Ludhiana': 'Punjab', 'Trichy': 'Tamil Nadu',
             'Madhavaram': 'Tamil Nadu', 'Tuticorin': 'Tamil Nadu', 'Virudhu Nagar': 'Tamil Nadu', 'Valasaravakkam': 'Tamil Nadu', 'Agra': 'Uttar Pradesh',
             'Ooty': 'Tamil Nadu', 'Kallakuridhi': 'Tamil Nadu', 'Arcot': 'Tamil Nadu', 'Noida': 'Uttar Pradesh', 'Kanchipuram': 'Tamil Nadu', 'Palani': 'Tamil Nadu',
             'Kanpur': 'Uttar Pradesh', 'Paramakudi': 'Tamil Nadu', 'Kanyakumari': 'Tamil Nadu', 'Perambur': 'Tamil Nadu', 'Karaikudi': 'Tamil Nadu', 'Poonamallee': 'Tamil Nadu',
             'Karur': 'Tamil Nadu', 'Kilakarai': 'Tamil Nadu', 'Salem': 'Tamil Nadu', 'RamananthaPuram': 'Tamil Nadu', 'Sivagangai': 'Tamil Nadu', 'Ranchi': 'Jharkhand',
             'Anakapthur': 'Tamil Nadu', 'Shimla': 'Himachal Pradesh', 'Vellore': 'Tamil Nadu', 'Aizawl': 'Mizoram', 'Villupuram': 'Tamil Nadu', 'Madurantakam': 'Tamil Nadu',
             'Maduravoyal': 'Tamil Nadu', 'Agartala': 'Tripura'}


import pandas as pd

# Create DataFrames
df_prices = pd.DataFrame.from_dict(categorieswise_price_dict, orient='index').stack().reset_index()
df_prices.columns = ['Category', 'Item', 'Price']

# df_locations = pd.DataFrame({'Location': locations})
df_locations = pd.DataFrame.from_dict(locations_dict, orient='index').stack().reset_index()
df_locations.columns = ['Location', "0",'State']
df_locations = df_locations[['Location','State']]
print(df_locations.head)
# Write to Excel
with pd.ExcelWriter('product_prices_and_locations.xlsx') as writer:
    df_prices.to_excel(writer, sheet_name='Prices', index=False)
    df_locations.to_excel(writer, sheet_name='Locations', index=False)

