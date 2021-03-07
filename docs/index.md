## Web Interactive Maps with Geopandas

Here you will find some of the maps that I have created using [Geopandas](https://geopandas.org/) and the free course [Automating GIS-Processes](https://autogis-site.readthedocs.io/en/latest/index.html), 
offered by the [Masters program in Geography](https://www.helsinki.fi/en/admissions/degree-programmes/geography-masters-programme) at Helsinki University.

### Data used:
- Schools - RLIS 2013
- Zipcodes - RLIS 2013
- Population - RLIS 2013
- Historic Landmarks (Colorado)- 2017, USA
- Population per neighborhoods in Colorado -2010, USA
- Finland Employment Rate 2013
- Finland Districts

### Libraries used:
- [Pandas](https://pandas.pydata.org/pandas-docs/version/0.15/tutorials.html)
- [NumPy](https://numpy.org/doc/stable/user/quickstart.html)
- [Geopandas](https://geopandas.org/)
- [PyProj](https://pyproj4.github.io/pyproj/stable/)
- [Folium](https://python-visualization.github.io/folium/)
- [Branca](https://python-visualization.github.io/branca/index.html)
- [Matplotlib](https://matplotlib.org/3.3.3/tutorials/index.html)


### Static map
**Name** : 
Schools per Zipcodes in the Pacific Northwest<br>
**Description** :
To show the distribution of public and private schools in the Pacific Northwest.

**Process**:
- Read shapefiles, then create GeoDataFrames.
- Check their Coordinate Referece System (CRS) ; to verify that they are in the same projection, If necessary re-project using the following syntax: 
	```python
	gdf1 = gdf1.to_crs(crs=gdf2.crs) # only when reprojecting using __crs__ from another gdf.
	gdf2 = gdf2.to_crs(<EPSG code>)
	```
- Verify that	geodataframes are in the same projection ; 
	```python
	assert gdf1.crs == gdf2.crs == gdf3.crs, "Layer not in the same CRS"
	```
- Create a canvas.
- Add geodataframes as layers in order bottom to top.
- Plot and save as PNG.

Click the link to see the static map : [Schools per Zipcodes in PNW](https://gustacro.github.io/AutoGIS_2019/SchoolsPerZipcode.png)

### Join Attributes and Geometries in Choropleth map
**Name** : 
Employment Rate in Finland-2013.

**Description:** 
To show the employment rate in Finland in the year 2013.

**Process**:
- Read dataset (csv) file and create dataframe.
- Get dataset directly from the vfs website: define url starting with "http://....", then `gdf_name= gpd.read_file(url)`.
- Check that both of the gdf have the same shape (rows number).
- Merge gdf using the commun column that is in both gdf:
	```python
	gdf1= gdf1.merge(dataframe, on='commun_col')
	```
- Check again the number of rows on the merged gdf. It should contain the same number of rows from origin.
- Create a plot to verify the merge:
	```python
	gdf1.plot(column='commun_col')
	plt.show()
	```
- To create an interactive map, all layers should be in __Web Mercator projection (4326)__ ; Re-project if needed 
- Create and "geoid" column in the gdf1 as:
	```python
	gdf1['geoid'] = gdf1.index.astype(str)
	```
- Create a map instance
- Define Choropleth layer using **folium.Choropleth(*args)** and add it the map instance by `.add_to(m)`
- Define style function to use in tooltip feature: 
	```python
	style_function= lambda x: {'color':'transparent', 'fillColor':'transparent', 'weight': 0}
	```
- add folium feature GeoJson like:
	```python
	folium.features.GeoJson(geodata
      			,name='Labels' # name of the layer in the Layer control
     			,style_function= style_function 
      			# Display text (define what value to show)
      			,tooltip=folium.features.GeoJsonTooltip(fields=['tyollisyys'] # colunm display in popup
									,aliases=['Employment rate'] 
									,sticky=False # 
                                    				)
	).add_to(m)
	```
- Add folium Layer Control to the map instance as: `folium.LayerControl().add_to(m)`
- save the map instance with:
	```python
	output = "path_to_directory/map_name.html"`
	m.save(output)
	```
Click the link to see the interactives map : [Employment Rate in Finland 2013](https://gustacro.github.io/AutoGIS_2019/joinAttr&GeomChoroplethMap.html)


### Population and Historic Landmarks in Colorado, USA map
**Name** : 
Population per Zipcode and Historic landmarks in Colorado (), USA.

**Description:** 
To show population per neighborhood and landmarks in Colorado, USA.

**Process**:
- Read dataset (.csv, .shp) file and create geodataframes.
- To create an interactive map, all layers should be in __Web Mercator projection (4326)__ ; Re-project if needed 
- Check their Coordinate Referece System (CRS) ; to verify that they are in the same projection, If necessary  re-project using the following syntax: 
	```python
	gdf1 = gdf1.to_crs(crs=gdf2.crs) # only when reprojecting using __crs__ from another gdf.
	gdf2 = gdf2.to_crs(<EPSG code>)
	```
- Verify that geodataframes are in the same projection ; 
	```python
	assert gdf1.crs == gdf2.crs == gdf3.crs, "Layer not in the same CRS"`
	```
- Get the x and y coordinates from the landmarks geodataframe
	```python
	ldmk_gdf['lon'] = ldmk_pl.geometry.x
	ldmk_gdf['lat'] = ldmk_pl.geometry.y 
	```
- Check that all geodataframe contain geometries columns:
	```python
	print(['geom column exists' for geom in gdf1.columns if geom =='geometry'])`. Do same with all geodataframes
	```
- If necessary re-define the columns to use per geodataframe.
- Use the values of `min`, `max`, and mean from the population dataset to define the quantile values and use it in our color scale.
	```python
	min, max = population_gdf['<pop_col>'].quantile([0.05, 0.95]).apply(lambda x: round(x, 2))	
	mean = round(population_gdf['pop_col'].mean(), 2) 
	```
- Create the color scale using the min, max and mean values
	```python
	colormap = branca.colormap.LinearColormap(
	colors= ['#ffffcc','#a1dab4','#41b6c4','#2c7fb8','#253494'],
		index= cens_pop['population'].quantile([0.2,0.4,0.6,0.8]),
		vmin= min,
		vmax= max
	)

	colormap.caption="Population in Denver, Colorado per neighborhood"

	colormap
	```
- Create dataframe series from `['lat', 'lon', 'name', 'address']` columns from the population gdf
	```python
	lat = ldmk_gdf['lat'] # do the same for mentioned columns above
	```
- Create pair lists from the dataframe series previous created
	```python
	locations = list(zip(lat, lon))
	naming = list(zip(name, address))
	```
- Create formating for popups to define what to show in each point
	```python
	popups = ['Name: {}<br>Address:{}'.format(name, address) for (name, address) in naming]
	```
- Create and "geoid" column in the gdf1:
	```python
	gdf1['geoid'] = gdf1.index.astype(str)
	```
- Create a map instance
- Define style function to use in tooltip feature:
- Add population layer to map instance
- Create Marker_cluster layer for ldmk places using `MarkCluster()` from `folium.plugins` and the __locations__ to `folium.plugins.FastMarkerCluster(locations)`
- Add mark_cluster to the map
- Add search bar to the map instance with the `search()` from `folium.plugins`
- Add folium Layer Control to the map instance as: `folium.LayerControl().add_to(m)`
- save the map instance with:
	- `output = "path_to_directory/map_name.html"`
	- `m.save(output)`

Click the link to see the interactives map : [Population and landmarks in Colorado, USA](https://gustacro.github.io/AutoGIS_2019/cluster_landmarks_Denver.html)

		
### Support or Contact

Having trouble with Pages? Check out our [documentation](https://github.com/Gustacro/AutoGIS_2019/tree/master/lesson_5) or contact support (<a href="mailto:someone@yoursite.com?subject=Mail from Our Site">Email Us</a>) and we’ll help you sort it out.
