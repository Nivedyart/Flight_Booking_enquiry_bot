from flask import  request, jsonify
from app import app
from app.main import process_user_input

#define route
@app.route('/flightbooking', methods = ['POST'])
def get_response():
    json_input = request.get_json(force = True)
    user_input = json_input["message"]
    response = process_user_input(user_input)
    return jsonify(response.__dict__)