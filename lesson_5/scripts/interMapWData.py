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

# convert points GeoDataFrame to GeoJSON file
point_gjson = folium.features.GeoJson(points, name='Public transport stations')

# Check the GeoJson features
# point_gjson.data.get('features')

# # # # ADDING POINT TO HELSINKI BASEMAP # # # #
m = folium.Map(location=[60.25, 24.8]
               , tiles='cartodbpositron'
               , zoom_start=11, control_scale=True
               )

# Adding points to the map instance
point_gjson.add_to(m)

# Adding Layer Control
folium.LayerControl().add_to(m)

