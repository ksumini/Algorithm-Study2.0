"""
<문제>
정렬되지 않은 정수 배열 nums에서 가장 긴 연속하는 원소 배열의 길이를 반환하라.
알고리즘은 O(n)으로 동작해야 한다.

<제한 사항>
0 <= nums.length <= 105
-109 <= nums[i] <= 109

<풀이 시간>
30분

<풀이>
파이썬의 정렬 알고리즘인 팀소트는 O(nlogn)이기 때문에 정렬없이 문제를 풀이해야 한다.

0. nums의 길이가 0일 수도 있기 때문에 원소가 없을 때는 0을 return
1. 중복된 원소 제거 및 빠른 원소 탐색(O(1))을 위해 set 자료형을 사용한다.
2. num_set의 각 원소를 탐색하며 시작점이 되는 원소인 경우에만 연속한 숫자들을 찾는다. (num-1이 num_set에 없는 경우가 시작점이 되는 경우)
3. 각 시작점일 때의 최대 길이를 업데이트한다.

<시간복잡도>
O(n): 각 숫자들을 무조건 한 번씩만 탐색하기 때문에, 최악의 경우 O(n)
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # 현재 숫자가 배열의 시작점인 경우만 처리
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                # 연속된 숫자가 더 이상 존재하지 않을때까지 찾기
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(current_length, max_length)

        return max_length