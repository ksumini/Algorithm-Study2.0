'''
오름차순 정렬 정수 배열: nums
return k. k 인덱스 뒤 요소들은 신경 안 씀.

in-place 알고리즘: 별도의 배열 사본 생성 x, 상수 변수만 허용 -> 공간복잡도 O(1)
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,1,2,2,3]))

