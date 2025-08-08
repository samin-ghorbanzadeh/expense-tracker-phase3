import json

def category_check(Selected_category):
    category = load_category()
    if Selected_category in category:
        return True
    else:
        while True:
            answer = input(f"Do you want to enter a new category? (yes/no)\nCurrent categories: {category}\n")
            if answer.lower() == 'yes':
                new_category = input("Enter your new category: ")
                category.append(new_category)
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(category, file, indent=4, ensure_ascii=False)
                return new_category
            elif answer.lower() == 'no':
                while True:
                    right_form = input(f"Enter a valid category from the list: {category}\n")
                    if right_form in category:
                        return right_form
                    else:
                        print("Invalid category, please try again.")
            else:
                print("Please enter 'yes' or 'no'.")
                continue

def load_category():
    with open("data.json", "r", encoding="utf-8") as file:
        category = json.load(file)

    if not isinstance(category, list):
        raise ValueError("Data is not a list.")
    if not category:
        raise ValueError("Category list is empty.")
    for item in category:
        if not isinstance(item, str):
            raise ValueError("List must contain only strings.")
        if not item.strip():
            raise ValueError("Category strings cannot be empty or whitespace.")
    if len(category) != len(set(category)):
        raise ValueError("There are duplicate categories in the list.")

    return category

               
           
              
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    