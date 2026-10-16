"""UUUU"""
RECIPE_INGREDIENTS = {
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts",
}

CORRECT_TASTES = {"Sweet", "Sour", "Salty"}

ingredients = set()
while True:
    item = input().strip()
    if item == "Cook":
        break
    ingredients.add(item)

tastes = set()
while True:
    item = input().strip()
    if item == "End":
        break
    tastes.add(item)

if not ingredients.issubset(RECIPE_INGREDIENTS):
    print("This is not Pad Thai!!!")

elif ingredients != RECIPE_INGREDIENTS:
    print("This is bad!")

else:
    if tastes == CORRECT_TASTES:
        print("Delicious!")
    else:
        print("Not Bad...")
