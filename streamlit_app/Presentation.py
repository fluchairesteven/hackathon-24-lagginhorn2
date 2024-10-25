import streamlit as st

# Title and Introduction
st.title("🇨🇭 Swiss Parliament Knowledge Graph Visualization 🌐")
st.write("""
Welcome to the **Swiss Parliament Knowledge Graph Viz** project! This dashboard is designed to explore data insights and demonstrate use cases from the Swiss parliamentary data, all made possible through the Demoscrasci knowledge graph. 🚀

### 📊 Data as a Starting Point
At the core of this project, we leverage Swiss parliamentary data from **Luis Salamanca's** previous work, ensuring a strong foundation built on **Demoscrasci** data. Through this information-rich dataset, we’re able to connect relationships, visualize data, and uncover patterns within parliamentary activities.

### 🧠 Knowledge Graph Powered Insights
Using **Neo4j Knowledge Graph**, we've structured and connected parliamentary data to provide a more meaningful understanding of the Swiss Parliament. The knowledge graph approach allows us to explore:
- **How parliamentary bills and topics are related**, 
- **The relationships between people and cantons**, 
- **Key insights on gender representation**, and much more.
""")

# Display Knowledge Graph Image (with a smaller width)
st.image("https://democrasci.jkminder.ch/_images/tikz_KG.svg", caption="Swiss Parliament Knowledge Graph Visualization", width=400)

st.write("""
### 🎯 Achievements and Use Cases
The Swiss Parliament Knowledge Graph has achieved significant milestones, including:
- **Enhanced Data Relationships**: Connect people, bills, topics, and cantons for deeper insights. 📈
- **Topic Trends and Patterns**: Explore topic trends over time and see which issues have gained or lost focus. 📅
- **Gender Representation Analysis**: See how gender representation evolves across cantons, years, and topics. 👩‍⚖️👨‍⚖️

### 🛠️ Explore the Dashboard
Check out the **interactive visualizations and data exploration tools** available here! Whether you're interested in historical trends, gender analysis, or relationship mapping within the Swiss Parliament, this dashboard offers a hands-on way to understand the data and the insights within it.

Thank you for exploring the Swiss Parliament Knowledge Graph with us! 🙌
""")
