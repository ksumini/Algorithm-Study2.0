class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :type: int
        """

        flips = 0
    
        while a > 0 or b > 0 or c > 0:
            # 각 숫자별 마지막 bit
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if (bit_a | bit_b) != bit_c:
                if bit_c == 1:
                    # bit_a, bit_b가 모두 0, bit_c는 1
                    # 하나만 1되면 됨.
                    flips += 1
                else:
                    # bit_c는 0 -> bit_a와 bit_b 모두 0으로 만들어야 함.
                    flips += bit_a + bit_b
        
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips
