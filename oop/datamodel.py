numbers=[1,2,3]

print(len(numbers))


class User:
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return f"User : {self.name}"


user1=User("ashutosh");
print(user1);