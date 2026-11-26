class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)): 
            total = 0
            temp=[]
            for j in range(len(matrix[i])): 
                total+=matrix[i][j]
                temp.append(total)  
            matrix.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0 
        while row1 <= row2:
            for col in range(col1,col2+1): 
                total+=self.matrix[row1][col] 
            row1+=1
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)