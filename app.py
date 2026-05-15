import streamlit as st
import pandas as pd
import os

st.title("🎒 Campus Lost & Found System")

menu = ["Home", "Report Lost Item", "Report Found Item", "View Lost Items", "View Found Items"]

choice = st.sidebar.selectbox("Menu", menu)

# Create CSV files if not exist
if not os.path.exists("lost_items.csv"):
    pd.DataFrame(columns=["Name", "Item", "Location", "Contact"]).to_csv("lost_items.csv", index=False)

if not os.path.exists("found_items.csv"):
    pd.DataFrame(columns=["Name", "Item", "Location", "Contact"]).to_csv("found_items.csv", index=False)

# Home Page
if choice == "Home":
    st.header("Welcome!")
    st.write("This project helps students report and search lost items.")

# Report Lost Item
elif choice == "Report Lost Item":
    st.header("Report Lost Item")

    name = st.text_input("Your Name")
    item = st.text_input("Lost Item")

    category = st.selectbox(
       "Category",
       ["Electronics", "Books", "Bottle", "Bag", "ID Card", "Others"]
)
    location = st.text_input("Lost Location")
    contact = st.text_input("Contact Number")

    if st.button("Submit Lost Item"):
        new_data = pd.DataFrame([[name, item, location, contact]],
                                columns=["Name", "Item", "Location", "Contact"])

        new_data.to_csv("lost_items.csv", mode='a', header=False, index=False)

        st.success("Lost item reported successfully!")

# Report Found Item
elif choice == "Report Found Item":
    st.header("Report Found Item")

    name = st.text_input("Finder Name")
    item = st.text_input("Found Item")
    location = st.text_input("Found Location")
    contact = st.text_input("Contact Number")

    if st.button("Submit Found Item"):
        new_data = pd.DataFrame([[name, item, location, contact]],
                                columns=["Name", "Item", "Location", "Contact"])

        new_data.to_csv("found_items.csv", mode='a', header=False, index=False)

        st.success("Found item reported successfully!")

# View Lost Items
elif choice == "View Lost Items":
    st.header("Lost Items")

    data = pd.read_csv("lost_items.csv")
    st.dataframe(data)

# View Found Items
elif choice == "View Found Items":
    st.header("Found Items")

    data = pd.read_csv("found_items.csv")
    st.dataframe(data)