import os
from Plant import Plant
from supabase import create_client, Client
from sqlalchemy import create_engine
from dotenv import load_dotenv
from Garden import Garden
from GardenCalculator import GardenCalculator

load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


response = supabase.table('companion_plants').select("*").execute()
all_plants = []
for plant in response.data:
    new_plant = Plant(plant["name"], plant["good_plants_names"], plant["bad_plants_names"])
    all_plants.append(new_plant)
    print(new_plant)

gc = GardenCalculator(3, 2, all_plants[16:32])
gc.find_best_garden()