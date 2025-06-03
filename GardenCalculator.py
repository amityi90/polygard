from itertools import permutations
from Garden import Garden
import numpy as np

class GardenCalculator:
    def __init__(self, heigt, width, plants_list):
        self.heigt = heigt
        self.width = width
        self.plants_list = plants_list
    
    def init_garden_matrix(self, plants_list):
        np_updated_plants_list = np.array(plants_list)
        garden_matrix = np_updated_plants_list.reshape(self.heigt, self.width)
        return garden_matrix
    
    def resize_plants_list(self):
        updated_plants_list = []
        len_updated_plants_list = self.width * self.heigt 
        if len(self.plants_list) >= len_updated_plants_list:
            updated_plants_list = self.plants_list[:len_updated_plants_list]
        else:
            while len(updated_plants_list) < len_updated_plants_list:
                updated_plants_list += self.plants_list
            updated_plants_list = updated_plants_list[:len_updated_plants_list]
        return updated_plants_list

    
    def find_best_garden(self):
        def get_attribute(obj):
            return obj.name    
        highest_garden_value = -10000000
        highest_garden_order = ""
        orders_and_values = [] 
        resized_plant_list = self.resize_plants_list()
        permuted_plants_list = list(permutations(resized_plant_list))
        for optionaly_order in permuted_plants_list:
            # print("\n", np.vectorize(get_attribute)(optionaly_order))
            new_garden_matrix = self.init_garden_matrix(optionaly_order)
            #  print("\n", np.vectorize(get_attribute)(new_garden_matrix))
            new_garden = Garden(3, 2, [], new_garden_matrix)
            distance_value = new_garden.init_and_return_distances_value()
            # new_garden.print_plant_matrix_names()
            if distance_value > highest_garden_value:
                highest_garden_value = distance_value
                highest_garden_order = new_garden.print_plant_matrix_names()
            print(f"\n ------ garden value: {distance_value} \n----highest value: {highest_garden_value}  \n-{highest_garden_order}-\n\n")
            orders_and_values.append({"order": new_garden_matrix, "garden": new_garden, "distance_value": distance_value})
        best_garden = max(orders_and_values, key=lambda x: x["distance_value"])
        print(best_garden["garden"].print_plant_matrix_names(), f"\n\nvalue: {best_garden['distance_value']} \n {np.vectorize(get_attribute)(best_garden['order'])}")
        return best_garden["garden"]
        