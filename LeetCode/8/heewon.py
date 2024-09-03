class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        
        sign = 1
        sign_check = False

        for alp in s:
            if alp == ' ':  # 1
                if ans or sign_check:
                    break
                continue
            if alp in ['+', '-']:   # 2
                if ans or sign_check:
                    break
                sign = 1 if alp == '+' else -1
                sign_check = True
            elif alp.isdigit(): # 3
                ans += alp
            else:
                break

        if ans: # 4
            ans = int(ans) * sign
            if -2**31 <= ans <= 2**31 - 1:
                return ans
            elif sign == 1:
                return 2**31 - 1
            else:
                return -2**31
        return 0