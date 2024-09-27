#  런타임 : 28.35% / 메모리 : 39.84%
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         ans = ''
#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 if s[i] == s[j-1]:
#                     temp_s = s[i:j]
#                     reversed_temp_s = temp_s[::-1]
#                     if reversed_temp_s == temp_s and len(ans) < len(temp_s):
#                         ans = temp_s
#         return ans
#
#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.longestPalindrome("aacabdkacaa"))

#  런타임 : 89.34% / 메모리 : 72.03%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 주어진 인덱스 범위에서 가능한 긴 palindromic substring 찾는 함수
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 현재 left와 right는 팰린드롬 경계를 벗어난 상태이므로, 경계 안쪽 문자열 반환
            return s[left + 1:right]

        n = len(s)
        ans = ''

        for i in range(n):
            # 길이가 홀수일 때 (중심이 하나인 경우)
            palindrome1 = expand_around_center(i, i)
            # 길이가 짝수일 때 (중심이 두 개인 경우)
            palindrome2 = expand_around_center(i, i + 1)

            if len(palindrome1) > len(ans):
                ans = palindrome1
            if len(palindrome2) > len(ans):
                ans = palindrome2

        return ans
