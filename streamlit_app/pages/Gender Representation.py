import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data_path = "genders_uc2.csv"  # Update with the correct path to your file
df = pd.read_csv(data_path)
df['date_start'] = pd.to_datetime(df['date_start'])
df['year'] = df['date_start'].dt.year.fillna(0).astype(int)  # Replace NaNs with 0, then convert to int

df = df[(df['year'] >= 2010) & (df['year'] <= 2022)]

# Title and Introduction
st.title("Swiss Parliamentary Gender Representation Analysis")
st.write("""
This dashboard provides an analysis of Swiss parliamentary bills. The visualizations here are designed to help
understand the distribution of bill sponsorship across cantons, the diversity of topics, and gender representation
within parliamentary activities.
""")

# Filters at the top of the main area with dropdown buttons
st.header("Filter Options")
col1, col2 = st.columns(2)

# Select All for Cantons
with col1:
    select_all_cantons = st.checkbox("Select All Cantons", value=True)
    if select_all_cantons:
        selected_cantons = df['canton_name'].unique().tolist()  # Select all cantons
    else:
        selected_cantons = st.multiselect(
            "Canton(s)", options=df['canton_name'].unique(), default=[]
        )

# Select All for Topics
with col2:
    select_all_topics = st.checkbox("Select All Topics", value=True)
    if select_all_topics:
        selected_topics = df['topic'].unique().tolist()  # Select all topics
    else:
        selected_topics = st.multiselect(
            "Topic(s)", options=df['topic'].unique(), default=[]
        )

# Filter the dataframe based on selections
filtered_df = df[(df['canton_name'].isin(selected_cantons)) & (df['topic'].isin(selected_topics))]

# Gender Representation by Year (Line Chart)
st.subheader("Gender Representation in the Bills Over Time")
year_gender = filtered_df.groupby(['year', 'person_gender']).size().reset_index(name='count')
fig3 = px.line(year_gender, x='year', y='count', color='person_gender', title="Gender Representation per Year")
st.plotly_chart(fig3)

# Multiselect to select multiple years for the pie chart
st.subheader("Gender Representation for Selected Years")
available_years = sorted(df['year'].unique())
selected_years = st.multiselect("Select Year(s)", options=available_years, default=[available_years[-1]])

# Pie Chart for Gender Representation in the Selected Years
df_selected_years = filtered_df[filtered_df['year'].isin(selected_years)]
gender_selected_years = df_selected_years['person_gender'].value_counts().reset_index()
gender_selected_years.columns = ['person_gender', 'count']
fig_pie = px.pie(gender_selected_years, names='person_gender', values='count', 
                 title=f"Gender Representation in Selected Years: {', '.join(map(str, selected_years))}")
st.plotly_chart(fig_pie)
# Display DataFrame and Download Option
st.subheader("Data Table and Source")
st.dataframe(filtered_df)
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_swiss_parliament_data.csv",
    mime="text/csv",
)
