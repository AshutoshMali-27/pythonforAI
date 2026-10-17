numbers = [10, 45, 23, 89, 12];
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]<numbers[j]):
            temp=numbers[i];
            numbers[i]=numbers[j];
            numbers[j]=temp;

for num in numbers:
    print(num," ",end="");