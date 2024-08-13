from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        answer = 0
        alp_cnt = Counter(word)
        for idx, cnt in enumerate(sorted(alp_cnt.values(), reverse=True)):
            answer += cnt * ((idx)//8 + 1)
        return answer