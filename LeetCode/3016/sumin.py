from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = sorted(Counter(word).values(), reverse=True)
        answer = 0
        push_cnt = 1

        for idx, cnt in enumerate(counts):
            if idx > 0 and idx % 8 == 0:
                push_cnt += 1
            answer += push_cnt * cnt
        return answer