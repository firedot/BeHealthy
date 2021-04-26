import json
import os
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--manual', '-m',
                    metavar = 'Choose manual mode of operation'
                    )
mealfiles = ['breakfast.json', 'lunch.json', 'dinner.json', 'snack.json']

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
        pass

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

# Check if meal files exist

for file in mealfiles:
    if not os.path.exists(file):
        print(f'Creating file {file}')
        file_struct = {[{'id': null, ''}]
