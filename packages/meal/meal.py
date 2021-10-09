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

   meal_types = ['breakfast','lunch','snack','dinner']

   def __init__(self, m_type: str, m_variant: int, dop: int):
       self.ingredients = list()
       self.__set_MealType(m_type)
       self.__set_MealVariant(m_variant)
       self.__set_DOP(dop)
       self.notes = 'Nothing to see here! Move along...'

   def __set_MealType(self, menu_type):
      if not menu_type.lower() in self.meal_types:
         raise ValueError(f'Meal type must be one of: {self.meal_types}')
      self.m_type = menu_type

   def __set_MealVariant(self, variant):
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
         dict entries for each ingredinet'''
      return self.ingredients
