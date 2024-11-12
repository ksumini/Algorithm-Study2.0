class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        max_len = 1
        answer = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                max_len += 1
            else:
                answer.append(max_len)
                max_len = 1
        answer.append(max_len)

        return max(answer)

    # def longestConsecutive2(self, nums: List[int]) -> int:
    #     visited = set()
    #     answer = []
    #     for num in nums:
    #         if num in visited:
    #             continue
    #
    #         temp = [num]
    #         visited.add(num)
    #         prv, nxt = num - 1, num + 1
    #
    #         # 1 더 작은 수 체크
    #         while prv in nums:
    #             visited.add(prv)
    #             temp.append(prv)
    #             prv = prv - 1
    #         # 1 더 큰 수 체크
    #         while nxt in nums:
    #             visited.add(nxt)
    #             temp.append(nxt)
    #             nxt = nxt + 1
    #
    #         if len(temp) > len(answer):
    #             answer = temp
    #
    #     return len(answer)

