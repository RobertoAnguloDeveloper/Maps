import folium
m = folium.Map(location=[5.8281255,-55.1589546], zoom_start=12)
folium.Marker(location=[5.8281255,-55.1589546], tooltip="Test", popup="CTG", icon=folium.Icon(icon="cloud", color="blue"),zoom_start=12).add_to(m)
m