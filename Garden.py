import numpy as np
import pandas as pd
import math


class Garden:
    def __init__(self, heigt, width, plants, garden_matrix):
        self.heigt = heigt
        self.width = width
        self.plants = plants
        self.garden_matrix = garden_matrix
        self.distances_value = 0
    
    def set_distsances(self):
        for x_current_plant in range(self.width):
            for y_current_plant in range(self.heigt):
                current_plant = self.garden_matrix[y_current_plant][x_current_plant]
                gcp_sum_of_distances = 0
                bcp_sum_of_distances = 0
                for x_companion_plant in range(self.width):
                    for y_companion_plant in range(self.heigt):
                        companion_plant = self.garden_matrix[y_companion_plant][x_companion_plant]
                        if companion_plant.name in current_plant.good_companion_plants:
                            distance = math.sqrt((x_companion_plant - x_current_plant) ** 2 + (y_companion_plant - y_current_plant) ** 2)
                            if distance != 0:
                                gcp_sum_of_distances += 1 / abs(distance)
                        elif companion_plant.name in current_plant.bad_companion_plants:
                            distance = math.sqrt((x_companion_plant - x_current_plant) ** 2 + (y_companion_plant - y_current_plant) ** 2)
                            if distance != 0:
                                bcp_sum_of_distances += 1 / -abs(distance)
                current_plant.set_gcp_distances_sum(gcp_sum_of_distances)
                current_plant.set_bcp_distances_sum(bcp_sum_of_distances)
                current_plant.set_general_sum(gcp_sum_of_distances + bcp_sum_of_distances)

    def print_plant_matrix_names(self):
        def get_attribute(obj):
            return obj.name 
        garden_matrix_names = np.vectorize(get_attribute)(self.garden_matrix)
        df_garden_matrix_names = pd.DataFrame(garden_matrix_names)
        return df_garden_matrix_names
    
    def set_garden_value(self):
        def get_attribute(obj):
            return obj.general_sum 
        garden_matrix_distances = np.vectorize(get_attribute)(self.garden_matrix)
        df_garden_matrix_distances = pd.DataFrame(garden_matrix_distances)
        self.distances_value = df_garden_matrix_distances.values.sum()
    
    def init_and_return_distances_value(self):
        self.set_distsances()
        self.print_plant_matrix_names()
        self.set_garden_value()
        return self.distances_value

    

                        

    


    
