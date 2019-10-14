import folium
map = folium.Map(location=[41.724433, -88.254221], zoom_start=20)
map.add_child(folium.Marker(location=[41.724433, -88.254221], popup="Home", icon=folium.Icon(color='green')))
map.save("webmap-myhome.html")
