matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

diagonal_sum=0;

for i in range(len(matrix)):
    diagonal_sum=diagonal_sum+matrix[i][i];


print(diagonal_sum);
