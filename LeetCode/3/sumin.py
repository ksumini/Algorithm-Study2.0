"""
<문제>
문자열 s가 주어졌을 때, 반복되는 문자없이 가장 긴 substring의 길이를 반환하는 함수 작성

<풀이 시간>
20분

<풀이>
투포인터로 풀이

<시간 복잡도>
O(n)
"""


class Solution:
    # 투포인터 풀이
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :param s: given string
        :return: the length of the longest substring
        """
        # 길이가 1이하인 경우는 바로 return
        if len(s) <= 1:
            return len(s)

        left = right = 0
        max_length = 0
        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_length = max(max_length, right-left)
            else:
                seen.remove(s[left])
                left += 1

        return max_length