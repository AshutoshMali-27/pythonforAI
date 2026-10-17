from collections import Counter


# text="banana";
# count={};

# for ch in text:
#     count[ch]=count.get(ch,0)+1;


# print(count);
## above program are without using counter
## with using counter

txt="banana";
count=Counter(txt);
print(count);


numbers=[1, 2, 2, 3, 3, 3];
count1=Counter(numbers);
print(count1);
print(count1.most_common(3));