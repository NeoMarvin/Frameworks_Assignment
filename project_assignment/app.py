# app.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="COVID-19 Recoveries Explorer", layout="wide")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("region_date_metadata.csv")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    return df

df = load_data()

st.title("COVID-19 Recoveries Explorer 🌍")
st.write("Explore recoveries per region over time.")

# --- SIDEBAR FILTERS ---
regions = df["Country_Region"].unique()
selected_region = st.sidebar.selectbox("Select Country/Region", regions)

# Filter data by selection
filtered_df = df[df["Country_Region"] == selected_region]

# --- DATA OVERVIEW ---
st.subheader(f"Data Overview for {selected_region}")
st.dataframe(filtered_df)

st.write("Summary Statistics:")
st.write(filtered_df["Recoveries"].describe())

# --- VISUALIZATIONS ---

# 1. Line chart: Recoveries over time
st.subheader("Recoveries Over Time")
daily_recoveries = filtered_df.groupby("Date")["Recoveries"].sum()
st.line_chart(daily_recoveries)

# 2. Bar chart: Top provinces/states by average recoveries
st.subheader("Top Provinces/States by Average Recoveries")
avg_province = filtered_df.groupby("Province_State")["Recoveries"].mean().sort_values(ascending=False)
st.bar_chart(avg_province.head(10))

# 3. Histogram: Distribution of recoveries
st.subheader("Distribution of Recoveries")
st.bar_chart(filtered_df["Recoveries"].value_counts().sort_index())

# 4. Scatter plot: Date vs Recoveries
st.subheader("Scatter Plot: Date vs Recoveries")
fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(filtered_df["Date"], filtered_df["Recoveries"], alpha=0.5)
ax.set_xlabel("Date")
ax.set_ylabel("Recoveries")
ax.set_title(f"Recoveries Over Time in {selected_region}")
st.pyplot(fig)
