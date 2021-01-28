#!/usr/bin/env

"""
# Vector Data I/O in Python

Reading data into Python is usually the first step of an analysis workflow.
There are various different GIS data formats available such as:
- Shapefile
- GeoJSON
- KML
- GPKG
- Geopandas
...is capable of reading data from all of these formats (plus many more).


File Format
In geopandas, we use a generic function from_file() for reading in different data formats.
In the bacground, Geopandas uses fiona.open() when reading in data.
Esri Shapefile is the default file format.
For other file formats we need to specify which driver to use for reading in the data.

"""

# -----------------------------------------------------------------------
## ----------- Check supported through geopandas, or directly from fiona: --------- ##
import geopandas as gpd
import os
# Check supported format drivers
# print(gpd.io.file.fiona.drvsupport.supported_drivers)

# You can do the same with fiona
import fiona
fiona.supported_drivers
# -----------------------------------------------------------------------


def read_gis_file(root, fp):
    """
    Porpuse:
    --------
    Read GIS file formats: shp, gjson, kml, gpkg

    Parameters:
    ----------
    root : folder location; str
    fp : file name + .extension; str

    Returns:
    --------
    A GeDataFrame
    """
    try:
        # Read shapefile
        filename, file_extension = os.path.splitext(os.path.join(root, fp))
        if file_extension == ".shp":
            data = gpd.read_file(os.path.join(root, fp))
        # Read GeoJSON
        elif file_extension == ".gjson":
            data = gpd.read_file(os.path.join(root, fp), driver="GeoJSON")
        # Read KML
        elif file_extension == ".kml":
            gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
            data = gpd.read_file(os.path.join(root, fp))
        # Read GeoPackage
        elif file_extension == ".gpkg":
            data = gpd.read_file(os.path.join(root, fp))
            # print(data)
        return data
    except Exception as e:
        print(e)


# Execute function
data = read_file(root="data", fp="finland_municipalities.shp")
print(data)


# ----------------------------------------------------------------
def write_gis_file(data, root, layer_name, output_drvr):
    """
    Porpuse:
    --------
    Write GIS file formats: shp, gjson, kml, gpkg

    Parameters:
    ----------
    data : A GeoDataFrame
    root : folder location; str
    layer_name : name of output file ;str
    output_drvr : GIS format of output

    Returns:
    --------
    A new file with the GIS format that the user need it
    """
# -----------------------------------------------------------------
    try:
        # Enable writing kml
        gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
        # Drivers
        drivers = {'Esri Shapefile': 'shp',
                   'GeoJSON': 'gjson', 'KML': 'kml', 'GPKG': 'gpkg'}
        # Write a layer to a defined file format
        for driver, extension in drivers.items():
            if output_drvr == driver:
                file_name = root + \
                    '/{0}_copy.{1}'.format(layer_name, extension)

                # Write data using the correct driver
                data.to_file(file_name, driver=driver)
                return(f'Created file: {file_name}')
    except:
        raise NotImplementedError()


# input layer_name
layer_name = input("Enter layer name: ")
# Execute function
print(write_file(data, root='data', layer_name=layer_name, output_drvr='KML'))
