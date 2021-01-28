
import folium
from pyproj import crs
import geopandas as gpd
import matplotlib.pyplot as plt
import webbrowser # package imported to visualize interactive map in spyder

# Create a Map instance with default basemap
m1= folium.Map(location=[45.5051, -122.6750]
              , zoom_start= 12
              , control_scale=True
               )

# Adding tiles- parameter for changing background map
m2= folium.Map(location=[60.25, 24.8]
              , tiles='Stamen Toner'# adding tiles; 
              , zoom_start= 12
              , control_scale=True
               )

# Adding layer to map
m3= m1 # let's use m1 as basemap

# Add Marker
# Run: help(folium.Icon) for info about icons
folium.Marker(
    location=[45.512880, -122.685390]
    ,popup='Casita'
    ,icon=folium.Icon(color='green', icon='ok-sign')
    ).add_to(m3)













# # # # SAVING MAP AS HTML # # # #
"""save map as html file here un-commenting the follow 2 lines or 
# run the follow 2 line in terminal"""
# output = 'maps\interMap_1.html'
# m.save(output)

# # render map on web browser
# webbrowser.open("interMap_1")