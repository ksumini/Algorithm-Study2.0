class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        # 각 행에 해당하는 리스트 생성
        rows = [''] * numRows
        cur_row = 0
        back = False # 올라가고 내려가는걸 판단하는 변수

        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                back = not back
            cur_row += 1 if back else -1
        return ''.join(rows)