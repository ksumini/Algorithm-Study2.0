'''
문제 설명
1. 양의 정수가 담긴 array nums, 양의 정수인 target이 주어짐.
2. 합이 target 이상이 되는 최소 길이를 리턴해라.
3. 그런 subarray가 없다면 0을 return


조건
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4

O(n)을 찾았다면 O(nlogn)의 답변도 찾아봐라... ㅎㄷㄷ

0부터 n-1까지 정수짝 선정? -> nC2 = n(n-1)/2 -> O(n^2)??
0부터 n-1까지 정수 2번 선정?
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = 100001
        n = len(nums)
        if sum(nums) < target:  # 애초에 전체 합이 target보다 작으면 return 0
            return 0

        left, right = 0, 0
        sum_subarray = 0


        # 처음에 작성한 답안인데, 이게 왜 안되는지 아직도 이해가 안갑니다. left = 3, right = 5, subarray = [2, 4]일때 다음 루프로 진행되지 않고 종료되는게 이해가 안가네요.
        # while right < n:
        #     # 먼저 right를 확장해 나가면서 부분 배열의 합을 계산
        #     if sum_subarray < target:
        #         sum_subarray += nums[right]
        #         right += 1
        #         print(left, right, nums[left:right], sum_subarray, target)
        #     else:
        #         answer = min(answer, right - left)
        #         sum_subarray -= nums[left]
        #         left += 1
        #         print(n, left, right, nums[left:right], sum_subarray, target)


        # 2개의 while문을 사용하니 해결 됐습니다.
        while right < n:
            # 먼저 right를 확장해 나가면서 부분 배열의 합을 계산
            sum_subarray += nums[right]
            right += 1

            # sum_subarray가 target 이상이면 최소 길이를 계산
            while sum_subarray >= target:
                answer = min(answer, right - left)
                sum_subarray -= nums[left]
                left += 1

        return answer
