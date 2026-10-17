x=5
x="hello"
name,age="ashutosh",25

print(name,age)

print(type(x))
print(type(5))
print(type(5.0))
print(type("hello"))

a=7
b=2
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# string in python 
s="hello"
t="also fine"
name="ashutosh"

print(f"hello {name} ,2+2={2+2}")

text="""line one 
line two"""

print(text)

print(s[0],s[-1],s[1:4])
print(s.upper(),s.lower(),s.replace("h","H"),s.split("e"))


status=None
if(age>=18):
    status="adult"
else:
    status="minor"

print(f"{name} is {age} years old and is a {status}")