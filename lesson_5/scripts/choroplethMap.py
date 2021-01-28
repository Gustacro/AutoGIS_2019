# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:15:28 2021

@author: gcolm
"""

import geopandas as gpd
from pyproj import CRS
# import requests
# import geojson
import folium
# import certifi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Get features directly from the wfs
url = 'https://kartta.hsy.fi/geoserver/wfs?request=GetFeature&typename=asuminen_ja_maankaytto:Vaestotietoruudukko_2018&outputformat=JSON'
# Read data
data = gpd.read_file(url)

# Check the data
# data.head()

# Define CRS
data.crs = CRS.from_epsg(3879)

# Re-project data to WGS84
data = data.to_crs(epsg=4326)

# Check layer crs definition
# print(data.crs)

# Rename columns
data = data.rename(columns={'asukkaita': 'pop18'})

# Create a Geo-id which is needed by the folium (it needs to have a unique identifier for each row)
data['geoid'] = data.index.astype(str)

# Re-define geodataframe with columns needed
data = data[['geoid', 'pop18', 'geometry']]

# convert to GeoJson file
# pop_gjson = data.to_json()

# check data
# data.head()

# # # # CREATE INTERACTIVE CHOROPLETH MAP FROM # # # #

# Define map instance
m = folium.Map(location=[60.25, 24.8], tiles='cartodbpositron',
               zoom_start=11, control_scale=True)

# Plot choropleth map
folium.Choropleth(
    geo_data=data, name='Population in 2018'
    , data=data
    , columns=['geoid', 'pop18']
    , key_on='feature.id'
    , fill_color='YlOrRd'
    , fill_opacity=0.7
    , line_opacity=0.2
    , line_color='white'
    , line_weight=0
    , highlight=False
    , smooth_factor=1.0
    # , threshold_scale=[100, 250, 500, 1000, 2000]
    , legend_name='Population in Helsinki'
    ).add_to(m)
