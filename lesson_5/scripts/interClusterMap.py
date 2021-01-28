# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:28:09 2021

@author: gcolm
"""

import folium
from pyproj import crs
import geopandas as gpd
import matplotlib.pyplot as plt
from folium.plugins import MarkerCluster


# import data
points_fp = 'data/addresses.shp'

# Read data
points= gpd.read_file(points_fp)

# # # # CLUSTERED POINT MAP # # # #
# Create a Map instance
m = folium.Map(location=[60.25, 24.8]
               , tiles = 'cartodbpositron'
               , zoom_start=11
               , control_scale=True
               )

# Get x and y from each point in the geodataframe
points['x'] = points['geometry'].apply(lambda geom : geom.x)
points['y'] = points['geometry'].apply(lambda geom : geom.y)

# Create list of coodinate pairs
locations = list(zip(points['y'], points['x']))

# Create a Map instance
m = folium.Map(location=[60.25, 24.8]
               , tiles='Stamentoner'
               , zoom_start= 11
               , control_scale=True
               )

# Create a folium Marker Cluster
marker_cluster = MarkerCluster(locations)

# Add marker cluster to the map
marker_cluster.add_to(m)