class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 3 -> 3 + 1 개씩 반복
        # 4 -> 4 + 2 개씩 반복
        # 5 -> 5 + 3 개씩 반복
        
        repeat = numRows + max(0, (numRows - 2))
        sub_str = []

        for start in range(0, len(s), repeat):
            # sub_str[i]: i + 1번째 패턴에 해당하는 단어            
            end = start + repeat
            if end > len(s):
                end = len(s)
            sub_str.append(s[start:end])

        answer = ''
        first_row = ''
        last_row = ''

        for cur_str in sub_str:
            # sub_str의 0번 째 index를 first_row에 저장
            # sub_str의 numRows - 1 번째 index가 존재하면 last_row에 저장
            first_row += cur_str[0]
            last_idx = numRows - 1
            if 0 < last_idx < len(cur_str):
                last_row += cur_str[last_idx]

      # 첫 번째 row를 answer에 더해줌.
        answer += first_row

        idx = 1
        while idx < numRows - 1:
            # 각 패턴에 맞춰 answer에 문자열을 더해 줌.
            for cur_str in sub_str:
                if idx < len(cur_str):
                    answer += cur_str[idx]
                if repeat - idx < len(cur_str):
                    answer += cur_str[repeat-idx]
            idx += 1
        
        answer += last_row

        return answer
