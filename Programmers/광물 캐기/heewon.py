'''
## 함수 설명
- `get_fatigue`: 광물의 종류에 맞는 모든 곡괭이 피로도 반환

## 접근 방식
- 5개의 광물을 주기로 [다이아, 철, 돌] 곡괭이를 사용할 때의 피로도 구하기
- 피로도 주기는 총 곡괭이 수와 광물의 주기(math.ceil(n/5))의 최솟값
    - 곡괭이가 충분한 경우 -> 모든 광물을 캘때까지
    - 곡괭이가 부족한 경우 -> 곡괭이 못 쓰는 광물은 고려 못 함
- 피로도를 최대한 줄이는 방향으로 정력 이후에 곡괭이를 (다이아, 철, 돌) 차례대로 사용

## 사용한 모듈
`math`

## 추가 정보
- 시간: 1 hour 이하
- 힌트: `None`

### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- # 62
'''
from typing import List
import math

def solution(picks:List, minerals:List)->int:
    """
    Args:
        picks: 곡괭이의 개수
        minerals: 광물들의 순서

    Returns:
        마인이 작업을 끝내기까지 필요한 최소한의 피로도
    """
    def get_fatigue(mineral:str)->List:
        """
        Args:
            mineral: 광물의 종류

        Returns:
            광물의 종류에 맞는 모든 곡괭이 피로도 반환
        """
        if mineral == 'diamond':
            return [1, 5, 25]
        elif mineral == 'iron':
            return [1, 1, 5]
        else:
            return [1, 1, 1]
        
    answer = 0
    
    n = len(minerals)
    m = min(sum(picks), math.ceil(n/5))
    
    period = 0
    idx = 0
    fatigue = [[0,0,0] for _ in range(m)]
    
    for mineral in minerals:
        for pick_idx, fati in enumerate(get_fatigue(mineral)):
            fatigue[idx][pick_idx] += fati
        period += 1
        if period == 5: # 다음 곡괭이 사용
            period = 0
            idx += 1
        if idx == m:    # 곡괭이가 부족하면 광물 캐기 STOP
            break
        
    # 둘다 정답
    # for f in sorted(fatigue, key=lambda x: [-(x[1]-x[0]), -(x[2]-x[1])]):
    for f in sorted(fatigue, key=lambda x: [-x[2], -x[1]]):
        if picks[0] != 0:       # 다이아 곡괭이 사용
            answer += f[0]
            picks[0] -= 1
        elif picks[1] != 0:     # 철 곡괭이 사용
            answer += f[1]
            picks[1] -= 1
        elif picks[2] != 0:     # 돌 곡괭이 사용
            answer += f[2]
            picks[2] -= 1
    return answer