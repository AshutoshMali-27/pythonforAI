matrix=[[1,2,3],
       [4,5,6],
       [7,8,9]]


for i in range(len(matrix)):
    row_sum=0;
    for j in range(len(matrix[0])):
        row_sum=row_sum+matrix[i][j];
    print(f"row sum for {i+1} row {row_sum}");
