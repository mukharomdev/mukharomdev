from learnpython.design_pattern.creational import Builder

ConcreteBuilderX = Builder.ConcreteBuilderX
ConcreteBuilderY = Builder.ConcreteBuilderY

Director = Builder.Director






if __name__ == "__main__":
  print("creational - Builder")
  print("")
  
  builderX = ConcreteBuilderX()
  builderY = ConcreteBuilderY()  
  
  director = Director()
  director.set(builderX)  
  director.construct()
  
  product1 = director.get()
  print("1st product parts: " + product1.get())
  
  director.set(builderY)  
  director.construct()
  
  product2 = director.get()
  print("2nd product parts: " + product2.get())
  