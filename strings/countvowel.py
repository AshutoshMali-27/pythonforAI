text=input("enter the string-:");
vowel=0;
consonant=0;

for ch in text.lower():
    if ch.isalpha():
        if ch in 'aeiou':
            vowel+=1;
        else:
            consonant+=1;

print("the number of vowel in string is-:",vowel);
print("the number of consonant in string is-:",consonant);