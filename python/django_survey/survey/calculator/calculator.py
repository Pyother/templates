from .models import System
import datetime

class Calculator:

    array_elements = []

    def __init__(self, array_elements):

        self.array_elements = array_elements
        self.system = list(System.objects.all().values())
        self.candidate_system = self.calculate(self.array_elements, self.system)

        print(self.candidate_system)
        
    def __str__(self):
        print(f"VALUES: {self.array_elements}")

    def dates_comparison(self, str1, str2):

        return (datetime.datetime.strptime(str1, '%d/%m/%Y') <= 
            datetime.datetime.strptime(str2, '%d/%m/%Y'))

    def calculate(self, array_elements, system):

        candidate_system = []

        for i in range(len(system)):
            if ((array_elements[2] == system[i]["employer"]) and
                (array_elements[3] == system[i]["substract"]) and 
                (self.dates_comparison(array_elements[6], system[i]["border_date"]) == True )):
                
                values = {"substract": system[i]["substract"],
                          "value": system[i]["value"]*float(array_elements[5]),
                          "comment": system[i]["comment"]}
                candidate_system.append(values)
                
            else:
                print("Not matches")
            
        return candidate_system

    