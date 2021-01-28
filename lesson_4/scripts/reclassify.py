

# import modules
import geopandas as gpd
import matplotlib.pyplot as plt
import mapclassify
import contextily as ctx # Adding basemaps from different providers
import os



def reclassify_Plot(data, col_target, classCol, k):
    """

    """
    # CLean column target from any Non Data value
    data = data.loc[data[col_target] >0]

    # Classify data column target and Plotting classified data column
    try:
        # define legend
        lgnd_kwds = {'title': title+ ' time',
                'loc': 'upper left', 'bbox_to_anchor': (1, 1.03), 'ncol': 1}
        # Create canvas
        fig, ax = plt.subplots(figsize=(10, 8))
        # plotting # 1...
        data.plot(ax=ax, column=col_target, scheme=classSch, k=k, legend=True, legend_kwds= lgnd_kwds, linewidth=0)
        plt.title('TravelTimes to RailwayStation in Helsinki')
        # add basemap
        ctx.add_basemap(ax, source=ctx.tile_providers._OSM_A )

        
        # Use tight layout
        plt.tight_layout()


    except:
        raise NotImplementedError()



# Variables
root  = "data"
fp = "TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"
data = gpd.read_file(os.path.join(root, fp))

# Input Data
col_target = str(input("Enter column name target: "))
classSch = str(input('Enter Scheme to be used: '))
k = int(input('Enter number of classification level: '))
title = str(input('Enter plot title: '))

# call function dataClassifier
reclass_plot = reclassify_Plot(data, col_target, classSch, k)
print(reclass_plot)























