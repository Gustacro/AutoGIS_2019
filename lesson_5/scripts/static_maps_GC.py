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
import os, sys

# Define root of the data
root = r"D:/Gustavo/resource_center/RLIS"

schools_fp = "PLACES/schools.shp"
libraries_fp = "PLACES/library.shp"
zipcodes_fp = r"C:\Users\gcolm\Documents\courses\online\online_courses\others\Geo_python_course\autoGIS_2019\lesson_5\data\pnw_schoolsPerZipcodes.shp"

# Read files
schools = gpd.read_file(os.path.join(root, schools_fp))
libraries = gpd.read_file(os.path.join(root, libraries_fp))
zipcodes = gpd.read_file(zipcodes_fp)

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
schools = schools.to_crs(crs=zipcodes.crs)
libraries = libraries.to_crs(crs=zipcodes.crs)

# Check if they have now the same crs
assert schools.crs == libraries.crs == zipcodes.crs, "Layer not in the same CRS"

# # # # PLOTTING 1.... # # # #

# Create one subplot. Control figure and size
fig, ax = plt.subplots(figsize=(12, 8))

# Visualize the travel into 9 classes using "Quantiles" classification scheme
zipcodes.plot(ax=ax, column='count'
          , linewidth=0.03
          , cmap="Spectral"
          , scheme="Quantiles"
          , k=6
          , alpha= 0.9
          )

# Add roads on top of the grid
# use ax to define where is the layer to be rendered it
schools.plot(ax=ax, color='grey', linewidth= 0.1)

# Add metro on top of previous map
libraries.plot(ax=ax, color='red', linewidth=0.1)

# remove empty white space around axes
plt.tight_layout()

# save figure as png
# outfp = "/docs/staticMap_NoLgnd.png"
# plt.savefig(outfp, dpi= 300)


# # # # -----------PLOTTING 2.... -----------# # # #

# # # #---ADDING LEGEND------# # # #

# Create one subplot. Control figure and size
fig, ax = plt.subplots(figsize=(12, 8))

# define legend
lgnd_kwds = {'title':'Schools Per Zipcode'
             , 'loc': 'upper left', 'bbox_to_anchor': (1, 1.01), 'ncol': 1}

# Visualize the travel into 9 classes using "Quantiles" classification scheme
zipcodes.plot(ax=ax
          , column='count'
          , cmap="Spectral"
          , linewidth=0.03
          , alpha= 0.9
          , scheme="Quantiles"
          , k=6
          , legend=True
          , legend_kwds=lgnd_kwds
          )

# Add roads on top of the grid
# use ax to define where is the layer to be rendered it
schools.plot(ax=ax, color='yellow', linewidth= 0.02)

# # Add metro on top of previous map
# libraries.plot(ax=ax, color='blue', linewidth=0.1)

# Add title to the plot
plt.title("School in the PNW per Zipcode")
# remove empty white space around axes
plt.tight_layout()

# save figure as png
outfp = "C:/Users/gcolm/Documents/courses/online/online_courses/others/Geo_python_course/autoGIS_2019/lesson_5/SchoolsPerZipcode.png"
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



































