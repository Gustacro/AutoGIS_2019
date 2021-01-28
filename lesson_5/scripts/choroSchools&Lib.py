# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:20:32 2021

@author: gcolm
"""
# import modules
import geopandas as gpd
from pyproj import CRS
import folium


# read data
df = r"D:\Gustavo\resource_center\RLIS\PLACES\school_site.shp"
# create geodataframe
data = gpd.read_file(df)

# Define CRS
# data.crs = CRS.from_epsg(3879)

# Re-project data to WGS84
data = data.to_crs(epsg=4326)

# Create a Geo-id which is needed by the folium (it needs to have a unique identifier for each row)
data['geoid'] = data.index.astype(str)


# rename geopandas columns to lower case
data.columns = data.columns.str.lower()

# select columns of interest
columns = ['geoid','site_name', 'county', 'geometry']

# define new data
data = data[columns]

data['centroid'] = data.loc[data['geometry']].centroid

