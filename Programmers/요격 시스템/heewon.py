'''

## 접근 방식
- e 좌표를 기준으로 정렬해서 카운트

## 사용한 모듈
`없음`

## 추가 정보
- 시간: 1 hour 미만
- 힌트: `None`



### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- #34
'''

def solution(targets):
    answer = 0
    launch = 0
    for s, e in sorted(targets, key= lambda x: x[1]):
        # 기준 값을 지나면 새로운 미사일 출발 지점 정하기 
        if launch <= s:
            answer += 1
            launch = e
    return answer