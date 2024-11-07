class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 키패드 매핑
        pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                          '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # 문자 조합 생성 함수
        def combine(curr, remain):
            if not remain:
                return curr
            if not curr:
                return combine([char for char in pad[remain[0]]], remain[1:])
            return combine([comb + char for comb in curr for char in pad[remain[0]]], remain[1:])
        
        return combine([], digits)