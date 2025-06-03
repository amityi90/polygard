import os
from supabase import create_client, Client
from dotenv import load_dotenv



class Database:
    def __init__(self):
        load_dotenv()
        self.url: str = os.environ.get("SUPABASE_URL")
        self.key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(self.url, self.key)

    def ex(self):
        response = self.supabase.table('plants').select("*").execute()
        return response
    
    def get_all_plants_with_companions(self):
        response = self.supabase.table("companion_plants_plants") \
            .select("main_plant_id, companion_plant_id, main_plant:plants!fk_main_plant(name), companion_plant:plants!fk_companion_plant(name)") \
            .execute()
        return response

    def get_all_plants_with_antagonistic(self):
        response = self.supabase.table("antagonistic_plants_plants") \
            .select("main_plant_id, antagonistic_plant_id, main_plant:plants!fk_main_plant_id(name), antagonistic_plant:plants!fk_antagonistic_plant_id(name)") \
            .execute()
        return response


    