class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        totals = []
        for i in range(len(mat)):
            total = 0
            for j in range(len(mat[i])):
                total += mat[i][j]
            totals.append(total)
        max_index = totals.index(max(totals))
        return [max_index, max(totals)]
