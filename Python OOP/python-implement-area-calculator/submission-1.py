import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length : int, width : int|None = None):
        if width is None:
            return round(length * ((math.pi) ** 2),2)

        else:
            return  length * width

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
