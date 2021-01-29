## Welcome to my first attempt of GitHub Page

Here you will find some of the maps that I have created using [Geopandas](https://geopandas.org/) and the free course [Automating GIS-Processes](https://autogis-site.readthedocs.io/en/latest/index.html), 
offered by the [Masters program in Geography](https://www.helsinki.fi/en/admissions/degree-programmes/geography-masters-programme) at Helsinki University.

### Data used:
- Schools - RLIS 2013
- Zipcodes - RLIS 2013
- Population - RLIS 2013
- Historic Landmarks (Colorado), USA
- Neighborhoods in Colorado, USA
- Finland Employment Rate 2013
- Finland Districts

### Libraries used:
- Pandas
- NumPy
- Geopandas
- PyProj
- Folium
- Branca
- Matplotlib


### Static map
Name: Schools per Zipcodes in the Pacific Northwest
Description: 
To show the distribution of public and private schools in the Pacific Northwest.
Process:
- Read the shapefiles, and create GeoDataFrames.
- Check their Coordinate Referece System (CRS); to verify that they are in the same projection, If necessary re-project using the following syntax: 
	- `gdf_name = gdf_name.to_crs(crs=gdf_name2.crs) ` __only when reprojecting using crs from another gdf__
	- `gdf_name = gdf_name.to_crs(<EPSG code>)`
	- verify that the geodataframes are the same projection; `assert gdf_name1.crs == gdf_name2.crs == gdf_name3.crs, "Layer not in the same CRS"`
- Create a canvas
- Add geodataframes as layers in order bottom to top
- Plot and save as PNG


### Join Attributes and Geometries in Choropleth map
Name: Employment Rate in Finland-2013
**Description:**
To show the employment rate in Finland in the year 2013.
Process:
- Read dataset (csv file) and create dataframe
- Get dataset directly from the vfs website: define url starting with "http://....", then `gdf_name= gpd.read_file(url)`.
- Check that both of the gdf have the same shape (rows number).
- Merge gdf using the commun column that is in both gdf `gdf1= gdf1.merge(dataframe, on='commun_col')`
- Check again the number of rows on the merged gdf. It should contain the same number of rows from origin.
- Create a plot to verify the merge 
	- `gdf1.plot(column='commun_col')`
	= `plt.show()`
- To create an interactive map, all layers should be in __Web Mercator projection__ ; Re-project if needed 
- Create and "geoid" column in the gdf1 gdf1['geoid'] = gdf1.index.astype(str)`
- Create a map instance
- Define Choropleth layer using **folium.Choropleth(*args)** and add it the map instance by `.add_to(m)`
- Define style function to use in tooltip feature: 
	- sample: `style_function= lambda x: {'color':'transparent', 'fillColor':'transparent', 'weight': 0}`
- add folium feature GeoJson like:
	- `folium.features.GeoJson(geodata
                        ,name='Labels' # name of the layer in the Layer control
                       ,style_function= style_function 
                        # Display text (define what value to show)
                       ,tooltip=folium.features.GeoJsonTooltip(fields=['tyollisyys'] # colunm field to display in the popup
                                                              ,aliases=['Employment rate'] 
                                                              ,sticky=False # 
                                                              )  
                       ).add_to(m)`

- Add folium Layer Control to the map instance as: `folium.LayerControl().add_to(m)`
- save the map instance with:
	- `output = 'path_to_directory/map_name.html'
	- `m.save(output)`

Click the link to see the interactives map[Employment Rate in Finland 2013]()

## ADD SOME PROBLEMS WITH THE DATA
## ...................

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Gustacro/AutoGIS_2019/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
