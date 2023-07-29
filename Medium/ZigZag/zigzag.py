class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [''] * numRows
        row = 0
        going_down = False

        for c in s:
            rows[row] += c

            if row == 0 or row == numRows - 1:
                going_down = not going_down

            row += 1 if going_down else -1

        return ''.join(rows)


solution = Solution()
print(solution.convert('PAYPALISHIRING', 3))
print(solution.convert('PAYPALISHIRING', 4))
print(solution.convert('A', 1))
