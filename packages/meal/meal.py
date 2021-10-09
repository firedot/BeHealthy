'''
DOD: Class which will hold 
     - Ingredients
     - quantity
     - meal type
     - meal varaint no.
     - may be prep notes
     Methods:
        add ingredinet: dict(name, qty)
        return ingredients: list(dict(name:qty))
'''

class Meal:

   def __init__(self, m_type, m_variant):
       self.ingredients = list()
       self.m_type = m_type
       self.m_variant = m_variant
       self.notes = 'Nothing to see here! Move along...'

   def addIngredient(self, ingredient: str, qty: int):
      '''Adds ingredinet entry to ingredients'''
      entry = {ingredient:qty}
      self.ingredients.append(entry)

   def addNotes(self, notes: str):
      '''Adds meal prep notes if any'''
      self.notes = notes


   def getMealIngredients(self):
      '''Returns list containing
         dict entries for each ingredinet'''
      return self.ingredients
