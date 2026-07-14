
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("MatSyn25 Process Discovery Tool")

st.write(
    "Interactive synthesis discovery system for MXenes, TMDs, and Graphene materials."
)


# Load datasets

motifs = pd.read_csv(
    '/content/family_method_motifs.csv'
)

hypothesis = pd.read_csv(
    '/content/hypothesis_cards.csv'
)

summary = pd.read_csv(
    '/content/dashboard_summary.csv'
)


st.sidebar.header("Filters")

families = motifs['assigned_family'].unique()

selected_family = st.sidebar.selectbox(
    "Select Family",
    families
)


filtered_df = motifs[
    motifs['assigned_family']
    == selected_family
]

st.subheader("Filtered Motifs")

st.dataframe(
    filtered_df.head(20)
)


fig = px.bar(
    filtered_df.head(10),
    x='methods_found_str',
    y='count',
    title='Top Synthesis Methods'
)

st.plotly_chart(fig)


st.subheader("Hypothesis Cards")

st.dataframe(hypothesis)


st.subheader("Project Summary")

st.dataframe(summary)
