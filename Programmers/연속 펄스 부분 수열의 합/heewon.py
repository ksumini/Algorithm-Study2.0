'''
## 접근 방식
- 펄스 2개 경우 미리 적용 후에 부분 수열 합 구하기
- 최대 부분 수열의 합은 DP 사용

## 사용한 모듈
`None`

## 추가 정보
- 시간: 1 hour 이하
- 힌트: `None`

### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- # 68
'''

def solution(sequence):
    answer = 0
    
    n = len(sequence)

    dp1 = [sequence[idx] * (-1) ** idx for idx in range(n)]         # 펄스: [1, -1, 1, ...]
    dp2 = [sequence[idx] * (-1) ** (idx + 1) for idx in range(n)]   # 펄스: [-1, 1, -1, ...]

    for i in range(1,n):
        dp1[i] = max(dp1[i - 1] + dp1[i], dp1[i])
        dp2[i] = max(dp2[i - 1] + dp2[i], dp2[i])
    
    return max(max(dp1), max(dp2))