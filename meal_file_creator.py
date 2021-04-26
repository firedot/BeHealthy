import json
import os
import argparse
from random import randint

parser = argparse.ArgumentParser()

parser.add_argument('--manual', '-m',
                    metavar = 'Choose manual mode of operation'
                    )

parser.add_argument('--filename', '-f',
                    metavar = 'Name of the meal file'
                    )

args = parser.parse_args()

# Define classes

class mealFile:

    def _readFile(file):
        with open(file, 'r') as input_file:
            return json.loads(input_file.read())

    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.exists(file_name):
            self.body = _readFile(self.file_name)
        else:
            self.body = dict(title='mealfile', version=1, day_meals=[])

    def addMeal(self, meal: dict):
        """
        adds a dictionary containing a meal
        to the meal file.
        The meal is structured like follows:
            {meal_type: brekfast/snack/lunch/dinner,
             ingredients: {ingredient_1: qty, ingredient_2: qty},
             nutrition_day: 1-30,
             meal_variant: 1-10
             }
        """
       self.body['day_meals'].append(meal)

    def writeFile():
        with open(self.name, 'w') as output_file:
            if not os.path.exists(self.name):

# Define functions

def CreateMeal(meal_type: str, ingredients: dict,
               nutrition_day: int,
               meal_variant: int):

    meal = dict()
    meal['meal_type'] = meal_type
    meal['ingredients'] = ingredients
    meal['nutrition_day'] = nutrition_day
    meal['meal_variant'] = meal_variant

    return meal


if __name__ == "__main__":
    done = False
    meal_1 = mealFile(args.filename)

    if args.m == 'm':
        while not done:
            m_type = input('Please enter the meal type: ')
            ingredients = input('Please add ingredients. I.e. food:qty: ')
            n_day = int(input('Please add to '))
            m_variant = int(input('Please add meal variant number: '))
            meal = CreateMeal(m_type, ingredients, n_day, m_variant)
            meal_1.addMeal(meal)
            end = input('Do you want to continue (Y\N): ')
            if end == 'N':
                print('Finished adding meals.')
                done = True

        print('Writing {0}'.format(meal_1.file_name))
        meal_1.writeFile()





