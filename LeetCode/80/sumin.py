"""
<문제>
오름차순 정렬된 정수 배열 정수 배열 nums가 주어졌을 때, 각 숫자가 최대 2번만 등장하도록 배열을 in-place 방식으로 변경해야 한다.
순서를 유지하면서, 추가적인 배열을 사용하지 않고 주어진 배열 자체(in-place)에서 수정해야 한다.
배열의 크기를 변경할 수 없기 때문에 결과적으로 남는 값들은 배열의 앞부분에 저장하고, 나머지 부분은 주요하지 않으니 무시해도 된다.

<제한 사항>
1 <= nums.length <= 3 * 10**4
-10**4 <= nums[i] <= 10**4
nums는 오름차순 정렬

<풀이>
풀이 시간: 35분
1. start는 배열의 앞부분을 덮어쓰는 역할, end는 배열을 탐색하는 역할을 한다.
2. end가 배열을 탐색하면서 중복된 값이 2개 이하일 때만 start에 해당 값을 덮어 쓴다.
3. cnt는 중복 횟수를 세며, 새로운 값이 나오면 초기화 한다.

<시간 복잡도>
O(n)
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        start = 1 # 배열을 덮어쓸 위치
        cnt = 1 # 중복 횟수를 세기 위한 변수
        for end in range(1, len(nums)):
            if nums[end] == nums[end-1]: # 이전 값과 같으면 중복 횟수 증가
                cnt += 1
            else: # 다른 값이 나오면 중복 횟수 초기화
                cnt = 1
            if cnt <= 2: # 중복이 2개 이하일 때 값을 덮어씀
                nums[start] = nums[end]
                start += 1
        return start