class user:

    country="india";

    def __init__(self,name,age):
        self.name=name;
        self.age=age;   

user1=user("ashutosh",27);
user2=user("ashu",20);

print(user1.country);
print(user2.country);