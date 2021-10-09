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

   def addIngredient(ingredient, qty):
      entry = {ingredient:qty}
      self.ingredients.append(entry)



