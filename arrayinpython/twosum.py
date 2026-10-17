numbers = [10, 45,55, 23, 89, 12];
target=55;

found=False;
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j] == target:
            print("the two number are ",numbers[i]," and ",numbers[j]);
            found=True;

if not found:
    print("no two number found");