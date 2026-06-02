import pytest
from classes import Ingredient
from classes import Recipe

def test_init_name_quantity_unit():
    ingredient = Ingredient('Bread',300.0,'г')
    assert ingredient.name == 'Bread'
    assert ingredient.quantity == 300.0
    assert ingredient.unit == 'г'

def test_str_name_quantity_unit():
    ingredient = Ingredient('Bread',300.0,'г')
    assert str(ingredient) == "Bread: 300.0 г"

def test_eq1_name_quantity_unit():
    ingredient1 = Ingredient('Bread',300.0,'г')
    ingredient2 = Ingredient('Bread',500.0,'г')
    ingredient3 = Ingredient('Cucumber',300.0,'г')
    ingredient4 = Ingredient('Bread',300.0,'кг')
    ingredient5 = Ingredient('Bread',300.0,'г')

    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert ingredient1 != ingredient4
    assert ingredient1 == ingredient5

def test_init_title_ingredients():
    ingredient = Ingredient('Bread',300.0,'г')
    recipe = Recipe('Sandwich',[ingredient])
    assert recipe.title == 'Sandwich'
    assert len(recipe.ingredients) == 1
def test_add_ingredient1():
    ingredient = Ingredient('Bread',300.0,'г')
    recipe = Recipe('Sandwich',[ingredient])
    ingredient2 = Ingredient('Bread',500.0,'г')
    recipe.add_ingredient(ingredient2)
    assert len(recipe.ingredients) == 1
    for el in recipe.ingredients:
        assert el.quantity == 800.0
def test_add_ingredient2():
    ingredient = Ingredient('Bread',300.0,'г')
    recipe = Recipe('Sandwich',[ingredient])
    ingredient3 = Ingredient('Cucumber',300.0,'г')
    recipe.add_ingredient(ingredient3)
    assert len(recipe.ingredients) == 2

def test_scale1():
    ingredient = Ingredient('Bread',300.0,'г')
    recipe = Recipe('Sandwich',[ingredient])
    new_recipe = recipe.scale(2)
    assert recipe.ingredients[0].quantity == 300.0
    assert new_recipe.ingredients[0].quantity == 600.0
    with pytest.raises(ValueError):
        recipe.scale(-5)
def test_len():
    ingredient = Ingredient('Bread',300.0,'г')
    recipe = Recipe('Sandwich',[ingredient])
    assert len(recipe.ingredients) == 1
