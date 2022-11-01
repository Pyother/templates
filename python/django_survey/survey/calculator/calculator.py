from .models import System

class Calculator:

    array_elements = []

    def __init__(self, array_elements):

        self.array_elements = array_elements
        self.system = list(System.objects.all().values())
        
        for i in range (len(self.system)):
            print("Border date: ", self.system[i]["border_date"])
            print("Element: ", self.array_elements[6])
            print(self.system[i]["border_date"]==self.array_elements[6])
        
    def __str__(self):
        print(f"VALUES: {self.array_elements}")

    