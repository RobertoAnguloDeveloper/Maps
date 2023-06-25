from datetime import datetime
from controller.DbConnection import MongoDB
from model.Vehicle import Vehicle

class VehicleController:
    def __init__(self, app):
        self.db = MongoDB(app).get_db()
        
    def create_vehicle(self, vehicle):
        vehicle_data = {
            'license_number': vehicle.license_number,
            'password': vehicle.password,
            'current_position': vehicle.current_position,
            'current_route_id': vehicle.current_route_id,
            'last_update': datetime.now()
        }
        # Lógica para guardar el vehículo en la base de datos utilizando el método insert_one de PyMongo
        result = self.db.vehicles.insert_one(vehicle_data)
        return result

    def get_vehicle(self, license_number):
        # Lógica para obtener un vehículo de la base de datos según el número de licencia
        vehicle = self.db.vehicles.find_one({'license_number': license_number})
        vehicle["_id"] = str(vehicle["_id"])
        return vehicle
    
    def get_all_vehicles(self):
        vehicles = self.db.vehicles.find()
        vehicle_list = list(vehicles)
        for i in range(len(vehicle_list)):
            vehicle_list[i]["_id"] = str(vehicle_list[i]["_id"])
        return vehicle_list
    
    def update_vehicle(self, vehicle):
        vehicle_to_update = self.get_vehicle(vehicle.license_number)
        if vehicle_to_update:
            vehicle_to_update['password'] = vehicle.password
            vehicle_to_update["current_route_id"] = vehicle.current_route_id
            self.db.vehicles.update_one({'license_number': vehicle.license_number}, {'$set':{'password': vehicle_to_update['password'], 'current_route_id': vehicle_to_update['current_route_id']}})
            return True
        return False

    def delete_vehicle(self, license_number):
        vehicle = self.get_vehicle(license_number)
        if vehicle:
            self.db.vehicles.delete_one({'license_number': license_number})
            return True
        return False