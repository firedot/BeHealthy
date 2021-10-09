class Meal:
   __meal_types = ['breakfast','lunch','snack','dinner']

   def __init__(self, m_type: str, m_variant: int, dop: int):
       self.ingredients = list()
       self.__set_MealType(m_type)
       self.__set_MealVariant(m_variant)
       self.__set_DOP(dop)
       self.notes = 'Nothing to see here! Move along...'

   def __set_MealType(self, menu_type):
      '''Set the m_variant attribute'''
      if not menu_type.lower() in self.__meal_types:
         raise ValueError(f'Meal type must be one of: {self.__meal_types}')
      self.m_type = menu_type

   def __set_MealVariant(self, variant):
      '''Set the m_variant attribute'''
      if not type(variant) is int:
         raise TypeError('m_variant must be an integer')
      self.m_variant = variant

   def __set_DOP(self, dop):
      if not type(dop) is int:
         raise TypeError('m_variant must be an integer')
      self.dop = dop


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
         dict entries for each ingredient'''
      return self.ingredients
