class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        string_by_rows = [''] * numRows
        idx = 0
        step = 1

        for w in s:
            string_by_rows[idx] += w

            # 첫 번째 행이나 마지막 행에 도달하면 방향을 변경
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1

            idx += step

        return ''.join(string_by_rows)


if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))
