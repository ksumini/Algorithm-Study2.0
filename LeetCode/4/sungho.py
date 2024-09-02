class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s

        def check_palindrome(s, start, end):
            """
            s[start:end+1]이 대칭단어인지 아닌지 판별
            :param s:
            :param start:
            :param end:
            :return:
            """
            word = s[start:end + 1]
            if word == word[::-1]:
                return True
            return False
            # for i in range((end-start+1)//2):
            #    if s[start+i] != s[end-i]:
            #        return False
            # return True

        section = [0, 1]  # idx 0 만 추가
        for i in range(n - 1):
            for j in range(i + 1, n):
                if j + 1 - i > section[1] - section[0] and check_palindrome(s, i, j):
                    section = [i, j + 1]
        return s[section[0]:section[1]]


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:  # 1개이하인 경우
            return s

        result = ''
        for i in range(n - 1):
            L, R = 0, 0
            # 중앙부
            if s[i] != s[i + 1]:  # 홀수인 경우
                L, R = i - 1, i + 1
            else:  # 짝수인 경우
                t = i
                while t < n and s[t] == s[i]:
                    R = t
                    t += 1
                L = i - 1
                R += 1

            # 옆에 날개
            while L > -1 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            if R - L > len(result):
                result = s[L + 1:R]
        return result
