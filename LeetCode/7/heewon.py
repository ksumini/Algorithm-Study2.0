# 초기 코드 / 31ms / 16.45 MB
class Solution:
    def check_int(self, x: int) -> bool:
        if -2**31 <= x <= 2**31 - 1:
            return True
        return False
    def reverse(self, x: int) -> int:
        if x > 0 and self.check_int(int(str(x)[::-1])):
            return int(str(x)[::-1])
        elif x < 0 and self.check_int(-int(str(-x)[::-1])):
            return -int(str(-x)[::-1])
        return 0
    
# 최적화? 39ms / 16.49 MB
class Solution:
    def check_int(self, x: int) -> int:
        reversed_x = int(str(x)[::-1])  # 역전
        if -2**31 <= reversed_x <= 2**31 - 1:   # int check
            return reversed_x
        return 0

    def reverse(self, x: int) -> int:
        if x > 0:
            return self.check_int(x)
        elif x < 0:
            return -self.check_int(-x)
        return 0