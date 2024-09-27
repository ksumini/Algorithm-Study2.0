class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_length = cur_length = 0

        contain = set()

        while right < len(s):
            while s[right] in contain:
                # 현재 추가할 string이 포함되어 있다면,
                # 포함되지 않을 때까지 left를 증가시키며 string을 제거한다.
                contain.remove(s[left])
                left += 1
                cur_length -= 1
            
            contain.add(s[right])
            cur_length += 1
            max_length = max(max_length, cur_length)
            right += 1

        return max_length
