from collections import Counter
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        c = Counter(nums)

        # 3개 같은 값
        if c[0] >= 3:
            answer.append([0, 0, 0])

        c2 = [k for k, v in c.items() if v >= 2 and k != 0]

        # 3개 다른 값
        for i, j in combinations(sorted(c.keys()), 2):
            if c[-i-j] and j <-i-j:
                answer.append([i, j, -i-j])

        # 2개 같은 값
        for cc in c2:
            if c[-2*cc]:
                answer.append([cc, cc, -2*cc])
        
        return answer