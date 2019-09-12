# Recipe Batches

Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:

```python
{
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}
```

The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you.

Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary.

For example

```python
# should return 0 since we don't have enough butter!
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)
```

## Testing

Run the test file by executing `python test_recipe_batches.py`.

You can also test your implementation manually by executing `python recipe_batches.py`.

## Hints

- If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
- What's the _minimum_ number of loops we need to perform in order to write a working implementation?

can use math
write function receiving a dictionary of recipes and a dictionary of ingredients, they have the same form
keys = ingredient names
value = amount needed / have
batches = ?
output the maximum number of whole batches that can be made with current ingredients if lacking ingredients return 0

if the same keys are not in the compared dictionaries return 0
sort the keys in both dictionaries to compare them

function(recipe, ingredients)
batches = None

go over lists and compare ingredients needed to current ingredients

for key, value in recipe items
if sorted recipe keys != sorted ingredients keys
return 0

    make = ingredients[k] // v

    if batches is None or make < batches
      batches = make

return batches
