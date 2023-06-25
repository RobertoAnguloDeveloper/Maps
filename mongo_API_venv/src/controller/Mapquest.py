import requests

class Mapquest:
    def __init__(self):
        self.url = 'https://www.mapquestapi.com/geocoding/v1/address'
        self.key = '32efpKKQxCSJchjYCMwAuREIB7ywAOAd'

    def get_geolocation(self, address):
        params = {
            'key': self.key,
            'location': address
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['info']['statuscode'] == 0:
                results = data['results'][0]['locations']
                if results:
                    location = results[0]
                    latitude = location['latLng']['lat']
                    longitude = location['latLng']['lng']
                    country = location['adminArea1']
                    street = location['street']
                    return {
                        'latitude': latitude,
                        'longitude': longitude,
                        'country': country,
                        'street': street
                    }
        return None

    def get_address(self, latitude, longitude):
        params = {
            'key': self.key,
            'location': f"{latitude},{longitude}"
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['info']['statuscode'] == 0:
                results = data['results'][0]['locations']
                if results:
                    location = results[0]
                    latitude = location['latLng']['lat']
                    longitude = location['latLng']['lng']
                    country = location['adminArea1']
                    street = location['street']
                    return {
                        'latitude': latitude,
                        'longitude': longitude,
                        'country': country,
                        'street': street
                    }
        return None
