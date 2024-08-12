# O(n)

class Solution:
    def minimumPushes(self, word: str) -> int:
        word_cnt = [0] * 26  # 알파벳 개수: 26
        for w in word:
            idx = ord(w) - ord('a')
            word_cnt[idx] += 1
        
        word_cnt.sort(reverse=True)

        answer = 0
        for idx in range(26):
            if word_cnt[idx] == 0:
                break
            
            # 0 ~ 7: 1
            # 8 ~ 15: 2
            # ...
            press = idx // 8 + 1
            answer += (press * word_cnt[idx])
        
        return answer    
