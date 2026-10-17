numbers = [10, 45, 23, 89, 12];
evencount=0;
oddcount=0;

for num in numbers:
    if(num%2==0):
        evencount+=1;
    else:
        oddcount+=1;

print(f"the count of even number in array is {evencount}");
print(f"the count of odd number in array is {oddcount}");
