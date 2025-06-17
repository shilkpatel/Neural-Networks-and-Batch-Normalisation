import typing

#Parent class

class activation_function():
    
    def calculate(self,x: float)->float:
        pass

    def derivative(self,x:float) ->float:
        pass

# child class

class relu(activation_function):
    
    def calculate(self,x:float)->float:
        if(x<0):
            return 0
        return x
    
    def derivative(self,x:float)-> float:
        return int(x>0)