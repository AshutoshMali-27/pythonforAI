num=12233445555;
count={};
while(num>0):
    digit=num%10;
    if digit in count:
        count[digit]+=1;
    else:
        count[digit]=1;
    num=num//10;

for num in count:
    print(f"the count  {num} of {count[num]} times");