# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:26:18 2021

@author: gcolm
"""

# import modules
import libpysal
import geopandas as gpd
import mapclassify as mc
import matplotlib.pyplot as plt
import os
# Check mapclassify version
print(mc.__version__)

# # # # Variables # # # # 
root  = "data"
fp = "TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"
data = gpd.read_file(os.path.join(root, fp))


# # # # QUANTILES  # # # #
# Define Quantiles classifier, 6 classes for column 'walk_d'
quant6 = mc.Quantiles(data['walk_d'], k=6)

# If user want the legend contain the classifier, invoque 'get_legend_classes' method
quant6.get_legend_classes() # It will create a list containing string of classifier classes

# To change the decimals in the classes invoque 'set_fmt' method
quant6.set_fmt(fmt='{:.0f}') # It will print the classes with zero decimals

# # # # CLOROPLETH # # # #
# Create cloropleth map.
# Expesify column; define classify scheme: Quantiles; and k= 10
data.plot(column='walk_d', scheme= 'Quantiles', cmap='RdYlBu_r', k=10, figsize=(12,8))


# # # # NATURAL BREAKS  # # # #
# Define Natural Breaks classifier with 9 classes
nBreak10 = mc.NaturalBreaks.make(k=9)

# Create new column containing data classifier classes values
data['nb_pt_r_tt'] = data[['pt_r_tt']].apply(nBreak10)


# # # # LEGEND # # # #
# Toggle a legend in a cloropleth
data.plot(column='nb_pt_r_tt', linewidth= 0, legend=True)
plt.tight_layout()


 # # # # HISTOGRAM  # # # #
# Define classifier
classifier= mc.NaturalBreaks(y=data['pt_r_tt'], k=5)
 # Plot histogram
data['pt_r_tt'].plot.hist(bins=50)
# plot the classes in the histogram
for value in classifier.bins:
    plt.axvline(value, color='k', linestyle='dashed', linewidth=1)
 











