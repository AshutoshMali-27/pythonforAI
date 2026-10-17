numbers = [10, 45, 23, 89, 12];
destination=[0]* len(numbers);
for i in range(len(numbers)):
    destination[i]=numbers[i];

print("array copied");

for num in destination:
    print(num," ",end="");