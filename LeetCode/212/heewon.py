class Solution:
    def dfs(self, x, y, word, visited):
        # 현재 위치의 문자를 단어에 추가
        word += self.board[x][y]
        
        # 단어 길이가 최대 길이를 초과하면 종료
        if len(word) > self.max_len:
            return
        
        # 현재까지 만들어진 단어를 가능한 단어 집합에 추가
        self.can_word.add(word)
        
        # 현재 위치를 방문 처리
        visited.add((x, y))
        
        # 상하좌우 네 방향에 대해 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            # 새 위치가 방문하지 않았고, 보드 범위 내에 있으면 탐색 계속
            if (nx, ny) not in visited and 0 <= nx < self.m and 0 <= ny < self.n:
                self.dfs(nx, ny, word, visited)
        
        # 백트래킹: 현재 위치를 방문 집합에서 제거
        visited.remove((x,y))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answer = []
        self.board = board
        self.m = len(board)  # 보드의 행 수
        self.n = len(board[0])  # 보드의 열 수
        self.can_word = set()  # 보드에서 만들 수 있는 모든 단어를 저장할 집합
        
        # 주어진 단어들의 첫 글자 목록
        first_word = [word[0] for word in words]
        
        # 주어진 단어들 중 가장 긴 단어의 길이 계산
        self.max_len = 0
        for word in words:
            self.max_len = max(self.max_len, len(word))
        
        # 보드의 모든 위치에서 DFS 탐색 시작
        for i in range(self.m):
            for j in range(self.n):
                # 현재 위치의 문자가 어떤 단어의 첫 글자라면 DFS 시작
                if self.board[i][j] in first_word:
                    self.dfs(i, j, '', set([(i,j)]))
        
        # 주어진 단어들 중 보드에서 만들 수 있는 단어만 답안에 추가
        for word in words:
            if word in self.can_word:
                answer.append(word)
        
        return answer