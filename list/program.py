x = [2,4,6,8,10]
a = [14, 13, 12, 'eleven', 10, 8, 6, 4, 2, 'one']


# Perform one single operation to remove 'eleven', 10, 8 all together at once
# del a[3:6]
# print(a);

# ## write the code to add eleven in the list at the end'
# x.append("eleven");

# print(x);

# ## write the code to insert 12 at position 0 of list

# x.insert(0,12);
# print(x);

# ## print to merge list y in x
# y=[1,3,5,7,9];
# x=x+y;
# print(x);

# ## remove element
# x.remove("eleven");
# print(x);

# ## pop element from the list
# x.pop(0);
# print(x);
# ## reverse element from the list
# x.reverse()
# print(x)
# ## sort element from the list
# x.sort()
# print(x)
# ## copy element from the list
# z=x.copy();
# print(z);

# ## append list inside list
# x.append(y);
# print(x);
# ## extend and + list
# a=[1,2,3,4,5];
# b=[6,7,8,9,10];
# a.extend(b);
# print(a);
# result=a+b;
# print(result);

# write a code to get the following output
# x = ["hey","there","hello","world"]
# y=" ";
# result=y.join(x);
# print(result);

## index
numbers = [10, 20, 30, 40]

position = numbers.index(30)

print(position)

## clear
numbers.clear()
print(numbers)

## del 

s = [10, 20, 30, 40]
del s
print(s)  # This will raise an error since 'numbers' is deleted