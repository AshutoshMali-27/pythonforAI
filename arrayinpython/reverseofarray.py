numbers = [10, 45, 23, 89, 12];
left=0;
right=len(numbers)-1;
while(left<right):
    temp=numbers[left];
    numbers[left]=numbers[right];
    numbers[right]=temp;
    left=left+1;
    right=right-1;


for num in numbers:
    print(num," ",end="");