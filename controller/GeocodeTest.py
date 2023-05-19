import requests
from CurrentPosition import CurrentPosition

def geocode_address(address):
    url = 'https://www.mapquestapi.com/geocoding/v1/address'
    params = {
        'key': '32efpKKQxCSJchjYCMwAuREIB7ywAOAd',
        'location': address
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Procesar la respuesta y extraer las coordenadas, etc.
        return data
    else:
        return None

# Ejemplo de uso
currentPosition = CurrentPosition().get_current_location2()
address = currentPosition #'1600 Pennsylvania Ave NW, Washington, DC, 20500'
result = geocode_address(address)
if result:
    latitude = result['results'][0]['locations'][0]['latLng']['lat']
    longitude = result['results'][0]['locations'][0]['latLng']['lng']
    print(f"Latitud: {latitude}")
    print(f"Longitud: {longitude}")
else:
    print("No se pudo geocodificar la dirección")
