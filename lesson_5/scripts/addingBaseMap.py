# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:52:13 2021

@author: gcolm
"""


# # # #  ADDING BASEMAP TO THE PLOT # # # #
# import modules
import geopandas as gpd
from pyproj import CRS
import matplotlib.pyplot as plt
import contextily as ctx # Adding basemaps from different providers

"""
Note: To add map tiles from providers such as "OpenStreetMap" & "Stamen Design" use contextily. Map tiles are 
        typically distributed in Web Mercator projection (EPSG:3857), - is often necessary re-project all spatial data
        into (Web Mercator) before visualizing data
"""

# data...
grid_fp = "data/TravelTimes_to_5975375_RailwayStation.shp"
# roads_fp = "data/roads.shp"
# metro_fp = "data/metro.shp"

# Read files
grid = gpd.read_file(grid_fp)
# roads = gpd.read_file(roads_fp)
# metro = gpd.read_file(metro_fp)

# Re-project layer to EPSG: 3857 projection Web Mercator
data = grid.to_crs(epsg=3857)

# # # # PLOT DATA WITH A BASEMAP # # # # 
# define canvas
fig, ax = plt.subplots(figsize=(12,9))
# remove NaN data represented with -1 value from column 'pt_r_tt'
data = data.loc[data['pt_r_tt'] > -1] # select all value > than -1
# plot column
data.plot(ax= ax, column='pt_r_tt', cmap='RdYlBu_r', linewidth=0, scheme='quantiles', k=9, alpha=0.6)

""" to check basemap available fron contextily do: dir(ctx.tile_providers) """
# ========= Add basemap to the canvas ========== # 
# ctx.add_basemap(ax) # default basemap is OpenStreetMap basemap
# Trying different basemap
ctx.add_basemap(ax, source=ctx.tile_providers._OSM_A )


# # # # ZOOM INTO THE DATA PLOTTED # # # # 
# A way of zoom into the data is by selecting a subset of the data as follow
# define canvas
fig, ax = plt.subplots(figsize=(12,9))
# Selecting values where pt_r_tt >=0 and pt_r_tt < 15 
subset = data.loc[(data['pt_r_tt'] >=0) & (data['pt_r_tt']< 15)] # select all value > than -1
# plot subset (because we are reducing amount of data by selecting a subset also we may have to reduce k (classes num.))
subset.plot(ax= ax, column='pt_r_tt', cmap='RdYlBu_r', linewidth=0, scheme='quantiles', k=5, alpha=0.6)

""" to check basemap available fron contextily do: dir(ctx.tile_providers) """
# Add basemap to the canvas
# basemap #1
# ctx.add_basemap(ax) # default basemap is OpenStreetMap basemap
# basemap #2
# ctx.add_basemap(ax, source=ctx.tile_providers._OSM_A )
# basemap #3 --> controling zoom; default auto; manualy 1-19 levels (higher number, more details); 
ctx.add_basemap(ax, source=ctx.tile_providers._OSM_A , zoom=15)


# # # # CROP THE MAP TO PLOT # # # # 
# %%time # Check how long it take to print output
# define canvas
fig, ax = plt.subplots(figsize=(12,9))
# plottng....
data.plot(ax= ax, column='pt_r_tt', cmap='RdYlBu_r', linewidth=0, scheme='quantiles', k=5, alpha=0.6)
# adding credits for basemap
credits = 'Travel time data by Digital Geography Lab, Map Data © OpenStreetMap contributors'
# adding basemap
ctx.add_basemap(ax, zoom=15, attribution=credits, source=ctx.tile_providers._OSM_A)
# Crop the canvas by setting set_xlim and set_ylim  (min & max of x, y )
ax.set_xlim(2760000, 2800000)
ax.set_ylim(8430000, 8470000)




























