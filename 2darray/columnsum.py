matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]
        ];

for i in range(len(matrix[0])):
    col_sum=0;
    for j in range(len(matrix)):
        col_sum=col_sum+matrix[j][i];
    print(f"the sum of column {i+1} is {col_sum}");