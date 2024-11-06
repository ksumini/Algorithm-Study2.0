"""
<문제>
전형적인 백트래킹 문제

<풀이>
풀이 시간: 10분
백트래킹으로 풀이

<시간 복잡도>
약 O(4**n)
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []
        if not digits:
            return result

        # Backtrack
        def backtrack(index, string):
            # Base Condition
            if index == len(digits):
                result.append(string)
                return

            for char in letters[digits[index]]:
                backtrack(index + 1, string + char)

        backtrack(0, "")

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations(''))
    print(s.letterCombinations('2'))