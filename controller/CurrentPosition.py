import geocoder
import time

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.address
    else:
        return None

def get_current_location2():
    g = geocoder.ip('me')
    if g.ok:
        lat, lng = g.latlng
        g = geocoder.osm([lat, lng], method='reverse')
        if g.ok:
            return g.address
    return None

def get_current_location3():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng
    else:
        return None

# while True:
#     location = get_current_location3()
#     if location:
#         latitude, longitude = location
#         print(f"Latitud: {latitude}")
#         print(f"Longitud: {longitude}")
#     else:
#         print("No se pudo obtener la ubicación actual")
    
#     time.sleep(1)
