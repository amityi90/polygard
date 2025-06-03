class Plant:
    def __init__(self, name, companion_plants = None, antagonistic_plants = None):
        self.name = name
        self.companion_plants = companion_plants
        self.antagonistic_plants = antagonistic_plants
        self.general_sum = 0
        if not self.companion_plants:
            self.companion_plants = []
        if not self.antagonistic_plants:
            self.antagonistic_plants = []

    def insert_companion_plant(self, companion_plant):
        if not self.companion_plants:
            self.companion_plants = []
        self.companion_plants.append(companion_plant)

    def insert_antagonistic_plant(self, antagonistic_plant):
        if not self.antagonistic_plants:
            self.antagonistic_plants = []
        self.antagonistic_plants.append(antagonistic_plant)
    
    def set_companion_distances_sum(self, sum):
        self.companion_distances_sum = sum
    
    def set_antagonistic_distances_sum(self, sum):
        self.antagonistic_distances_sum = sum

    def set_general_sum(self, sum):
        self.general_sum = sum
    
    def __str__(self):  
        return "name: " + self.name
    
    def to_dict(self):
        """
        Convert the Plant instance to a dictionary for JSON serialization.
        """
        return {
            "name": self.name,
            "companion_plants": self.companion_plants,
            "antagonistic_plants": self.antagonistic_plants,
            "general_sum": self.general_sum
        }
    


# class Plant:
#     def __init__(self, name, companion_plants, antagonistic_plants):
#         self.name = name
#         self.companion_plants = companion_plants
#         self.antagonistic_plants = antagonistic_plants
#         self.general_sum = 0
    
#     def set_gcp_distances_sum(self, sum):
#         self.gcp_distances_sum = sum
    
#     def set_bcp_distances_sum(self, sum):
#         self.bcp_distances_sum = sum

#     def set_general_sum(self, sum):
#         self.general_sum = sum
    
#     def __str__(self):  
#         return "name: " + self.name
    
#     def to_dict(self):
#         """
#         Convert the Plant instance to a dictionary for JSON serialization.
#         """
#         return {
#             "name": self.name,
#             "companion_plants": self.companion_plants,
#             "antagonistic_plants": self.antagonistic_plants,
#             "general_sum": self.general_sum
#         }