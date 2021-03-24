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

    data = {}

    def _readFile(filename):
        # Open previously created file
        with open(filename, 'r') as input_file:
            self.data = json.loads(input_file.read())

    def __init__(self, name):
        self.name = name
        if os.path.exists(self.name):
            _readFile(self.name)

    def addMeal(self.data):
        pass

    def writeFile():
        with open(self.name, 'w') as output_file:
            output_file.write(json.dumps(self.data))


# Check if meal files exist

for file in mealfiles:
    if not os.path.exists(file):
        print(f'Creating file {file}')
        file_struct = {[{'id': null, ''}]
