from flask import Flask, request, jsonify
import os
from models.plant import Plant
from supabase import create_client, Client
from sqlalchemy import create_engine
from dotenv import load_dotenv
from Garden import Garden
from GardenCalculator import GardenCalculator
import numpy as np
import pandas as pd
import math
from controller import Controller
import json
from flask_cors import CORS


controller = Controller()

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)
CORS(app)

@app.route('/all_plants', methods=['GET'])
def get_all_plants():
    """
    Return a list of all of the plants.
    """
    all_plants = controller.create_plants_list_from_DB()
    plant_strings = [json.dumps(plant.to_dict()) for plant in all_plants]

    return jsonify({"all_plants": plant_strings}), 200


@app.route('/make_garden', methods=['GET'])
def make_garden():
    all_plants = controller.create_plants_list_from_DB()
    gc = GardenCalculator(3, 2, all_plants)
    best_order = gc.find_best_garden()
    df = best_order.print_plant_matrix_names()
    df_json = df.to_json(orient='records')
    print("\n-----------\n")
    print(all_plants)
    print("\n-----------\n")
    return jsonify({"garden": df_json}), 201

@app.route('/make_garden_by_recived_args', methods=['POST'])
def make_garden_by_recived_args():
    data = request.json
    all_plants = []
    print("\n-----------\n")
    print(data["plants"])
    print("\n-----------\n")
    for plant in data["plants"]:
        new_plant = Plant(plant["name"], plant["companion_plants"], plant["antagonistic_plants"])
        all_plants.append(new_plant)
    print("\n-----------\n")
    print(all_plants)
    print("\n-----------\n")
    gc = GardenCalculator(data["width"], data["height"], all_plants)
    best_order = gc.find_best_garden()
    df = best_order.print_plant_matrix_names()
    df_json = df.to_json(orient='records')
    
    return jsonify({"garden": df_json}), 201

@app.route('/get_plant_data', methods=['POST'])
def get_plant_data():
    data = request.json
    response = supabase.table('companion_plants').select("name=Apple").execute()
    print(response)
    
    return jsonify({"plant": data["plant_name"]}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
