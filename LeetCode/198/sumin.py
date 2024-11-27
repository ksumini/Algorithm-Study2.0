"""
<문제>
전형적인 DP 문제

<풀이>
풀이 시간: 10분
1. 테이블 정의하기
- dp[i]: i번째 집을 방문했을 때 훔칠 수 있는 최대 돈의 양
2. 점화식 찾기
- dp[i] = max(dp[i-1], dp[i-2] + nums[i])
3. 초기값 정하기
- dp[0] = nums[0]
- dp[1] = max(nums[0], nums[1])

굳이 dp 배열을 만들지 않고 이전 두 집의 값만 가지고 갱신하면, 공간복잡도를 줄일 수 있을 것 같아
변수 두 개로 해결했다.

<시간 복잡도>
O(n)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0 # 이전 두 집의 최적값
        for num in nums:
            current = max(prev1, prev2 + num) # 현재 집을 털거나 안 털거나 중 최대값 선택
            prev2, prev1 = prev1, current

        return prev1