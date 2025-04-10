class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(30):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            c_bit = (c >> i) & 1

            if (a_bit | b_bit) == c_bit:
                continue

            if c_bit == 0:
                ans += a_bit + b_bit  # 최대 2까지 가능
            else:
                ans += 1  # c_bit == 1인데 둘 다 0이면 한 번 flip 필요

        return ans
