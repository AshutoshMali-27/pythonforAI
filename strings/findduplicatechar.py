text="programming";
for i in range(0,len(text)):
    count=1;
    for j in range(i+1,len(text)):
        if text[i]== text[j]:
            count=count+1;
    
    if count>1:
        print(text[i]," ",end="");