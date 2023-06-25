import geocoder
import time

class CurrentPosition:
    
    def get_current_location(self):
        g = geocoder.ip('me')
        if g.ok:
            return g.address
        else:
            return None

    def get_current_location2(self):
        g = geocoder.ip('me')
        if g.ok:
            lat, lng = g.latlng
            g = geocoder.osm([lat, lng], method='reverse')
            if g.ok:
                return g.address
        return None

    def get_current_location3(self):
        g = geocoder.ip('me')
        if g.ok:
            return g.latlng
        else:
            return None

# location = CurrentPosition().get_current_location3()

# print(location)
# location = CurrentPosition().get_current_location2()
# # if location:
# #     print(f"Latitud: {location}")
# # else:
# #     print("No se pudo obtener la ubicación actual")
# while True:
#     location = CurrentPosition().get_current_location3()
#     if location:
#         latitude, longitude = location
#         print(f"Latitud: {latitude}")
#         print(f"Longitud: {longitude}")
#     else:
#         print("No se pudo obtener la ubicación actual")
    
#     time.sleep(1)
