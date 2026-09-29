class Animal:
    def speak(self):
        print("Animal is speaking");

class Dog(Animal):
    def speak(self):
        print("Dog is barking");


dog1=Dog();
dog1.speak();