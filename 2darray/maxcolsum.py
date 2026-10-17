matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

maxsum=0;
for i in range(len(matrix[0])):
    col_sum=0
    for j in range(len(matrix)):
        col_sum=col_sum+matrix[j][i];
    print(f"colsum of {i+1} are {col_sum} ");
    if(col_sum>maxsum):
        maxsum=col_sum;
print(maxsum);

