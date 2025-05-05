import streamlit as st
import pandas as pd
import plotly.express as px

# Configure page
st.set_page_config(page_title="Poweshiek County Dashboard", layout="wide")

# Add title and banner
st.markdown(
    "<h1 style='text-align: center; color: navy;'> Poweshiek County Dashboard</h1>",
    unsafe_allow_html=True,
)

# KPI cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Population", "18,662")
col2.metric("Median Income", "$64,837")
col3.metric("Poverty Rate", "10.3%")
col4.metric("Broadband Access", "83.4%")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Demographics", "Environment", "Community Assets", "Geography"])

# Demo DataFrames
demo_percent_data = pd.DataFrame({
    'Category': ['Computer Access', 'Broadband Access', 'Poverty Rate',
                 'Disability <65', 'No Insurance', 'High School+', 'Bachelor’s+'],
    'Value': [93.6, 83.4, 10.3, 9.1, 4.5, 94.6, 28.2]
})

edu_data = pd.DataFrame({'Education': ['High School+', 'Below High School'], 'Percentage': [94.6, 5.4]})

env_data = pd.DataFrame({
    'Issue': ['Industry Contamination', 'Water Quality', 'Air Quality', 'Pesticides'],
    'Severity': [80, 90, 75, 70]
})

asset_data = pd.DataFrame({
    'Asset Type': ['Associations', 'Institutions', 'Individuals', 'Online Resources'],
    'Count': [4, 3, 4, 4]
})

city_data = pd.DataFrame({
    'City': ['Grinnell', 'Brooklyn', 'Montezuma', 'Victor'],
    'Population': [9564, 1502, 1442, 875]
})

# Detailed assets table data
detailed_asset_table = pd.DataFrame({
    'Category': ['Physical Space'] * 4 + ['Individuals'] * 4 + ['Associations'] * 11 +
                ['Online Resources'] * 8 + ['Institutions'] * 2 + ['Economy'] * 3,
    'Item': [
        'Drake Community Library', 'Conard Environmental Research Area (CERA)',
        'Jacob Krumm Nature Preserve', 'Uhlenhop Arboretum',
        'JD Griffith', 'Poweshiek Board of Conservation',
        'Poweshiek Board of Health', 'Jon Andelson and Tommy Hexter (CARES)',
        'Iowa Environmental Council', 'Iowa Faith and Climate Network',
        'Iowa Alliance for Responsible Agriculture', 'Jefferson County Farmers and Neighbors',
        'Socially Responsible Agriculture Project', 'Iowa Citizens for Community Improvement',
        'Izaak Walton League', 'Food and Water Watch',
        'Poweshiek County Soil and Water Conservation', 'Poweshiek CARES',
        'Imagine Grinnell',
        'Purple Air Quality Monitoring', 'EWG Tap Water Database', 'EPA Superfund Site',
        'IEC Environmental Justice Map', 'Izaak Walton League Nitrate Map',
        'Get into Grinnell Blog', 'Grinnell Flash News', 'Advocacy Toolkit',
        'Air Monitoring Summer Project', 'Working on..',
        'Iowa State Revolving Funds (SRF)', 'Lead Service Lines Replacement',
        'Center for Industrial Research and Service'
    ]
})

# Demographics Tab
with tab1:
    st.subheader("Demographic Indicators")
    st.write("A snapshot of Poweshiek County’s technology access, poverty levels, disability rates, insurance coverage, and educational attainment.")

    percent_fig = px.bar(demo_percent_data, x='Category', y='Value', text='Value',
                         title='Demographic Percentages', range_y=[0, 100])
    st.plotly_chart(percent_fig, use_container_width=True)

    st.metric("Median Income", "$64,837")

    st.write("Education levels show the county’s strength in high school graduation, with a smaller portion holding bachelor’s degrees or higher.")

    pie_fig = px.pie(edu_data, names='Education', values='Percentage',
                     title='Education Levels', hole=0.4)
    st.plotly_chart(pie_fig, use_container_width=True)

# Environment Tab
with tab2:
    st.subheader("Environmental Concerns")
    st.write("Key environmental challenges in Poweshiek County, with water quality and industry contamination ranked as top priorities.")

    env_fig = px.bar(env_data, x='Issue', y='Severity', color='Severity', text='Severity',
                     title='Environmental Challenges')
    st.plotly_chart(env_fig, use_container_width=True)

# Community Assets Tab
with tab3:
    st.subheader("Community Assets")
    st.write("An overview of the county’s strong network of associations, institutions, individuals, and online resources driving local action.")

    asset_fig = px.pie(asset_data, names='Asset Type', values='Count',
                       title='Community Asset Distribution', hole=0.4)
    st.plotly_chart(asset_fig, use_container_width=True)

    st.write("**Detailed Community Asset List**")
    st.dataframe(detailed_asset_table, use_container_width=True)

# Geography Tab
with tab4:
    st.subheader("Geographic Overview")
    st.write("Population distribution across key cities in Poweshiek County, led by Grinnell, followed by Brooklyn, Montezuma, and Victor.")

    city_fig = px.bar(city_data, x='City', y='Population', text='Population',
                      title='City Populations')
    st.plotly_chart(city_fig, use_container_width=True)

    st.markdown("""
    **Snapshot**
    - Founded: 1843, Named after Chief Poweshiek (Meskwaki)  
    - Total Area: 586 sq mi (1,520 km²)  
    - Population (2020): ~18,662  
    - Density: 32/sq mi
    """)

# Light CSS styling
st.markdown(
    """
    <style>
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
