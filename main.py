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
import streamlit as st

def home():
    st.title("Home Page")

    # Select location
    location = st.selectbox("Choose your location", locations_dict)
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
            st.write(f"Payment for  <h4 style='font-weight: bold; color: Green;'>₹{total_price}</h4> ",
                     unsafe_allow_html=True)
            st.write("Redirecting to payment gateway...")

            st.image("Payment_settings/Offline Merchant.png")  # Display the image

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