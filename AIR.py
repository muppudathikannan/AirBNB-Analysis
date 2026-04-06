import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# page config
st.set_page_config(layout="wide")

st.title("AIRBNB DATA ANALYSIS")

# load dataset
df = pd.read_csv("AIRBNB.csv")

# sidebar
with st.sidebar:
    select = option_menu("Main Menu",["Home","Data Visualization","About"])

# ---------------- HOME ---------------- #

if select=="Home":

    image1 = Image.open(r"C:\Users\ASUS\Downloads\Airbnb.png")
    st.image(image1)

    st.header("About Airbnb")

    st.write("""Airbnb is an online marketplace that connects people who want to rent out
    their property with people who are looking for accommodations for short stays.""")

# ---------------- DATA EXTRACTION ---------------- #

if select == "Data Visualization":

    st.header("Airbnb Data Visualization")

    # Country Filter
    country = st.selectbox("Select Country", df["Country"].unique())

    filtered_df = df[df["Country"] == country]

    # Visualization Selector
    chart_type = st.selectbox(
        "Select Visualization",
        [
            "Price Distribution by Room Type",
            "Property Type Distribution",
            "Correlation Heatmap",
            "Room Type Distribution",
            "Top 10 Neighbourhoods",
            "Availability Distribution",
            "Average Price by Property Type"
        ]
    )

    # Price Distribution
    if chart_type == "Price Distribution by Room Type":

        fig, ax = plt.subplots(figsize=(10,6))
        sns.boxplot(data=filtered_df, x="room_type", y="Price", ax=ax)

        ax.set_title("Price Distribution by Room Type")

        st.pyplot(fig)


    # Property Type Distribution
    elif chart_type == "Property Type Distribution":

        fig, ax = plt.subplots(figsize=(12,6))
        sns.countplot(data=filtered_df, x="Property_type", ax=ax)

        plt.xticks(rotation=45)

        ax.set_title("Property Type Distribution")

        st.pyplot(fig)


    # Correlation Heatmap
    elif chart_type == "Correlation Heatmap":

        corr = filtered_df.corr(numeric_only=True)

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

        ax.set_title("Correlation Heatmap")

        st.pyplot(fig)


    # Room Type Distribution
    elif chart_type == "Room Type Distribution":

        room_counts = filtered_df["room_type"].value_counts()

        fig, ax = plt.subplots(figsize=(8,8))

        ax.pie(room_counts, labels=room_counts.index, autopct="%1.1f%%")

        ax.set_title("Room Type Distribution")

        st.pyplot(fig)


    # Top 10 Neighbourhoods
    elif chart_type == "Top 10 Neighbourhoods":

        top_area = filtered_df["neighbourhood"].value_counts().head(10)

        fig, ax = plt.subplots(figsize=(12,6))

        sns.barplot(x=top_area.index, y=top_area.values, ax=ax)

        plt.xticks(rotation=45)

        ax.set_title("Top 10 Neighbourhoods with Most Listings")

        st.pyplot(fig)


    # Availability Distribution
    elif chart_type == "Availability Distribution":

        fig, ax = plt.subplots(figsize=(10,6))

        sns.histplot(filtered_df["availability_365"], bins=30, ax=ax)

        ax.set_title("Availability Distribution")

        st.pyplot(fig)


    # Average Price by Property Type
    elif chart_type == "Average Price by Property Type":

        fig, ax = plt.subplots(figsize=(12,6))

        sns.barplot(data=filtered_df, x="Property_type", y="Price", ax=ax)

        plt.xticks(rotation=45)

        ax.set_title("Average Price by Property Type")

        st.pyplot(fig)


# ---------------- ABOUT ---------------- #

if select=="About":

    st.header("About this Project")

    st.write("This project analyzes Airbnb data using Python, Pandas, and visualization libraries.")