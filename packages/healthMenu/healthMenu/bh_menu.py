from meal import Meal

class BhMenu:
   '''
   A class fore representation of a daily menu

   Attributes
   ----------
   dop: int
       For which day of the nutrition plan is the menu

   meals: list
       List with all meals for the current day

   Methods
   -------
   addMeal(m)
       adds a meal object to the menu

   listMenu()
       lists all meals from the menu
   '''

   def __init__(self, dop: int):
      self.dop = dop
      self.meals = []

   def addMeal(self, m: Meal):
      self.meals.append(m)

   def listMenu(self):
      return self.meals


