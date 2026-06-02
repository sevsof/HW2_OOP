from classes import Ingredient

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

