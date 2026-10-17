matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

minsum=float('inf')
for i in range(len(matrix)):
    rowsum=0;
    for j in range(len(matrix[0])):
        rowsum=rowsum+matrix[i][j];
    print(f"{rowsum}")
    if(rowsum<minsum):
        minsum=rowsum;

print(minsum)

