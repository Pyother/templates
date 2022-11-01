from .models import System

class Calculator:

    array_elements = []

    def __init__(self, array_elements):

        self.array_elements = array_elements
        self.system = System.objects.all().values()
        print(self.system)

    def __str__(self):
        print(f"VALUES: {self.array_elements}")

    