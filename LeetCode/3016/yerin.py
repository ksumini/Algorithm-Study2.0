'''
소문자 str
'''
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        numpads = defaultdict(int)
        numbers = [2, 3, 4, 5, 6, 7, 8, 9]
        i = 0
        answer = 0

        # 문자 카운트
        counter_alphabet = Counter(word)
        # 개수가 많은 순으로 숫자 패드에 매핑
        counter_alphabet_sort = sorted(counter_alphabet.items(), key=lambda x: x[1], reverse= True)

        for alph, cnt in counter_alphabet_sort:
            numpads[numbers[i]] += 1
            answer += cnt * numpads[numbers[i]]
            i = (i + 1) % len(numbers)

        return answer

