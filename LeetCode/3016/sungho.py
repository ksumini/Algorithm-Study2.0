from collections import defaultdict


class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # key - 8 numbers (2~9)
        # one letter to one key

        NUM_DICT = defaultdict(lambda: 0)
        n = len(word)

        for i in range(n):
            NUM_DICT[word[i]] += 1

        if len(NUM_DICT) <= 8:  # 가짓수가 8개 이하면 2 ~ 9까지 수 8개 중에 아무거나 배치하고 1씩 늘리면 됨
            return len(word)  # 답은 문자 길이

        NUM_DICT = sorted(NUM_DICT.items(), key=lambda x: (x[1]),
                          reverse=True)  # 1*8 2*... 식으로 갯수 많은거부터 1씩 채워서 1 2 3 4 최대 8개로 하면됨
        answer = 0
        for i in range(len(NUM_DICT)):
            answer += NUM_DICT[i][1] * (i // 8 + 1)
        return answer