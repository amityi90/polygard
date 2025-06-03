/*

    fetching plants with companion:

*/

SELECT 
    p1.plant_id AS plant_id, 
    p1.name AS plant_name, 
    p2.plant_id AS related_plant_id, 
    p2.name AS related_plant_name
FROM 
    companion_plants_plants pr
INNER JOIN 
    plants p1 ON pr.main_plant_id = p1.plant_id
INNER JOIN 
    plants p2 ON pr.companion_plant_id = p2.plant_id;