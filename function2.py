def greet(name="guest"):
    print("hello ",name,"!")


greet()
greet("ashutosh mali")


def introduce(name,age):
    print("Name :",name)
    print("Age :",age)


introduce(name="ashutosh",age=27)



def add(a:int,b:int)->int:
    return a+b

result=add(10,20)
result=result*2

print("addition of two number is ",result)


def calculate_squre(number:int)->int:
    result= number*number
    return result

answer=calculate_squre(10)
print("squre of number is ",answer)