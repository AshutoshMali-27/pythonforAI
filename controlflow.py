score =72

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")


if 0<=score<=100:
    print("Valid score")


status="adult" if score>=18 else "minor"

for x in [10,20,30]:
    print(x)

for ch in "python":
    print(ch)

for i in range(5):
    print(i)

for i in range(2,6):
    print(i)


for i in range(0,10,2):
    print(i)


names=["Asha", "Ravi", "Meena"]
ages=[25,20,30,35]


for i,names in enumerate(names):
    print(i,names)

for name,age in zip(names,ages):
    print(name,ages)


for n in [1,3,5]:
    if n%2==0:
        print("even")
    else:
        print("odd")

command="stop"


match command:
    case "start":
        print("starting")
    case "stop" |"quit":
        print("stopping")
    case _:
        print("unknow")



for i in range(1,21):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)



total=0

for i in range(1,101):
    if i%2==0:
        total=total+i

print(total)


def handle(cmd):
    match cmd:
        case "start":
            return "go"
        case "stop" | "quit":
            return "halt"
        case _:
            return "?"


print(handle("start"))  # go
print(handle("stop"))   # halt
print(handle("quit"))   # halt
print(handle("hello"))  # ?


fruits = ["apple", "mango", "kiwi"]

for i,fruit in enumerate(fruits,start=1):
     print(f"{i}. {fruit}")