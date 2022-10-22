import json


_7_indian_states_and_capitals = {"1. Andhra_pradesh" : "Amaravati", 
                                "2. Aurnachal_pradesh" : "Itanagar", 
                                "3. Assam" : "Dispur",
                                "4. Bihar" : "Patna", 
                                "5. Chhattisgarh" : "Raipur", 
                                "6 . Goa" : "Panaji", 
                                "7. Gujarat" : "Gandhinagar"}

print(_7_indian_states_and_capitals)

with open("C:\\Users\\Admin\OneDrive\\Desktop\\edy_assignment\\assignment6\\assignment_2\\states_and_capitals.json", "w") as json_file:
    json.dump(_7_indian_states_and_capitals, json_file, indent=2)
