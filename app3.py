# from flask import Flask, request, jsonify
# import os
# from Plant import Plant
# from supabase import create_client, Client
# from sqlalchemy import create_engine
# from dotenv import load_dotenv
# from Garden import Garden
# from GardenCalculator import GardenCalculator
# import numpy as np
# import pandas as pd
# import math

# load_dotenv()

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(url, key)

# app = Flask(__name__)

# @app.route('/all_plants', methods=['GET'])
# def get_all_plants():
#     """
#     Return a list of all of the plants.
#     """
#     response = supabase.table('companion_plants').select("*").execute()
#     all_plants = []
#     for plant in response.data:
#         new_plant = Plant(plant["name"], plant["good_plants_names"], plant["bad_plants_names"])
#         all_plants.append(new_plant.to_dict())
#         # print(new_plant)
#     return jsonify(all_plants), 200




# @app.route('/make_garden', methods=['GET'])
# def make_garden():
#     response = supabase.table('companion_plants').select("*").execute()
#     all_plants = []
#     for plant in response.data:
#         new_plant = Plant(plant["name"], plant["good_plants_names"], plant["bad_plants_names"])
#         all_plants.append(new_plant)
#     gc = GardenCalculator(3, 2, all_plants[16:32])
#     best_order = gc.find_best_garden()
#     df = best_order.print_plant_matrix_names()
#     df_json = df.to_json(orient='records')
#     return jsonify({"garden": df_json}), 201

# @app.route('/make_garden_by_recived_args', methods=['POST'])
# def make_garden_by_recived_args():
#     data = request.json
#     all_plants = []
#     for plant in data["plants"]:
#         new_plant = Plant(plant["name"], plant["good_companion_plants"], plant["bad_companion_plants"])
#         all_plants.append(new_plant)
#     gc = GardenCalculator(data["width"], data["height"], all_plants)
#     best_order = gc.find_best_garden()
#     df = best_order.print_plant_matrix_names()
#     df_json = df.to_json(orient='records')
    
#     return jsonify({"garden": df_json}), 201

# @app.route('/get_plant_data', methods=['POST'])
# def get_plant_data():
#     data = request.json
#     response = supabase.table('companion_plants').select("name=Apple").execute()
#     print(response)
    
#     return jsonify({"plant": data["plant_name"]}), 201


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
