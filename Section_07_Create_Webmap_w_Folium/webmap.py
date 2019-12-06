<<<<<<< HEAD
##############################################################################
# WHAT:
# A Webmap of the United States built with Python and Folium
# from Section 8 of https://www.udemy.com/the-python-mega-course
#
# DESCRIPTION:
# Use Python and folium to create a webmap with two layer and a layer control selector:
# - there is a layer with color coded points for volcanos with popups displaying the height in meters
# - there is a layer with a bold outline for each country and filled with colors representing population
#-----------------------------------------------------------------------------
# DATE         WHO                   DESCRIPTION
# ----------   --------------------  -----------------------------------------
# 2019-03-22   Maurice Johnson       Created
##############################################################################

import folium
import pandas


####################################################
# 1. CREATE BASE MAP OBJECT
###################################################
# Create Map object, set the zoom and select a background
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")


####################################################
# 2. CREATE LAYER WITH COLOR CODED POINTS FOR VOLCANOS
###################################################
# read volcano map points from a File
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# function to choose colors for volcano markers based on elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")

# Create feature group for volcano point
# The points for the volcanos are color coded based on elevevation
 # zip allows us to loop thru the lat, lon and elev list together
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))



########################################################################
# 3. CREATE LAYER WIT COLOR CODING WITHIN COUNTRY BOUNDARIES FOR POPULATION
#########################################################################
fgp = folium.FeatureGroup(name="Population")

# Creage a "Chrolopleth Map" i.e., Pull polygons for ourline of countries and fill with
# color coding based on population of the country
# style_function is a lambda function: a function that can be written in line and
# optionally executed anonymously (in place)
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


################################################################################
# 4. ADD LAYERS AND LAYER CONTROL OBJECT TO THE MAP and SAVE MAP TO HTML FILE
###############################################################################
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# Save the map to an html file
map.save("Map1.html")
=======
##############################################################################
# WHAT:
# A Webmap of the United States built with Python and Folium
# from Section 8 of https://www.udemy.com/the-python-mega-course
#
# DESCRIPTION:
# Use Python and folium to create a webmap with two layer and a layer control selector:
# - there is a layer with color coded points for volcanos with popups displaying the height in meters
# - there is a layer with a bold outline for each country and filled with colors representing population
#-----------------------------------------------------------------------------
# DATE         WHO                   DESCRIPTION
# ----------   --------------------  -----------------------------------------
# 2019-03-22   Maurice Johnson       Created
##############################################################################

import folium
import pandas


####################################################
# 1. CREATE BASE MAP OBJECT
###################################################
# Create Map object, set the zoom and select a background
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")


####################################################
# 2. CREATE LAYER WITH COLOR CODED POINTS FOR VOLCANOS
###################################################
# read volcano map points from a File
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# function to choose colors for volcano markers based on elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")

# Create feature group for volcano point
# The points for the volcanos are color coded based on elevevation
 # zip allows us to loop thru the lat, lon and elev list together
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))



########################################################################
# 3. CREATE LAYER WIT COLOR CODING WITHIN COUNTRY BOUNDARIES FOR POPULATION
#########################################################################
fgp = folium.FeatureGroup(name="Population")

# Creage a "Chrolopleth Map" i.e., Pull polygons for ourline of countries and fill with
# color coding based on population of the country
# style_function is a lambda function: a function that can be written in line and
# optionally executed anonymously (in place)
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


################################################################################
# 4. ADD LAYERS AND LAYER CONTROL OBJECT TO THE MAP and SAVE MAP TO HTML FILE
###############################################################################
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# Save the map to an html file
map.save("Map1.html")
>>>>>>> d9f007d2e37e095ebc203c10e5533b3e37a3f618
