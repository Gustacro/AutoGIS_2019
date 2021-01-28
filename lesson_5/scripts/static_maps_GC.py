# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 09:57:51 2021

@author: gcolm
"""

# # # # STATIC MAPS IN GEOPANDAS # # # #

# Basic Plotting 
"""
Create a 3 layers static map: 
    - Roads, metro lines (layers on top of each other)
"""
# import modules
import geopandas as gpd
from pyproj import CRS
import matplotlib.pyplot as plt

grid_fp = "data/TravelTimes_to_5975375_RailwayStation.shp"
roads_fp = "data/roads.shp"
metro_fp = "data/metro.shp"

# Read files
grid = gpd.read_file(grid_fp)
roads = gpd.read_file(roads_fp)
metro = gpd.read_file(metro_fp)

# Check coordinate system (CRS)
# print(grid.crs)
# print(roads.crs)
# print(metro.crs)

# Check CRS names of the layer
# print(f'Grid crs: {grid.crs.name}')
# print(f'Roads crs: {roads.crs.name}')
# print(f'Metro crs: {metro.crs.name}')

""" As we can see from previous print we got:
        Grid crs: ETRS89 / TM35FIN(E,N)
        Roads crs: KKJ / Finland zone 2
        Metro crs: KKJ / Finland zone 2        
"""

# Let's re-project geometrics to ETRS89 / TM35FIN based on the grid layer
# Reprojecting Geometries
roads = roads.to_crs(crs=grid.crs)
metro = metro.to_crs(crs=grid.crs)

# Check if they have now the same crs 
assert roads.crs == metro.crs == grid.crs, "Layer not in the same CRS"

# # # # PLOTTING.... # # # #

# Create one subplot. Control figure and size
fig, ax = plt.subplots(figsize=(12, 8))
                  
# Visualize the travel into 9 classes using "Quantiles" classification scheme
grid.plot(ax=ax, column='car_m_t'
          , linewidth=0.03
          , cmap="Spectral"
          , scheme="Quantiles"
          , k=9
          , alpha= 0.9
          ) 

# Add roads on top of the grid
# use ax to define where is the layer to be rendered it
roads.plot(ax=ax, color='grey', linewidth= 1.5)

# Add metro on top of previous map
metro.plot(ax=ax, color='red', linewidth=2.5)

# remove empty white space around axes
plt.tight_layout()

# save figure as png
outfp = "staticMap_NoLgnd.png"
plt.savefig(outfp, dpi= 300)

# # # # ADDING LEGEND TO THE PLOT # # # #

# Create one subplot. Control figure and size
fig, ax = plt.subplots(figsize=(12, 8))

# define legend
lgnd_kwds = {'title':'Car Travel Time (min)'
             , 'loc': 'upper left', 'bbox_to_anchor': (1, 1.01), 'ncol': 1}

# Visualize the travel into 9 classes using "Quantiles" classification scheme
grid.plot(ax=ax
          , column='car_m_t'
          , cmap="Spectral"
          , linewidth=0.03
          , alpha= 0.9
          , scheme="Quantiles"
          , k=9
          , legend=True
          ,legend_kwds=lgnd_kwds
          ) 

# Add roads on top of the grid
# use ax to define where is the layer to be rendered it
roads.plot(ax=ax, color='grey', linewidth= 1.5)

# Add metro on top of previous map
metro.plot(ax=ax, color='red', linewidth=2.5)

# Add title to the plot
plt.title("Car: Travel time from Rail Station in Helsinki")
# remove empty white space around axes
plt.tight_layout()

# save figure as png
outfp = "staticMap_WLgnd.png"
plt.savefig(outfp, dpi= 300)

"""
Note: if not defined lgnd_kwds variable with dict arguments for legend_kwds= lgnd_kwds parameter in grid.plot, 
you can define legend parameter by invoquing the following
"""
# Re-position the legend and set a title
# ax.get_legend().set_bbox_to_anchor((1.21,1))
# ax.get_legend().set_title("Travel time (min)")

# # # #  ADDING BASEMAP TO THE PLOT # # # #
# import contextily
import contextily as ctx # Adding basemaps from different providers
"""
Note: To add map tiles from providers such as "OpenStreetMap" & "Stamen Design" use contextily. Map tiles are 
        typically distributed in Web Mercator projection (EPSG:3857), - is often necessary re-project all spatial data
        into (Web Mercator) before visualizing data
"""









  

























