number=int(input("enter the number-:"));
reverse=0;

while(number>0):
    digit=number%10;
    reverse=reverse*10+digit;
    number=number//10;

print("the reverse of the number is-:",reverse);