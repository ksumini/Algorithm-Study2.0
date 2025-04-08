class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bits = bin(a)
        b_bits = bin(b)
        c_bits = bin(c)

        length = len(bin(max(a,b,c)))

        count = 0
        for i in range(length):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            c_bit = (c >> i) & 1

            if c_bit == a_bit | b_bit :
                pass
            elif c_bit == a_bit & b_bit:
                count += 1
            elif c_bit:
                count +=1
            else:
                count += 2

            # print(f"{a} {b} {c} {a_bit} {b_bit} {c_bit} count {count}")
        return count