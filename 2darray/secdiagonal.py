matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

n=len(matrix);
diagonal_sum=0
for i in range(n):
    diagonal_sum=diagonal_sum+matrix[i][n-1-i];

print(diagonal_sum);