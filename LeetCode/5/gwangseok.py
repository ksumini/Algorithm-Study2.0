# O(N^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        answer = ''
        left = 0
        while left < len(s):
            # Center가 될 구간을 구한다.
            # ...b..., ...bb...와 같이 같은 문자열을 가진 구간을 center로 본다.

            right = left + 1
            while right < len(s) and s[right] == s[left]:
                right += 1
            
            # right는 left와 문자가 다른 구간이므로, 
            # right - 1을 전달해줘, 
            # 현재 center에서의 max palidromic을 구한다.
            cur_palindromic = self.cur_max_palindromic(left, right-1)

            if len(cur_palindromic) > len(answer):
                answer = cur_palindromic
            
            left = right
        
        return answer
    
    def cur_max_palindromic(self, left, right) -> str:
        # center: s[left] ~ s[right]로 부터 
        # step을 증가시키며 max palidromic을 구한다.
        step = 1
        while True:
            compare_left = left - step
            compare_right = right + step

            if 0 <= compare_left and compare_right < len(self.s):
                if self.s[compare_left] != self.s[compare_right]:
                    break
                else:
                    step += 1
            else:
                break
        
        return self.s[left-(step-1):right+step]
            

        
        
