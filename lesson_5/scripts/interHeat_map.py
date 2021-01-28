# -*- coding: utf-8 -*-

import folium
from pyproj import crs
import geopandas as gpd
import matplotlib.pyplot as plt
import webbrowser # package imported to visualize interactive map in spyder


# import data
points_fp = 'data/addresses.shp'

# Read data
points= gpd.read_file(points_fp)

# Get x and y coodinates for each point
points['x'] = points['geometry'].apply(lambda geom: geom.x)
points['y'] = points['geometry'].apply(lambda geom: geom.y)

# Create a list of coordinate pairs
locations = list(zip(points['y'],points['x']))

# # # # IMPORTING FOLIUM PLUGGING # # # # 
from folium.plugins import HeatMap

# Create a Map instance
m = folium.Map(location=[60.25, 24.8]
               , tiles='Stamentoner'
               , zoom_start= 11
               , control_scale=True
               )

# Add heatmap pluging to the map
HeatMap(locations).add_to(m)
