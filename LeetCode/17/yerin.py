'''
2-9 숫자 포함된 문자열
반환 : 모든 가능한 문자 조합. 순서 상관 x

'''


from typing import List


class Solution:
    def __init__(self):
        self.answer = []
        self.map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        # answer = []
        self.add_letter_to_string('', 0, digits)
        return self.answer if self.answer else []

    def add_letter_to_string(self, string: str, index: int, digits: str):
        if index < len(digits):
            for letter in self.map[digits[index]]:
                self.add_letter_to_string(string + letter, index + 1, digits)
        else:
            self.answer.append(string)


if __name__ == '__main__':
    print(Solution().letterCombinations(''))