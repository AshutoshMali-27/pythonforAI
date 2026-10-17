t = (2,1,4,6,2,1,4,1,2,7,1)

print(t)
print(t[::-1])

## tuple is immutable so we cannot change the value of tuple but we can convert it into list and then change the value of list and then again convert it into tuple

print(t.index(6))

## packing in tuple
x=("ashutosh",10,"mali")
print(x);
##Tuple Unpacking
name,age,designation=("ashutosh",27,"developer");
print(name);
print(age);
print(designation);

## single element tuple
number=(10);
print(type(number));  
## this result are  integer
number=(10,);
print(type(number));  
## now the result are tuple

## convert tuple into list
number=(10,20,30);
lst=list(number);
print(lst);

## convert list into tuple
sst = [10, 20, 30]
tup=tuple(sst);
print(tup);