
# 내 풀이
# beats: 50%, memory: 50%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        n = len(s)
        DICT = {}

        for i in range(n):
            if s[i] not in DICT: # s[i]가 처음 들어왔을 때
                DICT[s[i]] = set()
                DICT[s[i]].add(s[i])
                for k, v in DICT.items(): # 모든 글자들에 추가
                    DICT[k].add(s[i])
            else: # 기존에 있는 것들이랑 겹쳐서 들어왔을 때
                for k, v in DICT.items(): # 모든 글자들에 대해서
                    if s[i] in v: # 이미 들어온 적이 있으면 wkw, wjkwlkw ...
                        answer = max(answer, len(v))  # 길이 비교하고
                        del DICT[k] # 제거하고
                    else:
                        DICT[k].add(s[i]) # 들어온 적이 없으면 또 길이 추가
                DICT[s[i]] = set() # D[s[i]] 갱신
                DICT[s[i]].add(s[i])
        values = DICT.values()
        for i in range(len(values)): # 길이 비교하기 위해서
            values[i] = len(values[i])
        answer = max(values + [answer]) # 한번에 결과찾기

        return answer


# 좀 더 최적화한 코드
# beats: 90%, memory: 90%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l, length = 0, 0

        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            length = max(length, r - l + 1)
            seen[char] = r

        return length
