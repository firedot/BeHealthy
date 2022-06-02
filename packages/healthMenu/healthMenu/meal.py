class Meal:
   '''
   A class used to represent a singe meal

   Attributes
   ----------

   meal_types: str
      string of acceptable m_type values

   m_type: str
      type of the meal

   m_variant: int
      variant of the meal

   dop: int
       For which day of the nutrition plan the meal
       is planned

   Methods
   -------

   addIngredient(ingredient, qty)
      Adds an ingredient to the meal's ingredients list

   addNotes(notes)
      Adds a note for the meal

   getMealIngredients()
      Returns a list of dictionaries
      containing all ingredients and quantities

   '''

   meal_types = 'breakfast / lunch / snack / dinner'

   def __init__(self, m_type: str, m_variant: int, dop: int):
      if not m_type.lower() in self.meal_types:
         raise ValueError(f'Meal type must be one of: {self.meal_types}')
      elif not type(m_variant) is int or not type(dop) is int:
         raise TypeError('m_variant and dop must be an integers')
      else:
       self.ingredients = list()
       self.m_type = m_type
       self.m_variant = m_variant
       self.notes = 'Nothing to see here! Move along...'

   def addIngredient(self, ingredient: str, qty: int):
      '''Adds ingredinet entry to ingredients'''
      if not type(qty) is int:
         raise TypeError('Ingredient quantity must be an integer')
      else:
          entry = {ingredient:qty}
          self.ingredients.append(entry)

   def addNotes(self, notes: str):
      '''Adds meal prep notes if any'''
      self.notes = notes


   def getMealIngredients(self):
      '''Returns list containing
         dict entries for each ingredinet'''
      return self.ingredients
