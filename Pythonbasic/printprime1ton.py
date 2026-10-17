num=int(input("enter the number:"));
for i in range(2,num+1):
    isprime=True;
    for j in range(2,i):
        if(i%j==0):
            isprime=False;
            break;
    if(isprime):
        print(i," ",end=""); 

