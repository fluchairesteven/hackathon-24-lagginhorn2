import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import pandas as pd
import branca

# Load GeoJSON file
gdf = gpd.read_file("swissBOUNDARIES3D_1_3_TLM_KANTONSGEBIET.geojson")

# Load CSV data
df = pd.read_csv("uc1_9713.csv")

# Mapping dictionary for canton names
map_canton_names = {
    "GraubÃ¼nden": "Graubünden",
    "Bern": "Bern",
    "Valais": "Wallis",
    "Vaud": "Waadt",
    "Ticino": "Tessin",
    "St. Gallen": "St. Gallen",
    "ZÃ¼rich": "Zürich",
    "Fribourg": "Freiburg",
    "Luzern": "Luzern",
    "Aargau": "Aargau",
    "Uri": "Uri",
    "Thurgau": "Thurgau",
    "Schwyz": "Schwyz",
    "Jura": "Jura",
    "NeuchÃ¢tel": "Neuenburg",
    "Neuenburg": "Neuenburg",
    "Neuchâtel": "Neuenburg",
    "Solothurn": "Solothurn",
    "Glarus": "Glarus",
    "Basel-Landschaft": "Basel-Landschaft",
    "Obwalden": "Obwalden",
    "Nidwalden": "Nidwalden",
    "GenÃ¨ve": "Genf",
    "Schaffhausen": "Schaffhausen",
    "Appenzell Ausserrhoden": "Appenzell A.-Rh.",
    "Zug": "Zug",
    "Appenzell Innerrhoden": "Appenzell I.-Rh."
}

# Standardize canton names in the GeoDataFrame using the mapping dictionary
gdf['NAME'] = gdf['NAME'].replace(map_canton_names)

# Calculate gender ratio by canton
gender_ratio = df.groupby("canton_name")["person_gender"].apply(lambda x: (x == "f").sum() / len(x)).reset_index()
gender_ratio.columns = ['canton_name', 'female_ratio']

# Calculate number of bills by canton
bill_count = df.groupby("canton_name")["bill_id"].count().reset_index()
bill_count.columns = ['canton_name', 'number_of_bills']

# Merge gender ratio and bill count with GeoDataFrame
gdf = gdf.merge(gender_ratio, left_on="NAME", right_on="canton_name", how='left')
gdf = gdf.merge(bill_count, left_on="NAME", right_on="canton_name", how='left')

# Create a linear colormap from blue to pink (reversed)
colormap_gender = branca.colormap.LinearColormap(
    colors=['#0000ff', '#ff69b4'],  # Blue to Pink for gender ratio
    vmin=gdf['female_ratio'].min(),
    vmax=gdf['female_ratio'].max(),
    caption='Female Representation Ratio'
)

colormap_bills = branca.colormap.LinearColormap(
    colors=['#ffffff', '#ffcc00'],  # White to Yellow for number of bills
    vmin=gdf['number_of_bills'].min(),
    vmax=gdf['number_of_bills'].max(),
    caption='Number of Bills'
)
st.title("Cantons Overview")
st.write("""
This dashboard shows the bills supported directly by the Cantons and also the gender ratio per Cantons
""")

# Create base map with a simpler background
m = folium.Map(location=[46.8182, 8.2275], zoom_start=7.2, tiles="CartoDB positron")

# Streamlit selection for metric to display
metric = st.selectbox("Select Metric to Display", ["Gender Equality Ratio", "Number of Bills"])

if metric == "Gender Equality Ratio":
    folium.GeoJson(
        gdf,
        style_function=lambda feature: {
            'fillColor': colormap_gender(feature['properties']['female_ratio']) if feature['properties']['female_ratio'] is not None else '#ffffff',
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0.7,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["NAME", "female_ratio"],
            aliases=["Canton", "Female Ratio"],
            localize=True,
            sticky=False,
            labels=True,
            style="""
                background-color: #F0EFEF;
                border: 2px solid black;
                border-radius: 3px;
                box-shadow: 3px;
            """,
            max_width=800,
        )
    ).add_to(m)
    
    m.add_child(colormap_gender)

else:
    folium.GeoJson(
        gdf,
        style_function=lambda feature: {
            'fillColor': colormap_bills(feature['properties']['number_of_bills']) if feature['properties']['number_of_bills'] is not None else '#ffffff',
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0.7,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["NAME", "number_of_bills"],
            aliases=["Canton", "Number of Bills"],
            localize=True,
            sticky=False,
            labels=True,
            style="""
                background-color: #F0EFEF;
                border: 2px solid black;
                border-radius: 3px;
                box-shadow: 3px;
            """,
            max_width=800,
        )
    ).add_to(m)
    
    m.add_child(colormap_bills)

# Display the map in Streamlit
folium_static(m)

# Additional Information
st.subheader("Interpretation")
if metric == "Gender Equality Ratio":
    st.write("This map shows the ratio of female representation in political bills across Swiss cantons. Colors vary from blue (lower female representation) to pink (higher female representation), indicating levels of gender equality in political participation.")
    st.subheader("Top 5 Cantons with Highest Female Representation")
    top_5_gender = gender_ratio.sort_values(by='female_ratio', ascending=False).head(5)
    st.table(top_5_gender)

    st.subheader("Bottom 5 Cantons with Lowest Female Representation")
    bottom_5_gender = gender_ratio.sort_values(by='female_ratio').head(5)
    st.table(bottom_5_gender)
    filtered_df = gender_ratio.sort_values(by='female_ratio', ascending=False)

else:
    st.write("This map shows the number of bills per canton. Colors vary from white (fewer bills) to yellow (more bills), indicating legislative activity.")
    st.subheader("Top 5 Cantons with Most Bills")
    top_5_bills = bill_count.sort_values(by='number_of_bills', ascending=False).head(5)
    st.table(top_5_bills)

    st.subheader("Bottom 5 Cantons with Fewest Bills")
    bottom_5_bills = bill_count.sort_values(by='number_of_bills').head(5)
    st.table(bottom_5_bills)
    filtered_df = bill_count.sort_values(by='number_of_bills', ascending=False)



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