from healthMenu import BhMenu
from healthMenu import Meal

def stopAdd(msg):
    answ = input(f"Do you want to continue {msg} (Y/N)? ")
    return True if 'y' in answ.lower() else False

print('Script for menu creation')
day_of_np = int(input('Please enter the day of the nutrition plan: '))
daily_meals = ['breakfast', 'lunch', 'dinner', 'snack', 'snack']

add_meals = True

weekly_menu = []

while add_meals:
    day_of_np = int(input('Please enter the day of the nutrition plan: '))
    day_menu = BhMenu(day_of_np)

    for entry in daily_meals:
        print(f'Adding ingredients to {entry}')
        meal_variant = int(input(f'Please enter the {entry} variant (1, 2, 3 etc...): '))
        meal_entry = Meal(entry, meal_variant, day_of_np)
        add_inreds = True
        while add_inred:
           meal_entry.addIngredient(input('Please add ingredient name: '), \
                 int(input('Please add quantity: ')))
           add_ingreds = stopAdd('adding more ingredients')

    add_meals = stopAdd('adding more meals to the menu')






