from flask import Flask, render_template, request, jsonify

from controller.CurrentPosition import CurrentPosition
from controller.VehicleController import VehicleController
from model.Vehicle import Vehicle

app = Flask(__name__)
vehicle_controller = VehicleController(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vehicle_reg')
def vehicle_reg():
    return render_template('vehicle_reg.html')

@app.route('/vehicle/create', methods=['POST'])
def create_vehicle():
    # data = request.form.to_dict()
    # license_number = data['license_number']
    # password = data['password']
    # current_position = CurrentPosition().get_current_location3()
    # current_route_id = {}

    # if license_number and password and current_position:
    #     vehicle = Vehicle(license_number, password, current_position, current_route_id)
    #     result = vehicle_controller.create_vehicle(vehicle)
    #     if result:
    #         return jsonify({'message': 'Vehicle created successfully'})
    #     else:
    #         return jsonify({'message': 'Failed to create vehicle'}), 500
    # else:
    #     return jsonify({'message': 'Invalid request'}), 400

# @app.route('/vehicle/create', methods=['POST'])
# def update_vehicle():
    response = request.get_json()
    vehicle = Vehicle(response["license_number"], response["password"], response["current_position"], response["current_route_id"])
    result = vehicle_controller.create_vehicle(vehicle)
    if result:
            return jsonify({'message': 'Vehicle created successfully'})
    else:
        return jsonify({'message': 'Failed to create vehicle'}), 500
    
@app.route('/vehicle/update', methods=['PUT'])
def update_vehicle():
    response = request.get_json()
    search = get_vehicle(response["license_number"])
    if search:
        vehicle = Vehicle(response["license_number"], response["password"],CurrentPosition().get_current_location3(), response["current_route_id"])
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