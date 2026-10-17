arr = [10,20,30,40,50];
target=30;
index=-1;

for i in range(0,len(arr)):
    if arr[i] == target:
        index=i;
        break;


if index==-1:
    print("the target number is not found in array");
else:
    print("the target number is found at index ",index);
