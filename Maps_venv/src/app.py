from flask import Flask, render_template, request, jsonify

from controller.CurrentPosition import CurrentPosition
from controller.VehicleController import VehicleController
from model.Vehicle import Vehicle

app = Flask(__name__)
vehicle_controller = VehicleController(app)

@app.route('/')
def index():
    return get_all_vehicles()

@app.route('/vehicle/create', methods=['POST'])
def create_vehicle():
    response = request.get_json()
    vehicle = Vehicle(response["license_number"], response["password"], CurrentPosition().get_current_location3())
    result = vehicle_controller.create_vehicle(vehicle)
    if result:
            return jsonify({'mensaje': 'Vehicle created successfully'})
    else:
        return jsonify({'message': 'Failed to create vehicle'}), 500
    
@app.route('/vehicle/update', methods=['PUT'])
def update_vehicle():
    response = request.get_json()
    search = get_vehicle(response["license_number"])
    if search:
        vehicle = Vehicle(response["license_number"], response["password"],CurrentPosition().get_current_location3())
        result = vehicle_controller.update_vehicle(vehicle)
        if result:
                return jsonify({'message': 'Vehicle updated successfully'})
        else:
            return jsonify({'message': 'Failed to update vehicle'}), 500
    else:
        return jsonify({'message': 'License number not found'}), 500
    

@app.route('/vehicle/get/<license_number>', methods=['GET'])
def get_vehicle(license_number):
    vehicle = vehicle_controller.get_vehicle(license_number)
    if vehicle:
        return jsonify(vehicle)
    else:
        return jsonify({'message': 'Vehicle not found'}), 404

@app.route('/vehicles/')
def get_all_vehicles():
    vehicles = vehicle_controller.get_all_vehicles()
    return jsonify(vehicles)

@app.route('/vehicle/delete/<license_number>', methods=['DELETE'])
def delete_vehicle(license_number):
    result = vehicle_controller.delete_vehicle(license_number)
    if result:
        return jsonify({'message': 'Vehicle deleted successfully'})
    else:
        return jsonify({'message': 'Failed to delete vehicle'}), 500

if __name__ == '__main__':
    app.run(debug=True)