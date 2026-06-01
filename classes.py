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
    def __init__(self,title,ingredients):
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

        
    
    

        
