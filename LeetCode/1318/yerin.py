class Solution:
    def dec_to_list_bin(self, n):
        return list(map(int, format(n, 'b').zfill(30)))

    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a = self.dec_to_list_bin(a)
        bin_b = self.dec_to_list_bin(b)
        bin_c = self.dec_to_list_bin(c)

        ans = 0

        for a_bit, b_bit, c_bit in zip(bin_a, bin_b, bin_c):
            if (a_bit | b_bit) == c_bit:
                continue

            if c_bit == 0:
                ans += a_bit + b_bit
            else:
                ans += 1

        return ans


if __name__ == '__main__':
    print(Solution().minFlips(258343848, 90957776, 291428165))

