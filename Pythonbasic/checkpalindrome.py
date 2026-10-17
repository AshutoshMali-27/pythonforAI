number=int(input("enter the number-:"));
reverse=0;
num=number;
while(number>0):
    digit=number%10;
    reverse=reverse*10+digit;
    number=number//10;


if(reverse==num):
    print(num,"is palindrome number");
else:
    print(num,"is not palindrome number");