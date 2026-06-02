import pytest
from classes import Ingredient
from classes import Recipe
from classes import ShoppingList

def test_init_name_quantity_unit():
    ingredient = Ingredient('Bread',300.0,'г')
    assert ingredient.name == 'Bread'
    assert ingredient.quantity == 300.0
    assert ingredient.unit == 'г'

def test_quantity():
    with pytest.raises(ValueError):
        Ingredient('Bread',-1,'г')

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
    assert len(recipe) == 1

def test_add_recipe():
    ingredient = Ingredient('Bread',300.0,'г')
    recipe = Recipe('Sandwich',[ingredient])
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipe,2)
    for el in shoppingList._items:
        assert el[0].quantity == 600.0
        assert el[1] == 'Sandwich'
    with pytest.raises(ValueError):
        shoppingList.add_recipe(recipe,-2)

def test_remove_recipe():
    ingredient1 = Ingredient('Bread',400.0,'г')
    recipe1 = Recipe('Sandwich Special',[ingredient1])
    ingredient2 = Ingredient('Bread',300.0,'г')
    recipe2 = Recipe('Sandwich Basic',[ingredient2])
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipe1,1)
    shoppingList.add_recipe(recipe2,1)
    shoppingList.remove_recipe('Sandwich Special')
    for el in shoppingList._items:
        assert el[1] != 'Sandwich Special'
    copy_list = shoppingList._items.copy()
    shoppingList.remove_recipe('Sandwich')
    assert copy_list == shoppingList._items

def test_get_list():
    ingredient1 = Ingredient('Bread',400.0,'г')
    ingredient3 = Ingredient('Cucumber',300.0,'г')
    recipe1 = Recipe('Sandwich Special',[ingredient1,ingredient3])
    ingredient2 = Ingredient('Bread',300.0,'г')
    recipe2 = Recipe('Sandwich Basic',[ingredient2])
    shoppingList = ShoppingList()
    shoppingList.add_recipe(recipe1,1)
    shoppingList.add_recipe(recipe2,1)
    new_list = shoppingList.get_list()
    assert new_list[0].quantity == 700.0
    assert new_list[0].name == 'Bread'
    assert new_list[1].name == 'Cucumber'

def test_add():
    ingredient3 = Ingredient('Cucumber',300.0,'г')
    recipe1 = Recipe('Sandwich Special',[ingredient3])
    ingredient2 = Ingredient('Bread',300.0,'г')
    recipe2 = Recipe('Sandwich',[ingredient2])
    shoppingList1 = ShoppingList()
    shoppingList2 = ShoppingList()
    shoppingList1.add_recipe(recipe1,1)
    shoppingList2.add_recipe(recipe2,1)
    copy_list1 = shoppingList1._items.copy()
    copy_list2 = shoppingList2._items.copy()
    new_shopping_list = shoppingList1.__add__(shoppingList2)
    assert new_shopping_list._items == shoppingList1._items+shoppingList2._items
    assert copy_list1 == shoppingList1._items
    assert copy_list2 == shoppingList2._items







    
    


    
