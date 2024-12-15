import streamlit as st

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

    # Select location
    location = st.selectbox("Choose your location", locations)
    st.write(f"Your Selected Location: {location}")

    if location:
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
                            # quantity_type = st.radio("Quantity Type", ["Below 1 kg", "Above 1 kg"],
                            #                          key=f"{category}_{i}_quantity_type")
                            #
                            # if quantity_type == "Below 1 kg":
                            #     quantity = st.slider("Quantity in grams", 50, 1000, 50, key=f"{category}_{i}_quantity",
                            #                          step=50)
                            #     quantity *= .001
                            #
                            # else:
                            quantity = st.number_input("Quantity (kg)", min_value=0.250, max_value=20.0,
                                                           step=0.25, key=f"{category}_{i}_quantity")

                            cartitems.append((category, item, quantity))
                    with col4:
                        st.image(image_path)
                    with col5:
                        st.markdown(f"<h4 style='font-weight: bold; color: orange;'>₹{price}</h4>", unsafe_allow_html=True)

        with col2:
            st.title("Your Cart")
            st.write("All the values are rounded to the nearest number")
            total_price = 0
            all_quantities_less_than_one = True
            first_item_rounded = False

            # Check all quantities first
            for _, _, quantity in cartitems:
                if quantity >= 1:
                    all_quantities_less_than_one = False
                    break

            # Round up the first item and calculate the total price
            for category, item_name, quantity in cartitems:
                image_path = f"Images/{item_name.replace(' ', '_')}.jpeg"
                price = categorieswise_price_dict[category][item_name]

                # Round up the first item if all quantities are less than 1
                if all_quantities_less_than_one and not first_item_rounded:
                    quantity = 1.0
                    first_item_rounded = True
                    st.markdown(f"<h4 style='font-weight: bold; font-size: 16px;'>Note: The first item's quantity has been rounded up to 1 kg.</h4>", unsafe_allow_html=True)

                total_price += round(price * quantity)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"<h4 style='font-weight: bold; font-size: 16px; color: Black;'> {item_name.title()} </h4>", unsafe_allow_html=True)
                with col2:
                    st.image(image_path)
                with col3:
                    st.markdown(
                        f"<h4 style='font-weight: bold; color: black;'>Price: ₹{(price)} * {(round(quantity, 2))} kg = ₹{round(price * quantity)}</h4>",
                        unsafe_allow_html=True)

            st.markdown(f"<h4 style='font-weight: bold; color: red;'>Total Price: ₹{total_price}</h4>",
                        unsafe_allow_html=True)

            payment_page(total_price)

def payment_page(total_price):
    st.title("Payment Page")

    st.write("Select Payment Method:")
    payment_method = st.radio("", ("COD", "Pay Online"))
    if st.button("Confirm Order"):
        if payment_method == "COD":
            st.write(f"Pay <h4 style='font-weight: bold; color: blue;'>₹{total_price}</h4> At your door step",
                     unsafe_allow_html=True)
            st.success("Order placed successfully! Your order will be delivered soon.")
        elif payment_method == "Pay Online":
            # st.write(f"Payment for ₹{total_price}")
            st.write(f"Payment for  <h4 style='font-weight: bold; color: blue;'>₹{total_price}</h4> ",
                     unsafe_allow_html=True)
            st.write("Redirecting to payment gateway...")

            st.image("Payment_settings/Offline Merchant.png")  # Display the image

            # payment_status = st.radio("", ("Completed Payment", "In progress"))
            # if st.button("YES"):
            #     if payment_status == "Completed Payment":
            #         utr_number = st.number_input("Enter UTR Number (12 digits):", min_value=100000000000,
            #                                      max_value=999999999999)
            #         if len(utr_number) == 12 and utr_number.isdigit():
            #             st.success("Payment successful! Order placed successfully.")
            #             st.write("UTR Number:", utr_number)
            #         else:
            #             st.write("Invalid UTR Number. Please enter 12 digits.")


            # utr_number = st.number_input("Enter UTR Number (12 digits):", min_value= 100000000000, max_value=999999999999)
            # if len(utr_number) == 12 and utr_number.isdigit():
            #     st.success("Payment successful! Order placed successfully.")
            #     st.write("UTR Number:", utr_number)
            # else:
            #     st.write("Invalid UTR Number. Please enter 12 digits.")



# def payment_completion(utr_number):
#     # if st.button("Payment Completed"):
#     #     utr_number = st.number_input("Enter UTR Number (12 digits):")
#
#     if len(utr_number) == 12 and utr_number.isdigit():
#         st.success("Payment successful! Order placed successfully.")
#         st.write("UTR Number:", utr_number)
#     else:
#         st.error("Invalid UTR Number. Please enter 12 digits.")
# def payment_page(total_price):
#     st.title("Payment Page")
#
#     st.write("Select Payment Method:")
#     payment_method = st.radio("", ("COD", "Pay Online"))
#
#     if st.button("Confirm Order"):
#         if payment_method == "COD":
#             st.write(f"Pay <h4 style='font-weight: bold; color: blue;'>₹{total_price}</h4> At your door step", unsafe_allow_html=True)
#             st.success("Order placed successfully! Your order will be delivered soon.")
#         elif payment_method == "Pay Online":
#             st.write(f" Payment for <h4 style='font-weight: bold; color: Green;'>₹{total_price}</h4>", unsafe_allow_html=True)
#
#             if 'payment_completed' not in st.session_state:
#                 st.session_state.payment_completed = False
#                 st.session_state.utr_entered = False
#
#             if st.session_state.payment_completed and not st.session_state.utr_entered:
#                 utr_number = st.text_input("Enter UTR Number (12 digits):")
#
#                 if len(utr_number) == 12 and utr_number.isdigit():
#                     st.session_state.utr_entered = True
#                     st.write(f" Payment for <h4 style='font-weight: bold; color: Green;'>₹{total_price}</h4> completed.")
#                     st.success("Order placed successfully! Your order will be delivered soon.")
#                     st.write("UTR Number:", utr_number)
#                 else:
#                     st.error("Invalid UTR Number. Please enter 12 digits.")
#             elif st.session_state.payment_completed and st.session_state.utr_entered:
#                 st.write(f" Payment for <h4 style='font-weight: bold; color: Green;'>₹{total_price}</h4> completed.")
#                 st.success("Order placed successfully! Your order will be delivered soon.")
#                 st.write("UTR Number:", st.session_state.utr_number)
#             else:
#                 # Redirect to payment gateway or display a button to confirm payment
#                 st.write("Redirecting to payment gateway...")
#                 # ... (Optional) Show a placeholder image or loading animation while redirecting
#                 st.image("Payment_settings/Offline Merchant.png")  # Replace with appropriate image
#
#             # Add your payment gateway integration logic here
#             # For example, using a library like `stripe` or `razorpay`
#             # You can use `st.experimental_rerun` to trigger a redirect
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