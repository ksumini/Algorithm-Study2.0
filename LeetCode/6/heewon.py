class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        row_str = [''] * (numRows) # 각각의 row에 들어가는 문자 저장

        for i, chr in enumerate(s):
            idx = i % (2*numRows - 2)   # 2 * (numRows - 1) 의 주기를 가짐
            if idx >= numRows:          # row_str의 크기는 numRows 이므로 이보다 큰 값은 각각의 Row에 맞게 추가 계산
                row_str[2*numRows - 2 - idx] += chr
            else:
                row_str[idx] += chr

        return ''.join(row_str) # join으로 1개의 문자열 출력