import folium
from CurrentPosition import CurrentPosition

currentPosition = CurrentPosition().get_current_location3()
# print(currentPosition)
m = folium.Map(location=currentPosition, zoom_start=14)
m.save("index.html")