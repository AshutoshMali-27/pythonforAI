class animal:
    def speak(self):
        print("animal is speaking");

class dog(animal):
    def bark(self):
        print("dog is barking");


dog1=dog();
dog1.speak();
dog1.bark();