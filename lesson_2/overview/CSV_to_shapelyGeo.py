#!/usr/bin/env

"""
Main Popuse :
-------------
plot a map based on a set of longitude and latitude coordinates
that are stored in a csv file.

Requirements :
--------------
CSV file with coordinates ; .csv
"""

# -----------------------------------------------------------------------
# import modules
import os
import sys
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pyproj import CRS
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------

def testing(root, fp):
    """
    docs :
    """
    try:
        # Create dataframe
        data = pd.read_csv(os.path.join(root, fp))
        # Create Point object from lat & lon columns, then pass them as new column call 'geometry'
        data['geometry'] = [(Point(x, y))
                            for x, y in zip(data['lon'], data['lat'])]
        print(data.head())
        # ========= Save dataframe as Shapefile =======================

        # Return dataframe
        return data
    except:
        raise NotImplementedError()


# Script path
# autoGIS_2019/lesson_2/overview/fromCSV_shapelyGeo.py
# csv path
# autoGIS_2019/lesson_2/Exercise-2/data/some_posts.csv

data = testing(root= r"Exercise-2/data/", fp="some_posts.csv")
