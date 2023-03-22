
from learnpython.design_pattern.creational import AbstractFactory

# creational - AbstractFactory

ConcreteFactoryX = AbstractFactory.ConcreteFactoryX
ConcreteFactoryY = AbstractFactory.ConcreteFactoryY





if __name__ == '__main__':
   factoryX = ConcreteFactoryX()
   factoryY = ConcreteFactoryY()
  
   p1 = factoryX.createProductA()
   print("Product: " + p1.getName())
  
   p2 = factoryY.createProductA()
   print("Product: " + p2.getName())
  
   