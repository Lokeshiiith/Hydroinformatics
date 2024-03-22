import pandas as pd
import numpy as np
from scipy.stats import gamma, norm
import matplotlib.pyplot as plt
import geopandas as gpd
from pykrige.ok import OrdinaryKriging
from scipy.interpolate import griddata
from shapely.geometry import Polygon, Point

import streamlit as st
import folium

# Sidebar navigation
st.sidebar.title('Navigation')
nav_selection = st.sidebar.radio('Select Option', ['Region and Points', 'Map Based on Lat Long'])

# Load data or define variables
# You can replace this with your actual data or logic
data = pd.DataFrame({
    'Region': ['Region A', 'Region B', 'Region C'],
    'SIP Index': [10, 20, 30],
    'Latitude': [40.7128, 34.0522, 37.7749],
    'Longitude': [-74.0060, -118.2437, -122.4194]
})

if nav_selection == 'Region and Points':
    st.header('Region and Points')

   

elif nav_selection == 'Map Based on Lat Long':
    st.header('Map Based on Latitude and Longitude')

    
