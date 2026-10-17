num=int(input("enter the number-:"));
sum=0;
count=0;
while(num>0):
    digit=num%10;
    count=count+1;
    sum=sum+digit;
    num=num//10;


print("the sum of digit is ",sum);
print("the count of digit is ",count);