from database import Database
from models.plant import Plant


class Controller:
    def __init__(self):
        database = Database()
        self.database = database

    def create_plants_list_from_DB(self):
        all_plants = []
        all_plants_names = []
        companions_raw_list = self.database.get_all_plants_with_companions()
        antagonistic_raw_list = self.database.get_all_plants_with_antagonistic()
        print('\n')
        for plant in companions_raw_list.data:
            if not (any(check_plant == plant['main_plant']['name'] for check_plant in all_plants_names)):
                new_plant = Plant(plant['main_plant']['name'])
                all_plants.append(new_plant)
                all_plants_names.append(plant['main_plant']['name'])
            plant_index = all_plants_names.index(plant['main_plant']['name'])
            all_plants[plant_index].insert_companion_plant(plant['companion_plant']['name'])
        for plant in antagonistic_raw_list.data:
            if not (any(check_plant == plant['main_plant']['name'] for check_plant in all_plants_names)):
                new_plant = Plant(plant['main_plant']['name'])
                all_plants.append(new_plant)
                all_plants_names.append(plant['main_plant']['name'])
            plant_index = all_plants_names.index(plant['main_plant']['name'])
            all_plants[plant_index].insert_antagonistic_plant(plant['antagonistic_plant']['name'])

        for plant in all_plants:
                print('\n', plant, '\n', plant.companion_plants, '\n', plant.antagonistic_plants)
                
        return all_plants
                       
test = Controller()
test.create_plants_list_from_DB()