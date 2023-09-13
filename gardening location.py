#   ____   U  ___ u  _   _     _   _     U  ___ u   ____      _   _                            
#U /"___|   \/"_ \/ | \ |"|   | \ |"|     \/"_ \/U |  _"\ u  |'| |'|                           
#\| | u     | | | |<|  \| |> <|  \| |>    | | | | \| |_) |/ /| |_| |\                          
# | |/__.-,_| |_| |U| |\  |u U| |\  |u.-,_| |_| |  |  _ <   U|  _  |u                          
#  \____|\_)-\___/  |_| \_|   |_| \_|  \_)-\___/   |_| \_\   |_| |_|                           
# _// \\      \\    ||   \\,-.||   \\,-.    \\     //   \\_  //   \\                           
#(__)(__)    (__)   (_")  (_/ (_")  (_/    (__)   (__)  (__)(_") ("_)                          
#                                                                                              
#                                                                                             
#                                                                                              
#                                                                                              
#                                                                                              
#                                                                                              
#                                                                                              
# __     __ U _____ u   ____     ____                U  ___ u  _   _            _      _  _    
# \ \   /"/u\| ___"|/U |  _"\ u / __"| u      ___     \/"_ \/ | \ |"|          /"|    | ||"|   
#  \ \ / //  |  _|"   \| |_) |/<\___ \/      |_"_|    | | | |<|  \| |>       u | |u   | || |_  
#  /\ V /_,-.| |___    |  _ <   u___) |       | | .-,_| |_| |U| |\  |u        \| |/   |__   _| 
# U  \_/-(_/ |_____|   |_| \_\  |____/>>    U/| |\u\_)-\___/  |_| \_|          |_|   _  /|_|\  
#   //       <<   >>   //   \\_  )(  (__).-,_|___|_,-.  \\    ||   \\,-.     _//<,-,(")u_|||_u 
#  (__)     (__) (__) (__)  (__)(__)      \_)-' '-(_/  (__)   (_")  (_/     (__)(_/  " (__)__) 

import requests
from datetime import datetime

# Function to fetch USDA Zone using the API
def get_usda_zone(zip_code):
    try:
        url = f"https://phzmapi.org/{zip_code}.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            usda_zone = data.get("zone")
            return usda_zone
        return None  # ZIP code not found in the API
    except Exception as e:
        print("Error:", str(e))
        return None

def suggest_plants(usda_zone, current_month):
    # Define planting recommendations based on USDA Hardiness Zone and current month
    planting_recommendations = {
        '1a': {
            'Spring': "Not suitable for spring planting in this zone.",
            'Summer': "Not suitable for summer planting in this zone.",
            'Fall': "Not suitable for fall planting in this zone."
        },
        '1b': {
            'Spring': "Not suitable for spring planting in this zone.",
            'Summer': "Not suitable for summer planting in this zone.",
            'Fall': "Not suitable for fall planting in this zone."
        },
        '2a': {
            'Spring': "Not suitable for spring planting in this zone.",
            'Summer': "Not suitable for summer planting in this zone.",
            'Fall': "Not suitable for fall planting in this zone."
        },
        # Define recommendations for other zones and seasons as needed
    }

    zone_recommendations = planting_recommendations.get(usda_zone, {})

    current_season = "Spring"  # Default to spring
    if 5 <= current_month <= 7:
        current_season = "Summer"
    elif 8 <= current_month <= 10:
        current_season = "Fall"

    recommendations = zone_recommendations.get(current_season, "No specific recommendations available for this season in this zone.")

    return recommendations

if __name__ == "__main__":
    print("Welcome to the Planting Recommendations Script!")

    while True:
        zip_code = input("Enter the ZIP code: ")
        current_month = datetime.now().month

        usda_zone = get_usda_zone(zip_code)

        if usda_zone is not None:
            planting_recommendations = suggest_plants(usda_zone, current_month)
            print(f"\nUSDA Hardiness Zone for ZIP code {zip_code}: {usda_zone.upper()}")
            print(f"Planting recommendations for the current month and season:\n")
            print(planting_recommendations)
        else:
            print("ZIP code not found in the API.")

        continue_or_quit = input("Press Enter to check another location or 'q' to quit: ")
        if continue_or_quit.lower() == 'q':
            break
