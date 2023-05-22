from flask import Flask, render_template, request, jsonify
import forms

from controller.CurrentPosition import CurrentPosition
from controller.VehicleController import VehicleController
from model.Vehicle import Vehicle

app = Flask(__name__)
vehicle_controller = VehicleController(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vehicle/create', methods=['POST'])
def create_vehicle():
    print("sfdsfds")
    # data = request.get_json()
    # license_number = data.get('license_number')
    # password = data.get('password')
    # current_position = data.get('current_position')
    # current_route_id = data.get('current_route_id')

    # if license_number and password and current_position and current_route_id:
    #     vehicle = Vehicle(license_number, password, current_position, current_route_id)
    #     result = vehicle_controller.create_vehicle(vehicle)
    #     if result:
    #         return jsonify({'message': 'Vehicle created successfully'})
    #     else:
    #         return jsonify({'message': 'Failed to create vehicle'}), 500
    # else:
    #     return jsonify({'message': 'Invalid request'}), 400

@app.route('/vehicle/get/<license_number>')
def get_vehicle(license_number):
    vehicle = vehicle_controller.get_vehicle(license_number)
    if vehicle:
        return jsonify({'vehicle': vehicle.__dict__})
    else:
        return jsonify({'message': 'Vehicle not found'}), 404

@app.route('/vehicles/')
def get_all_vehicles():
    vehicles = vehicle_controller.get_all_vehicles()
    vehicle_list = [vehicle.__dict__ for vehicle in vehicles]
    return jsonify({'vehicles': vehicle_list})

@app.route('/vehicle/delete/<license_number>', methods=['DELETE'])
def delete_vehicle(license_number):
    result = vehicle_controller.delete_vehicle(license_number)
    if result:
        return jsonify({'message': 'Vehicle deleted successfully'})
    else:
        return jsonify({'message': 'Failed to delete vehicle'}), 500

if __name__ == '__main__':
    app.run()