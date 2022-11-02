from .models import System
import datetime

class Calculator:

    array_elements = []

    def __init__(self, array_elements):

        self.array_elements = array_elements
        self.system = list(System.objects.all().values())
        
        date1 = datetime.datetime.strptime(self.array_elements[6], '%d/%m/%Y')
        date2 = datetime.datetime.strptime(self.system[0]["border_date"], '%d/%m/%Y')
        print(date1 == date2)
        
    def __str__(self):
        print(f"VALUES: {self.array_elements}")

    