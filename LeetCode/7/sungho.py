class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False
        if x < 0:
            is_negative = True

        x = str(abs(x))  # 절대값으로 변환하여 부호 제거
        result = x[::-1]  # 문자열을 뒤집음

        result = int(result)

        if is_negative: # 음수면 부호 변경
            result *= -1

        if result < -2 ** 31 or result > 2 ** 31 - 1: # 한도초과
            return 0

        return result
