class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):  # 세 개의 수를 확인하는 거니, 배열 길이에서 2를 뺀 값만큼 반복
            # 중복 처리
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:  # 총합이 0일 때, 삽입.
                    ans.append([nums[i], nums[left], nums[right]])
                    # 중복 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:  # 합이 0보다 작을 때 -> 더하는 값을 크게 만들어야 함
                    left += 1
                else:  # 합이 0보다 클 때 -> 더하는 값을 작게 만들어야 함
                    right -= 1

        return ans
