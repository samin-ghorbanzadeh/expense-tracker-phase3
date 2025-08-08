import json
category = [
    "food",
    "transport",
    "shopping",
    "utilities",
    "groceries"
]
with open ("data.json" , "w" , encoding = "utf-8") as file:
    json.dump(category , file , indent=4  , ensure_ascii= False)
    

