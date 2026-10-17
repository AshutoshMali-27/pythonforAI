numbers = [10, 45, 23, 89, 12];
smallest=float('+inf');
secondsmallest=float('+inf');

for num in numbers:
    if(num<smallest):
        secondsmallest=smallest;
        smallest=num;
    elif(num<secondsmallest and num!=smallest):
        secondsmallest=num;


print("the second smallest number in array is ",secondsmallest);