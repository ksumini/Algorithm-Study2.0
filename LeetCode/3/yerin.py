# 시간복잡도 : O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # 각 문자의 마지막 인덱스를 저장하는 딕셔너리
        max_len = 0
        start = 0  # 시작 인덱스 저장하는 변수

        for i, w in enumerate(s):
            # 현재 문자가 이미 char_map에 있고, 해당 문자의 마지막 인덱스가 시작 인덱스보다 크거나 같은 경우
            if w in char_index_map and char_index_map[w] >= start:
                # 중복된 문자가 나타났으므로, start를 중복된 문자의 다음 인덱스로 이동
                start = char_index_map[w] + 1
            
            # 현재 문자의 인덱스를 char_map에 업데이트
            char_index_map[w] = i
            max_len = max(max_len, i - start + 1)

        return max_len

# 시간복잡도 : O(n**2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ''
        max_len = 0
        for w in s:
            if w in temp_str:
                max_len = max(max_len, len(temp_str))
                # 현재 문자가 임시 문자열 안에도 존재할 때
                # 해당 문자까지의 문자열 절삭 후 현재 문자 추가
                idx = temp_str.index(w)
                temp_str = temp_str[idx+1:] + w
            else:
                temp_str += w
        else:
            max_len = max(max_len, len(temp_str))


        return max_len