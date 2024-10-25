Exploring and visualizing regional politics in Switzerland
---

_“Kümmern Sie sich um meine Region? Bien sûr, la tua e tutte le altre, ed da tut la Svizra”_

Created for Challenge 5.2 at the [SDSC Hackathon](https://sdsc-hackathons.ch/) on October 24-25, 2024

Team: Simon, Adrien, Steven, Nejma, Oleg

Presentation: [Slides on HackMD](https://hackmd.io/@oleg/rk_1gAuxyx#/)

# Challenge

To improve understanding of **Swiss parliamentary decisions** using **Open Research Data** & shared platforms for **Data Science**.

![DemocraSci logo](https://hackmd.io/_uploads/H150QkteJl.png)

# Solution

We worked as a team to obtain, explore and visualize the data. Our main collaboration tools were the Renku platform, as well as GitHub and Discord. The OpenAI and Cohere GPT systems were used for code assistance. We also used HackMD and Excalidraw for this presentation.

### 1. Data collection and access

_A graph-based information extraction pipeline_

![1000030608](https://hackmd.io/_uploads/r1ckOkKlJe.jpg)

The data from Swiss parliamentary APIs was extracted by the DemocraSci team and utilized to build a knowledge graph, creating a powerful resource for understanding the complex relationships between parliamentary entities. 

Neo4j, a leading graph database, is used to model and query these relationships efficiently. The knowledge graph captures connections between politicians, parties, bills, and regions, enabling us to analyze and visualize the impact of decisions on a regional level.

A copy of this database has been published on Zenodo, and imported into an S3 bucket for processing at the hackathon.

### 2. Impact Analysis

By leveraging the Cypher query language, we extract relevant metadata, including topics, entities, and relationships. A detailed data schema is available online from the DemocraSci project.

![Screenshot fo Neo4j](https://hackmd.io/_uploads/S15ez1tgJg.png)

### 3. Knowledge Graph Enrichment

This pipeline forms the foundation for our knowledge graph, providing a structured representation of parliamentary data.

---

4. Visual Exploration Dashboard

---

5. Reusability and Next Steps

- 1 minute to present and then walk-around demo
- Share documentation via public GitHub

---


Slide 4: Visualization and Insights

To make our findings accessible and engaging, we develop a dashboard or web application for visualization. This tool allows users to explore the enriched knowledge graph, gaining valuable insights into the impact of parliamentary decisions. Interactive visualizations, such as maps and charts, provide a clear understanding of how different regions are affected by specific bills and policies. Our goal is to facilitate a deeper understanding of the Swiss political system and its regional implications.

Slide 5: Impact and Future Directions

By completing this project, we aim to contribute to a more informed and engaged public discourse. Our knowledge graph and visualization tools provide a powerful resource for journalists, researchers, and policymakers, enabling them to make data-driven decisions. Looking ahead, we plan to continue enhancing our methods and tools, ensuring their adaptability and scalability. We believe that our project has the potential to shape future research and policy-making, ultimately leading to more effective and responsive governance in Switzerland.

