numbers = [10, 45, 23, 89, 12];
largest=float('-inf');
secondlargest=float('-inf');

for num in numbers:
    if(num>largest):
        secondlargest=largest;
        largest=num;
    elif(num>secondlargest and num!=largest):
        secondlargest=num;


print("the second largest number in array is ",secondlargest);