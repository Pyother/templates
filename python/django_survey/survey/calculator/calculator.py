from .models import System

class Calculator:

    array_elements = []

    def __init__(self, array_elements):

        self.array_elements = array_elements
        self.system = list(System.objects.all().values())
        
        for i in range (len(self.system)):
            print("Employer: ", self.system[i]["employer"])
            print("Element: ", self.array_elements[i])
            print(self.system[i]["employer"]==self.array_elements[i])
        
    def __str__(self):
        print(f"VALUES: {self.array_elements}")

    