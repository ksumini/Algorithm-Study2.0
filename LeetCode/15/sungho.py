class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answers = set()

        # 중복 원소 갯수 세기
        nums_dict = Counter(nums)

        # 원소 기준으로 순서 정렬
        list_nums_dict = sorted(list(nums_dict.items()))

        for i in range(len(list_nums_dict)):
            k1, v1 = list_nums_dict[i]  # k1 원소에 대해
            for j in range(i + 1, len(list_nums_dict)):  # 다른 원소 k2
                k2, v2 = list_nums_dict[j]
                if (-k1 - k2) in nums_dict:  # k1, k2가 주어지면 k3 그러니까 원소 3개의 합이 0인 거가 어떤 원소인지 알게됨(-k1-k2)
                    if -k1 - k2 != k1 and -k1 - k2 != k2:
                        answers.add(tuple(sorted([k1, k2, -k1 - k2])))
                    elif -k1 - k2 == k1 and -k1 - k2 != k2 and nums_dict[k1] >= 2:
                        answers.add(tuple(sorted([k1, k1, k2])))
                    elif -k1 - k2 == k2 and -k1 - k2 != k1 and nums_dict[k2] >= 2:
                        answers.add(tuple(sorted([k1, k2, k2])))

        if nums_dict[0] >= 3: # 0이 3개 이상있는 경우에는 추가
            answers.add((0, 0, 0))
        return list(answers)