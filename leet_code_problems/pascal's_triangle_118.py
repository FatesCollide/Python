class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        answer = []
        
        for i in range(numRows):
            row = []
            
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    value = answer[-1][j - 1] + answer[-1][j]
                    row.append(value)
                    
            answer.append(row)
            
        return answer
