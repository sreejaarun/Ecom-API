import streamlit as st
import pandas as pd
import os

# Mock product data
products_data = {
    'Product Name': ['Product 1', 'Product 2', 'Product 3'],
    'Description': ['Description 1', 'Description 2', 'Description 3'],
    'Price': [100.0, 200.0, 150.0]
}

# Mock product reviews data
reviews_data = {
    'Product Name': ['Product 1', 'Product 1', 'Product 2'],
    'Rating': [4, 5, 3],
    'Comment': ['Good product', 'Excellent!', 'Could be better']
}

# Create DataFrames
products_df = pd.DataFrame(products_data)
reviews_df = pd.DataFrame(reviews_data)

# Sidebar - User registration and login (mocked)
st.sidebar.header("User Authentication")

# Mock user registration
if st.sidebar.button("Register"):
    st.sidebar.text("User registration form (not implemented)")

# Mock user login
if st.sidebar.button("Login"):
    st.sidebar.text("User login form (not implemented)")

# Main content - Product listing
st.title("E-commerce App")

st.header("Product Listing")
st.table(products_df)

# Product review section
st.header("Product Reviews")

# Select a product for review
selected_product = st.selectbox("Select a product:", products_df["Product Name"])

if selected_product:
    st.subheader(f"Reviews for {selected_product}")
    product_reviews = reviews_df[reviews_df["Product Name"] == selected_product]
    st.table(product_reviews)

# Review submission form (mocked)
if st.button("Submit Review"):
    st.text("Review submission form (not implemented)")

# Pagination (mocked)
st.header("Pagination")
page = st.slider("Page", 1, 10, 1)
st.text(f"Showing products on page {page}")

# Product upload (CSV files)
st.header("Product Upload (CSV)")

# Allow the user to upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Admin section (mocked)
if st.sidebar.checkbox("Admin Panel"):
    st.sidebar.text("Admin panel (not implemented)")

# Logout (mocked)
if st.sidebar.button("Logout"):
    st.sidebar.text("User logout (not implemented)")
