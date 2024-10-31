class Solution:
    def findWords(self, board, words):
        # DFS 함수: 현재 위치(x,y)에서 시작하여 단어를 찾음
        def dfs(x, y, root):
            # 현재 위치의 문자를 저장
            letter = board[x][y]
            # Trie에서 현재 문자에 해당하는 노드를 가져옴
            cur = root[letter]
            
            # 현재 노드가 단어의 끝인지 확인
            # '#' 키가 있다면 완성된 단어이므로 제거하고 결과에 추가
            word = cur.pop('#', False)
            if word:
                res.append(word)
            
            # 현재 위치를 방문했다고 표시 ('*'로 임시 변경)
            board[x][y] = '*'
            
            # 상하좌우 네 방향으로 탐색
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # 다음 위치 계산
                nx, ny = x + dx, y + dy
                # 다음 위치가 보드 범위 안에 있고, 
                # 다음 문자가 현재 Trie 노드의 자식으로 존재하는 경우 탐색 진행
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in cur:
                    dfs(nx, ny, cur)
            
            # 탐색이 끝났으므로 원래 문자로 복구
            board[x][y] = letter
            
            # 현재 노드에 자식이 없다면 (더 이상 찾을 단어가 없다면)
            # 부모 노드에서 현재 문자 노드를 제거 (메모리 최적화)
            if not cur:
                root.pop(letter)
        
        # Trie 자료구조 생성
        trie = {}
        for word in words:
            # 현재 처리중인 단어의 Trie 노드
            node = trie
            # 단어의 각 문자를 Trie에 추가
            for char in word:
                # setdefault: 키가 존재하면 값을 반환, 없으면 새로운 dict를 생성
                node = node.setdefault(char, {})
            # 단어의 끝을 표시 ('#' 키에 완성된 단어를 저장)
            node['#'] = word
        
        # 보드의 크기 계산
        m, n = len(board), len(board[0])
        # 찾은 단어들을 저장할 리스트
        res = []
        
        # 보드의 모든 위치에서 탐색 시작
        for i in range(m):
            for j in range(n):
                # 현재 위치의 문자가 Trie의 시작 문자인 경우에만 탐색 시작
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        # 찾은 모든 단어 반환
        return res