class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        # 숫자 리버스
        if x < 0:
            reversed_x = int('-' + str(-x)[::-1])
        else:
            reversed_x = int(str(x)[::-1])

        return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0
