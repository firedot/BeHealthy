from healthMenu import bh_menu
from healthMenu import meal

'''
TO-DO:

-   Major refactor wherever possible
-   Write the menu to a file (JSON / CSV - optional)
-   add ingredients without asking Y/N (continuosly add until stopped)
'''
def stopAdd(msg):
    answ = input(f"Do you want to continue {msg} (Y/N)? ")
    return True if 'y' in answ.lower() else False

def validateInput(data, msg):
    '''
    validate if the input data is the correct type
    and if it is return propper msg
    '''

    userInput = input(msg)

    while  (data == 'num' and not userInput.isnumeric()):
       print('Please input an integer!')
       userInput = input(msg)

    if userInput.isnumeric():
       userInput = int(userInput)

    return userInput

print('Script for menu creation')
daily_meals = ['breakfast', 'lunch', 'dinner', 'snack', 'snack']

add_meals = True

weekly_menu = []

while add_meals:
    day_of_np = validateInput('num','Please enter the day of the nutrition plan: ')
    day_menu = bh_menu.BhMenu(day_of_np)

    for entry in daily_meals:
        print(f'Adding ingredients to {entry}')
        meal_variant = validateInput('num', f'Please enter the {entry} variant (1, 2, 3 etc...): ')
        meal_entry = meal.Meal(entry, meal_variant, day_of_np)
        add_ingreds = True
        print('Enter ingredients until keyword "stop" or "exit" to quit')
        while add_ingreds:
           ingredient = validateInput('text', 'Add ingredient: ')
           if ingredient.lower() == 'stop':
              add_ingreds = False
              break
           elif ingredient.lower() == 'exit':
              exit(0)

           qty = validateInput('num', 'Add quantity: ')
           meal_entry.addIngredient(ingredient, qty)

    weekly_menu.append(day_menu)

    add_meals = stopAdd('adding more meals to the menu')

for entry.listMenu() in weekly_menu:
   for entry_1.getMealIngredients in entry:
      for key, val in entry_1.listMenu():
         print(key, val)





