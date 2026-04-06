import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(layout="wide")

st.title("AIRBNB DATA ANALYSIS")
st.write("")

# Load dataset
df = pd.read_csv("AIRBNB.csv")

# Sidebar menu
with st.sidebar:
    select = option_menu(
        "Main Menu",
        ["Home", "Data Extraction", "About"]
    )

# ---------------- HOME ---------------- #

if select == "Home":

    image1 = Image.open(r"C:\Users\ASUS\Downloads\Airbnb.png")
    st.image(image1)

    st.header("About Airbnb")

    st.write("""Airbnb is an online marketplace that connects people who want to rent out
    their property with people who are looking for accommodations for short stays.
    Airbnb allows hosts to earn income from their property and guests to find affordable
    and unique accommodations.""")

    st.write("""Airbnb operates a platform where users can list and book accommodations
    including apartments, homestays, vacation rentals, treehouses, castles, and hotels.
    The company operates in many countries around the world and is headquartered in
    San Francisco, USA.""")

    st.header("Background of Airbnb")

    st.write("""Airbnb started in 2007 when two hosts welcomed three guests to their home
    in San Francisco. Today it has grown to millions of hosts worldwide and billions of
    guest arrivals across almost every country.""")

# ---------------- DATA EXTRACTION ---------------- #

if select == "Data Extraction":

    st.header("Airbnb Data Analysis")

    # ---------- MAP PLOT ---------- #

    st.subheader("1. Airbnb Locations Around the World")

    fig1 = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="Country",
        size="review_score",
        hover_name="Name",
        hover_data=["Price", "room_type", "review_score"],
        zoom=2
    )

    fig1.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig1, use_container_width=True)

    # ---------- BOX PLOT (PLOTLY) ---------- #

    st.subheader("2. Price Variation by Country and Property Type")

    fig2 = px.box(
        df,
        x="Country",
        y="Price",
        color="room_type",
        title="Price Variation by Location and Property Type"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ---------- SEASON CREATION ---------- #

    df["month"] = pd.to_datetime(df["last_review"]).dt.month

    df["season"] = df["month"].map({
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Spring", 4: "Spring", 5: "Spring",
        6: "Summer", 7: "Summer", 8: "Summer",
        9: "Autumn", 10: "Autumn", 11: "Autumn"
    })

    availability_season = df.groupby("season")["availability_365"].mean().reset_index()

    # ---------- LINE PLOT ---------- #

    st.subheader("3. Average Airbnb Availability by Season")

    fig3 = px.line(
        availability_season,
        x="season",
        y="availability_365",
        markers=True,
        title="Average Airbnb Availability by Season"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # ---------- SEABORN BOXPLOT ---------- #

    st.subheader("4. Price Variation by Room Type")

    fig4, ax = plt.subplots()

    sns.boxplot(
        x="room_type",
        y="Price",
        data=df,
        ax=ax
    )

    ax.set_title("Price Variation by Room Type")

    st.pyplot(fig4)

    # ---------- SCATTER PLOT ---------- #

    st.subheader("5. Price vs Review Score")

    fig5, ax = plt.subplots()

    sns.scatterplot(
        x="review_score",
        y="Price",
        data=df,
        ax=ax
    )

    ax.set_title("Price vs Review Score")

    st.pyplot(fig5)

# ---------------- ABOUT ---------------- #

if select == "About":

    st.header("ABOUT THIS PROJECT")

    st.subheader("1. Data Collection")
    st.write("Gather Airbnb data including listings, hosts, pricing, and reviews.")

    st.subheader("2. Data Cleaning")
    st.write("Handle missing values, remove duplicates, and standardize formats.")

    st.subheader("3. Exploratory Data Analysis")
    st.write("Analyze patterns, trends, and relationships in Airbnb listings.")

    st.subheader("4. Visualization")
    st.write("Use charts and graphs to present key insights from the data.")

    st.subheader("5. Geospatial Analysis")
    st.write("Understand geographic distribution of Airbnb listings using maps.")