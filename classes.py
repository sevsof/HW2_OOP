class Ingredient:
    def __init__(self,name,quantity,unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self,value):
        if value<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    def __eq__(self, other):
        if not isinstance(other,Ingredient):
            return NotImplemented
        return self.name == other.name and self.unit == other.unit

class Recipe:
    def __init__(self,title,ingredients=None):
        self.title = title
        if ingredients:
            self.ingredients = ingredients
        else:
            self.ingredients = []

    def add_ingredient(self,ingredient: Ingredient):
        if ingredient in self.ingredients:
            for element in self.ingredients:
                if element == ingredient:
                    element.quantity+=ingredient.quantity
                    break
        else:
            self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio,(int,float)) and ratio>0:
            return True
        else:
            return False
        
    def scale(self,ratio:float):
        if Recipe.is_valid_ratio(ratio):
            newRecipe = Recipe(self.title,[])
            for element in self.ingredients:
                newElement = Ingredient(element.name,element.quantity*ratio,element.unit)
                newRecipe.add_ingredient(newElement)
            return newRecipe
        else:
            raise ValueError()
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        result = "\n".join(str(el) for el in self.ingredients)
        return f"Title: {self.title}\nIngredients: {result}"


class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self,recipe,portions):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        for ingredient in recipe.scale(portions).ingredients:
            self._items.append((ingredient,recipe.title))
    def remove_recipe(self,title):
        self._items = [recipe for recipe in self._items if recipe[1] != title]
        
    def get_list(self):
        dict_of_ingredient = {}
        for element in self._items:
            ingredient = element[0]
            key = (ingredient.name,ingredient.unit)
            if key in dict_of_ingredient:
                dict_of_ingredient[key]+=ingredient.quantity
            else:
                dict_of_ingredient[key] = ingredient.quantity
        list_of_ingredient = []
        for name_unit, quantity in dict_of_ingredient.items():
            list_of_ingredient.append(Ingredient(name_unit[0],quantity,name_unit[1]))
        return sorted(list_of_ingredient, key = lambda x: x.name)
    def __add__(self,other):
        new_shoppingList = ShoppingList()
        new_shoppingList._items=self._items+other._items
        return new_shoppingList
    

class DietaryRecipe(Recipe):
    def __init__(self,title,diet_type,ingredients=None):
        super().__init__(title,ingredients)
        self.diet_type = diet_type
    def scale(self,ratio):
        recipe = super().scale(ratio)
        new_dietaryRecipe = DietaryRecipe(recipe.title,self.diet_type, recipe.ingredients) 
        return new_dietaryRecipe
    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"



        


            



        
    
    

        
