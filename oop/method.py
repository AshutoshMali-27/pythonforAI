class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def greet(self):
        print("hello ",self.name," !","you are ",self.age," years old");




user1=User("ashutosh",27);
user1.greet();