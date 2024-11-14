from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dial = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        letters = []
        for digit in digits:
            letters.append(dial[digit])

        if letters:
            comb_letters = product(*letters)
            return ["".join(comb_letter) for comb_letter in comb_letters]
        return []
        
