# version 1 - defaultdict, 30.25%, 79.5%
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        end = 1
        n = len(s)
        alp_cnt = defaultdict(int)
        alp_cnt[s[start]] += 1
        answer = end - start
        while end < n:
            if not alp_cnt[s[end]]:
                alp_cnt[s[end]] += 1
                end += 1
            else:
                alp_cnt[s[start]] -= 1
                start += 1
            answer = max(answer, end - start)
        return answer
    
# version 2 - str in, 41.94% / 38.04%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        end = 1
        n = len(s)
        answer = end - start
        while end < n:
            if s[end] not in s[start:end]:
                end += 1
            else:
                start += 1
            answer = max(answer, end - start)
        return answer
    
# fast code - 98.54% / 79.50%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:   return 0 # 빈 문자열 처리
        answer = 1
        left = 0    # 서브스트링의 왼쪽 index
        hashmap = {}    # chr : index(갱신)
        for right, ch in enumerate(s):  # O(len(s))
            if (idx:=hashmap.get(ch, -1)) >= left:  # hashmap에 저장된 문자이며 현재의 서브스트링에 중복되는지 확인
                answer = max(answer, right - left)  # 답 갱신
                left = idx + 1                      # 새로운 서브스트링 시작
            hashmap[ch] = right                     # hashmap 갱신
        answer = max(answer, len(s) - left)         # 마지막 서브스트링 확인
        return answer