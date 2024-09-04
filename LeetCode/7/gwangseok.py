class Solution:
    def reverse(self, x: int) -> int:
        num_str = str(x)

        if num_str[0] == '-':
            reverse_num_str = '-' + num_str[:0:-1]
        else:
            reverse_num_str = num_str[::-1]

        reverse_num = int(reverse_num_str)

        min_ = -2**31
        max_ = -min_ - 1

        if min_ <= reverse_num <= max_:
            return reverse_num
        return 0
