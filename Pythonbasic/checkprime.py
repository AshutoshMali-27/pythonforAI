
def isprime(num):
    if(num<=1):
        return False;
    for i in range(2,num):
        if(num%i==0):
            return False;
    return True;


num =int(input("enter the number:"));
checkprime= isprime(num);
if checkprime:
    print(num,"is prime number");
else:
    print(num,"is not prime number");




