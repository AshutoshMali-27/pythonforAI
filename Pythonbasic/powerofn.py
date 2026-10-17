num=int(input("enter the number:"));
exponent=5;
result=1;
for i in range(1,exponent+1):
    result=result*num;

print(f"the power of number {num} is {result}");