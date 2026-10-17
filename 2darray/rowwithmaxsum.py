matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

maxsum=0;
for i in range(len(matrix)):
    row_sum=0;
    for j in range(len(matrix[0])):
        row_sum=row_sum+matrix[i][j];
    print(f"row sum for {i+1} are{row_sum}")
    if(maxsum<=row_sum):
        maxsum=row_sum;
print(maxsum);
    
    
    
