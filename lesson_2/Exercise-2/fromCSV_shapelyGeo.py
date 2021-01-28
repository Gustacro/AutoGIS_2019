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

def testing(root, fp, idx_col):
    """
    docs :
    """
    try:
        # Create dataframe
        data = pd.read_csv(os.path.join(root, fp), index_col=idx_col)
        # Create Point object from lat & lon columns, then pass them as new column call 'geometry'
        data['geometry'] = [(Point(x, y))
                            for x, y in zip(data['lon'], data['lat'])]
        print(data.head())

        # Return dataframe
        return data

    except Exception as e:
        print(e)

# =========================== Save dataframe as Shapefile =======================


def dFToGDF(data, crs_code, output_path, filename):
    try:
        # Create a GeoDataFrame from dataframe, also define geometry column
        geo = gpd.GeoDataFrame(data, geometry='geometry',
                               crs=CRS.from_epsg(crs_code).to_wkt())
        # Save GeoDataFrame as shapefile
        output = output_path
        output_name = filename
        output_file = os.path.join(output, output_name)
        # print output location path
        print(f'Output location: {output_file}')
        # print output file CRS
        print(f"GeoDataFrame CRS: {geo.crs}")
        # safe file as shapefile
        geo.to_file(output_file)

        # Return GeoDataFrame
        return geo
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


# calling functions
data = testing(root=r"data/", fp="some_posts.csv", idx_col='userid')

# calling function 2
geo = dFToGDF(data=data, crs_code=4326,
              output_path=r"C:\Users\gcolm\Documents\courses\online\GIS_python_functions", filename="testing_shapefile.shp")

print('Shapefile was created')
