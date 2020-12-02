class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in reversed(range(len(triangle[:-1]))):
            row_cur = triangle[row]
            row_next = triangle[row+1]
            for i in range(len(row_cur)):
                row_cur[i] += min(row_next[i],row_next[i+1])
        return triangle[0][0]
