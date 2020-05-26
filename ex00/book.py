from datetime import datetime
from recipe import Recipe


class Book:

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        for key, val in self.recipe_list.items():
            for recipe in val:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe
        print('I do not know this recipe')

    def get_all_recipes_by_type(self, recipe_type):
        try:
            for recipe in self.recipe_list[recipe_type]:
                print(recipe.name)
        except KeyError:
            print('Not a valid recipe type')

    def add_recipe(self, recipe):
        if type(recipe) != Recipe:
            print('Not a valid recipe')
            return
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        print('Recipe for %s successfully added' % recipe.name)
