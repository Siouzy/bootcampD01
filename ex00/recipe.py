from datetime import datetime


class Recipe:

    __recipe_type_types = ['lunch', 'dessert', 'starter']

    def __init__(
            self,
            name,
            cooking_lvl,
            cooking_time,
            ingredients,
            recipe_type,
            description=''):
        if recipe_type not in self.__recipe_type_types:
            print('Not a valid recipe type')
            return
        self.ingredients = ingredients.split(',')
        if len(self.ingredients) == 0:
            print('ingredients list cannot be empty')
            return
        if len(name) == 0:
            print('name cannot be empty')
            return
        try:
            self.name = name
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.recipe_type = recipe_type
            self.description = description
        except ValueError:
            print('cooking_lvl and cooking_time must be intergers')
            return

    def __str__(self):
        format_str1 = "{:s} is a level {:d} recipe with ingredients:"
        format_str2 = ''
        for ing in self.ingredients:
            format_str2 += "- {:s}\n"
        format_str3 = "It is a {:s} that will take you {:d} minutes to prepare"
        format_str = '\n'.join(
            [format_str1, format_str2, format_str3, self.description]
            )
        t = (
            self.name,
            self.cooking_lvl
            ) + tuple(
                i for i in self.ingredients
                ) + (
                    self.recipe_type,
                    self.cooking_time
                    )
        txt = format_str.format(*t)
        return txt
