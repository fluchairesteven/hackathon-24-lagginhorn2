import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data_path = "genders_uc2.csv"  # Update with the correct path to your file
df = pd.read_csv(data_path)
df['date_start'] = pd.to_datetime(df['date_start'])
df = df.dropna(subset=['date_start'])  # Drop rows with missing date_start values
df['year'] = df['date_start'].dt.year.astype(int)  # Ensure year is integer

# Filter data between 2010 and 2022
df = df[(df['year'] >= 2009) & (df['year'] <= 2022)]

# Title and Introduction
st.title("Topics Over Time in Swiss Parliamentary Bills")
st.write("""
This dashboard analyzes the trends of various topics discussed in Swiss parliamentary bills over time. 
You can use the filters below to explore how different topics have evolved from 2010 to 2022.
""")

# Filter Options
st.header("Filter Options")
col1, col2 = st.columns(2)

# Select Topics
with col1:
    select_all_topics = st.checkbox("Select All Topics", value=True)
    if select_all_topics:
        selected_topics = df['topic'].unique().tolist()  # Select all topics
    else:
        selected_topics = st.multiselect(
            "Topic(s)", options=df['topic'].unique(), default=[]
        )

# Select Years
with col2:
    available_years = sorted(df['year'].unique())
    selected_years = st.slider(
        "Select Year Range", min_value=available_years[0], max_value=available_years[-1],
        value=(available_years[0], available_years[-1]), step=1
    )

# Filter data based on selections
filtered_df = df[(df['topic'].isin(selected_topics)) & (df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

# Topic Trends Over Time (Line Chart)
st.subheader("Topic Trends Over Time")
topic_trend = filtered_df.groupby(['year', 'topic']).size().reset_index(name='count')
fig = px.line(topic_trend, x='year', y='count', color='topic', title="Trends of Topics Over Time", width=850, height=600)
st.plotly_chart(fig)

# Display DataFrame and Download Option
st.subheader("Data Table and Source")
st.dataframe(filtered_df)
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_topic_trends_swiss_parliament.csv",
    mime="text/csv",
)
