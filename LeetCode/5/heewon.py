from collections import defaultdict
from itertools import combinations

class Solution:
    def checkPalindrome(self, substring: str) -> str:
        return substring if substring == substring[::-1] else ''

    def longestPalindrome(self, s: str) -> str:
        if self.checkPalindrome(s):
            return s

        answer = s[0]   # 초기 값
        char_indices = defaultdict(list)    # 문자별 index 정보 저장, 문자: [index1, index2, index3]

        for idx, letter in enumerate(s):
            char_indices[letter].append(idx)

        for char_indices_list in char_indices.values(): # 문자별로 확인
            for i, j in sorted(combinations(char_indices_list, 2), key=lambda x: x[0]-x[1]):  # index차이가 큰 경우부터 확인
                if palindrome := self.checkPalindrome(s[i:j+1]):    # palindrome 확인
                    answer = max(palindrome, answer, key=len)   # 최대 길이 갱신
                    break   # 나머지 경우는 최대 불가

        return answer