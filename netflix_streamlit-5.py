# -*- coding: utf-8 -*-
"""Netflix_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XQUgViJ9mFtz_A_kp0QuHfWdeNKPLhRk
"""

!pip install streamlit
!pip install pyngrok

# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

df = pd.read_csv('netflix_titles.csv')
df

# Commented out IPython magic to ensure Python compatibility.
# %%writefile streamlit_app.py
# import streamlit as st
# import pandas as pd
# import altair as alt
# import plotly.express as px
# 
# # Set up the dashboard layout
# st.set_page_config(
#     page_title="Netflix Dashboard",
#     page_icon="🎬",
#     layout="wide"
# )
# 
# st.title("🎬 Netflix Dashboard")
# st.write("📊 An interactive dashboard analyzing Netflix content trends.")
# 
# # Load dataset
# @st.cache_data
# def load_data():
#     df = pd.read_csv("netflix_titles.csv")  # Ensure this file is uploaded
#     return df
# 
# df = load_data()
# 
# # **CLEANING DATASET**
# # 1️⃣ Identify incorrect rating values (entries with "min" instead of rating)
# invalid_rows = df[df["rating"].str.contains("min", na=False)]
# 
# # 2️⃣ Move incorrect ratings to the duration column
# df.loc[invalid_rows.index, "duration"] = df.loc[invalid_rows.index, "rating"]
# 
# # 3️⃣ Replace incorrect ratings with NaN
# df.loc[invalid_rows.index, "rating"] = None
# 
# # 4️⃣ Fill missing ratings with "Unknown"
# df.fillna({"rating": "Unknown", "country": "Unknown"}, inplace=True)
# 
# # **New Cleaned DataFrame for Movies**
# df_movies1 = df[df["type"] == "Movie"]
# df_movies1["duration_min"] = df_movies1["duration"].str.extract(r'(\d+)').astype(float)
# 
# # 🎯 **Color Theme Selection**
# color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
# selected_color_theme = st.selectbox("🎨 Select a Color Theme", color_theme_list, index=0)
# 
# # 📊 **1. Bar Graph for Movies vs. TV Shows**
# type_counts = df["type"].value_counts().reset_index()
# type_counts.columns = ["Type", "Count"]
# 
# bar_movies_tv = alt.Chart(type_counts).mark_bar().encode(
#     x=alt.X("Type:N", title="Content Type"),
#     y=alt.Y("Count:Q", title="Count"),
#     color=alt.Color("Type:N", scale=alt.Scale(scheme="category10")),
#     tooltip=["Type", "Count"]
# ).properties(
#     title="Movies vs. TV Shows",
#     width=350,
#     height=350
# )
# 
# # 📊 **2. Bar Graph for Top 10 Rated Movies**
# top_rated = df_movies1.groupby("rating")["title"].count().reset_index()
# top_rated.columns = ["Rating", "Movie Count"]
# top_rated = top_rated.sort_values(by="Movie Count", ascending=False).head(10)
# 
# bar_top_rated = alt.Chart(top_rated).mark_bar().encode(
#     x=alt.X("Rating:N", title="Rating", sort="-y"),
#     y=alt.Y("Movie Count:Q", title="Number of Movies"),
#     color=alt.Color("Rating:N", scale=alt.Scale(scheme="category10")),
#     tooltip=["Rating", "Movie Count"]
# ).properties(
#     title="Top 10 Rated Movies",
#     width=350,
#     height=350
# )
# 
# # 🌎 **3. Choropleth Map for Netflix Content by Country**
# df_exploded = df.assign(country=df["country"].str.split(",")).explode("country")
# df_exploded["country"] = df_exploded["country"].str.strip()
# country_counts = df_exploded["country"].value_counts().reset_index()
# country_counts.columns = ["Country", "Count"]
# 
# choropleth = px.choropleth(
#     country_counts,
#     locations="Country",
#     locationmode="country names",
#     color="Count",
#     color_continuous_scale=selected_color_theme,
#     labels={"Count": "Number of Titles"},
#     title="Netflix Content by Country"
# )
# choropleth.update_layout(margin=dict(l=0, r=0, t=30, b=0), height=350)
# 
# # **🎨 Organizing Layout (3 Columns x 1 Row)**
# col1, col2, col3 = st.columns(3)
# 
# with col1:
#     st.altair_chart(bar_movies_tv, use_container_width=True)
# 
# with col2:
#     st.altair_chart(bar_top_rated, use_container_width=True)
# 
# with col3:
#     st.plotly_chart(choropleth, use_container_width=True)
#

!streamlit run streamlit_app.py &>/dev/null &

!ngrok authtoken 2sbhzmMrnAYf8oLLhxH2dS4xjWP_22g48Z2zX4pScYfuKVTfV

from pyngrok import ngrok

# Open a tunnel explicitly for HTTP
public_url = ngrok.connect("8501", "http")
print(f"Public URL: {public_url}")