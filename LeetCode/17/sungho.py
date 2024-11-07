class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num2alphabet = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        }

        if digits == "":
            return []
        if len(digits) == 1:
            return num2alphabet[digits[0]]

        outputs = []
        def multiply_list(l1, l2):
            result = []
            for e1 in l1:
                for e2 in l2:
                    result.append(e1+e2)
            return result

        result = multiply_list(num2alphabet[digits[0]], num2alphabet[digits[1]])
        if len(digits) == 2:
            return result

        result = multiply_list(result, num2alphabet[digits[2]])
        if len(digits) == 3:
            return result
        
        result = multiply_list(result, num2alphabet[digits[3]])
        return result
        

