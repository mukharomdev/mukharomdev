from learnpython.design_pattern.creational import AbstractFactory


ConcreteFactoryX = AbstractFactory.ConcreteFactoryX
ConcreteFactoryY = AbstractFactory.ConcreteFactoryY




if __name__ == "__main__":
   print("Creational-AbstractFactory")
   print()
   factoryX = ConcreteFactoryX()
   factoryY = ConcreteFactoryY()
  
   p1 = factoryX.createProductA()
   print("Product: " + p1.getName())
  
   p2 = factoryY.createProductA()
   print("Product: " + p2.getName())
   print()
   
