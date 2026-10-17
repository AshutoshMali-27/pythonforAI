numbers = [10, 45, 23, 89, 12];
smallest=numbers[0];

for num in numbers:
    if(num<smallest):
        smallest=num;

print("the smallest number in array is ",smallest);