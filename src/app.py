import folium
from CurrentPosition import CurrentPosition

currentPosition = CurrentPosition().get_current_location3()
# print(currentPosition)
m = folium.Map(location=currentPosition, zoom_start=14)
customIcon = folium.CustomIcon("./src/img/car2.png", icon_size=(50, 50))
folium.Marker(location=currentPosition, icon=customIcon, draggable=True).add_to(m)
# folium.Marker(location=currentPosition, draggable=True).add_to(m)
m.save("index.html")