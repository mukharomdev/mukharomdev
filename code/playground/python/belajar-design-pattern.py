
from learnpython.design_pattern.creational import AbstractFactory 
from AbstractFactory import ConcreteFactoryX,ConcreteFactoryY





if __name__ == '__main__':
   factoryX = ConcreteFactoryX()
   factoryY = ConcreteFactoryY()
  
   p1 = factoryX.createProductA()
   print("Product: " + p1.getName())
  
   p2 = factoryY.createProductA()
   print("Product: " + p2.getName())
  
  