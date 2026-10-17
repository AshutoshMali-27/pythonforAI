num=int(input("enter the number:"));
sqrt=0;
for i in range(1,num+1):
    if(i*i==num):
        sqrt=i;
        break;


if(sqrt==0):
    print(num,"does not have perfect square root");
else:
    print("the square root of number",num,"is",sqrt);