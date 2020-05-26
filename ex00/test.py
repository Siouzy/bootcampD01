from book import Book
from recipe import Recipe

white_russian = Recipe(
    'white russian',
    2,
    3,
    ['milk', 'vodka', 'ice', 'kalua'],
    'dessert',
    'A nice and sweet cocktail'
    )
to_print = str(white_russian)
print(1)
print(to_print)

my_book = Book('Cocktails')
print('creation date: ', my_book.creation_date)
print('last update: ', my_book.last_update)
print(2)
my_book.add_recipe('kikou')
print(3)
my_book.add_recipe(white_russian)
print('last update: ', my_book.last_update)
print(4)
white_russian_2 = my_book.get_recipe_by_name('white russian')
other_book = Book('Other')
print(5)
other_book.add_recipe(white_russian_2)
print(6)
other_book.get_all_recipes_by_type('starter')
print(7)
other_book.get_all_recipes_by_type('dessert')

bloody_mary = Recipe(
    'bloody mary',
    4,
    4,
    ['tomato juice', 'vodka', 'ice', 'celery salt', 'pepper', 'tabasco'],
    'lunch',
    'A spicy drink that will fill you like a meal!'
)
print(8)
my_book.add_recipe(bloody_mary)

pastaga = Recipe(
    'Pastis',
    0,
    1,
    ['pastis', 'ice', 'water'],
    'starter',
    'The perfect starter to any summer meal'
)
print(9)
my_book.add_recipe(pastaga)

print(10)
for cat, val in my_book.recipe_list.items():
    print(cat)
    for recipe in val:
        print(recipe)

cheesecake = Recipe(
    'cheesecake',
    5,
    60,
    ['mascarpone', 'yogourt', 'sugar', 'eggs', 'speculos', 'walnuts', 'flour'],
    'dessert',
    'The famous dessert from New-York, with a creamy twist!'
)
print(11)
other_book.add_recipe(cheesecake)
print(12)
other_book.get_all_recipes_by_type('dessert')
