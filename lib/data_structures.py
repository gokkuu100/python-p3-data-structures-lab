spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = [x["name"] for x in spicy_foods]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest = [dict(foods) for foods in spicy_foods if foods["heat_level"]>5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisineBased = [dict(food) for food in spicy_foods if food["cuisine"] == cuisine]
    return cuisineBased

def print_spiciest_foods(spicy_foods):
        for food in spicy_foods:
            if food["heat_level"] > 5:
                heat_level_emojis = "🌶" * food["heat_level"]
                print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
   total_heat = sum(foods["heat_level"] for foods in spicy_foods)
   average = total_heat / len(spicy_foods)
   return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

    


# print(get_names(spicy_foods))
# print(get_spiciest_foods(spicy_foods))
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
# print(print_spicy_foods(spicy_foods))
# print(print_spiciest_foods(spicy_foods))
# print(get_average_heat_level(spicy_foods))
newFood = dict(name="Bitui", cuisine="African", heat_level= 8)
print(create_spicy_food(spicy_foods, newFood))