class Plant:
    def __init__(self, name, good_companion_plants, bad_companion_plants):
        self.name = name
        self.good_companion_plants = good_companion_plants
        self.bad_companion_plants = bad_companion_plants
        self.general_sum = 0
    
    def set_gcp_distances_sum(self, sum):
        self.gcp_distances_sum = sum
    
    def set_bcp_distances_sum(self, sum):
        self.bcp_distances_sum = sum

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
            "good_companion_plants": self.good_companion_plants,
            "bad_companion_plants": self.bad_companion_plants,
            "general_sum": self.general_sum
        }