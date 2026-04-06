import pandas as pd 
import streamlit as st 
from streamlit_option_menu import option_menu
from PIL import Image

#streamlit part
st.set_page_config(layout='wide')
st.title("AIRBNB DATA ANALYSIS")
st.write("")

with st.sidebar:

    select=option_menu("Main Menu",["Home","Data Extraction","About"])

if select=="Home":
    
    image1= Image.open(r"C:\Users\ASUS\Downloads\Airbnb.png")
    st.image(image1)

    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')


    # ---------------- DATA EXTRACTION ---------------- #

if select == "Data Extraction":

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

    # 1️⃣ Price Distribution
    if chart_type == "Price Distribution by Room Type":

        fig, ax = plt.subplots(figsize=(10,6))
        sns.boxplot(data=filtered_df, x="room_type", y="Price", ax=ax)

        ax.set_title("Price Distribution by Room Type")

        st.pyplot(fig)


    # 2️⃣ Property Type Distribution
    elif chart_type == "Property Type Distribution":

        fig, ax = plt.subplots(figsize=(12,6))
        sns.countplot(data=filtered_df, x="Property_type", ax=ax)

        plt.xticks(rotation=45)

        ax.set_title("Property Type Distribution")

        st.pyplot(fig)


    # 3️⃣ Correlation Heatmap
    elif chart_type == "Correlation Heatmap":

        corr = filtered_df.corr(numeric_only=True)

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

        ax.set_title("Correlation Heatmap")

        st.pyplot(fig)


    # 4️⃣ Room Type Distribution
    elif chart_type == "Room Type Distribution":

        room_counts = filtered_df["room_type"].value_counts()

        fig, ax = plt.subplots(figsize=(8,8))

        ax.pie(room_counts, labels=room_counts.index, autopct="%1.1f%%")

        ax.set_title("Room Type Distribution")

        st.pyplot(fig)


    # 5️⃣ Top 10 Neighbourhoods
    elif chart_type == "Top 10 Neighbourhoods":

        top_area = filtered_df["neighbourhood"].value_counts().head(10)

        fig, ax = plt.subplots(figsize=(12,6))

        sns.barplot(x=top_area.index, y=top_area.values, ax=ax)

        plt.xticks(rotation=45)

        ax.set_title("Top 10 Neighbourhoods with Most Listings")

        st.pyplot(fig)


    # 6️⃣ Availability Distribution
    elif chart_type == "Availability Distribution":

        fig, ax = plt.subplots(figsize=(10,6))

        sns.histplot(filtered_df["availability_365"], bins=30, ax=ax)

        ax.set_title("Availability Distribution")

        st.pyplot(fig)


    # 7️⃣ Average Price by Property Type
    elif chart_type == "Average Price by Property Type":

        fig, ax = plt.subplots(figsize=(12,6))

        sns.barplot(data=filtered_df, x="Property_type", y="Price", ax=ax)

        plt.xticks(rotation=45)

        ax.set_title("Average Price by Property Type")

        st.pyplot(fig)

if select=="About":
     

    st.header("ABOUT THIS PROJECT")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')


