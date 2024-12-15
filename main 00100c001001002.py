import streamlit as st

# Define categories and locations
categories = {
    "Vegetables": ["bangalore tomato", "beans", "beet root", "bitter gourd", "bottle gourd", "brinjal",
                   "broad beans", "cabbage", "capsicum", "carrot", "cauliflower", "chayote(seema vankaya)",
                   "Colocasia(chamagadda)", "coriander leaves", "cucumber(kira dosakaya)", "drum stick(munaga kaaya)",
                   "ginger", "green chilli", "green plantain(kuura aratikaaya)", "kohlrabi", "ladies finger", "mint",
                   "onion(big)", "plantain flower(arati puvvu)", "plantain stem(arati gadda)", "potato", "pumpkin",
                   "radish",
                   "ridge gourd(beera kaaya)", "scarlet gourd(donda kaaya)", "snake gourd(potla kaaya)",
                   "sweet potato(genisi gadda)",
                   "tapioca", "tomato", "yam(kandagadda)"],
    "Eggs": ["chicken egg", "country egg", "duck egg", "emu bird egg", "quail egg", "turkey egg"],

    "Fruits": ["Apple", "Avocado", "Black Grape", "Cherry", "Coconut", "Custard Apple", "Dates", "Fig(atthi kaaya)",
               "Gooseberry(usiri kaaya)", "Green Banana", "Jack Fruit", "Lemon", "Litchi", "Mango", "Mosambi", "Orange",
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
        "bangalore tomato": 30,
        "beans": 30,
        "beet root": 30,
        "bitter gourd": 30,
        "bottle gourd": 30,
        "brinjal": 30,
        "broad beans": 30,
        "cabbage": 30,
        "capsicum": 30,
        "carrot": 30,
        "cauliflower": 30,
        "chayote(seema vankaya)": 30,
        "Colocasia(chamagadda)": 30,
        "coriander leaves": 30,
        "cucumber(kira dosakaya)": 30,
        "drum stick(munaga kaaya)": 30,
        "ginger": 30,
        "green chilli": 30,
        "green plantain(kuura aratikaaya)": 30,
        "kohlrabi": 30,
        "ladies finger": 30,
        "mint": 30,
        "onion(big)": 30,
        "plantain flower(arati puvvu)": 30,
        "plantain stem(arati gadda)": 30,
        "potato": 30,
        "pumpkin": 30,
        "radish": 30,
        "ridge gourd(beera kaaya)": 30,
        "scarlet gourd(donda kaaya)": 30,
        "snake gourd(potla kaaya)": 30,
        "sweet potato(genisi gadda)": 30,
        "tapioca": 30,
        "tomato": 30,
        "yam(kandagadda)": 30
    },
    # ... other categories
    "Eggs": {
        "chicken egg": 6,
        "country egg": 6,
        "duck egg": 6,
        "emu bird egg": 6,
        "quail egg": 6,
        "turkey egg": 6
    },

    "Fruits": {
        "Apple": 100,
        "Avocado": 100,
        "Black Grape": 100,
        "Cherry": 100,
        "Coconut": 100,
        "Custard Apple": 100,
        "Dates": 100,
        "Fig(atthi kaaya)": 100,
        "Gooseberry(usiri kaaya)": 100,
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
locations = ["Gudur", "Nellore", "Amaravati", "Tirunelvelli", "Theni", "Rameswaram", "Pudukottai", "Dehradun",
             "Erode", "Dindigul", "Dharmapuri", "Dhanbad", "Ariyalur", "Fariabad", "Cuddalore", "Nammakal", "Gangtok",
             "Pammal",
             "Goa", "Pollachi", "Gurgaon", "Raipur", "Guwahati", "Arakkonam", "Hosur", "Thane", "Imphal",
             "Thiruvottiyur", "Varnasi",
             "Ambur", "Manali", "Indore", "Chengalpattu", "Alandur", "Mohali", "Maraimalai Nagar", "Bhopal",
             "Nagercoil", "Avadi",
             "Nagapattinam", "Jayankondam", "Kodaikanal", "Srinagar", "Kovilpatti", "Tambaram", "Krishnagir",
             "Thanjavur",
             "Kumbakonam", "Thiruthani", "Tiruvallur", "Tiruppur", "Ambattur", "Thiruvannamalai", "Ludhiana", "Trichy",
             "Madhavaram", "Tuticorin", "Virudhu Nagar", "Valasaravakkam", "Agra", "Ooty", "Kallakuridhi", "Arcot",
             "Noida",
             "Kanchipuram", "Palani", "Kanpur", "Paramakudi", "Kanyakumari", "Perambur", "Karaikudi", "Poonamallee",
             "Karur",
             "Kilakarai", "Salem", "RamananthaPuram", "Sivagangai", "Ranchi", "Anakapthur", "Shimla", "Vellore",
             "Aizawl", "Villupuram",
             "Madurantakam", "Maduravoyal", "Agartala"]


import streamlit as st

def home():
    st.title("Home Page")
    cartitems = []

    col1, col2 = st.columns(2)

    with col1:
        for category, items in categories.items():
            st.header(category)
            for i, item in enumerate(items):
                # Assuming you have images in a folder named 'images'
                image_path = f"Images/{item.lower().replace(' ', '_')}.jpeg"  # Replace with your image format
                price = categorieswise_price_dict[category][item]

                col3, col4, col5 = st.columns(3)
                with col3:
                    if st.checkbox(item, key=f"{category}_{i}"):
                        quantity = st.number_input("Quantity", min_value=1, max_value=10, key=f"{category}_{i}_quantity", )

                        cartitems.append((category, item, quantity))
                with col4:
                    st.image(image_path)
                with col5:
                    st.write(price)

    with col2:
        st.title("Your Cart")
        total_price = 0
        for category, item_name, quantity in cartitems:
            image_path = f"Images/{item_name.replace(' ', '_')}.jpeg"
            price = categorieswise_price_dict[category][item_name]
            total_price += price * quantity

            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"{item_name}")
            with col2:
                st.image(image_path)
            with col3:
                st.write(f"Price: ₹{price * quantity}")

        st.write(f"Total Price: ₹{total_price}")

        # st.button("Place Your Order", on_click=payment_page())
        payment_page(total_price)


def payment_page(total_price):
    st.title("Payment Page")

    st.write("Select Payment Method:")
    payment_method = st.radio("", ("COD", "Pay Online"))

    if st.button("Confirm Order"):
        if payment_method == "COD":
            st.write(f" Pay {total_price} at your door step")
            st.success("Order placed successfully! Your order will be delivered soon.")
        elif payment_method == "Pay Online":
            # Redirect to payment link
            st.write("Redirecting to payment gateway...")
            st.image("Payment_settings/Offline Merchant.png")


            # Add your payment gateway integration logic here
            # For example, using a library like `stripe` or `razorpay`
            # You can use `st.experimental_rerun` to trigger a redirect
def select_location():
    st.sidebar.title("Select Location")
    location = st.sidebar.selectbox("Choose a location", locations)
    st.write(f"You selected: {location}")

def account_profile():
    st.title("Account & Profile")
    # Add user profile details, order history, and settings

def wallet():
    st.markdown("payment")
def orders():
    st.title("Orders")
    # Display past order history
def cart():

    st.title("Cart")

    # Display items in the cart with quantity and total


# Main app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ["Home", "Select Location", "Wallet", "Account & Profile", "Orders", "Cart"])

    if page == "Home":
        home()
    elif page == "Select Location":
        select_location()
    elif page == "Payment":
        wallet()
    elif page == "Account & Profile":
        account_profile()
    elif page == "Orders":
        orders()
    elif page == "Cart":
        cart()

if __name__ == "__main__":
    main()