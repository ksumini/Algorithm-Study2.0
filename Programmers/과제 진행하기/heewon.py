'''
## 함수 설명
- `parse_time`: string 타입의 시간 문자열을 int 타입의 숫자로 변경

## 접근 방식
- 문자열을 모두 계산 가능한 숫자들로 변경 (start, playtime)
- `배열은 시간순으로 정렬되어 있지 않을 수 있습니다.` 를 고려하여 정렬 필요!
- 과제를 처리하는 방식
    - 과제의 이름과 시간을 같이 저장한다 -> [과제, 남은 시간]
    - 최근에 과제를 수행 -> `stack`을 사용
    - 새로운 과제를 받을 때마다 연기한 과제들과 비교한다.
        - 연기한 과제가 없으면 새로운 과제를 연기한 과제에 넣기
        - 연기한 과제가 있으면
            - 새로운 과제를 시작할 시간 이전에 연기한 과제를 끝낼수 있다면 끝내기
            - 새로운 과제를 시작할 시간 이전에 연기한 과제를 끝낼수 없다면 연기한 과제의 남은 시간을 수정해서 다시 저장
- plans 순서대로 처리한 후에 완료한 과제 목록에 연기한 과제 역순으로 추가

## 사용한 모듈
`typing`

## 추가 정보
- 시간: 1 hour 이하
- 힌트: `None`

### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- #54
'''

from typing import List

def solution(plans: List[List[str]]) -> List[str]:
    """
    # 계획 리스트를 입력받아 수업 스케줄 가능 여부를 판별하는 함수

    plans: [과제, 시작시간(시:분), 수업 시간(분)] 리스트

    returns: 수강 가능한 과제 리스트
    """

    def parse_time(time_str: str) -> int:
        """
        # 시간 문자열을 분 단위 정수형으로 변환하는 함수

        time: 시:분 형식의 시간 문자열

        returns: 분 단위 정수형
        """

        hours, minutes = map(int, time_str.split(':'))
        return 60 * hours + minutes

    answer = []  # 수강 가능한 과제 리스트
    suspend = []  # 연기하는 과제 리스트 (과제, 남은 수업시간)
    before_start_time = 0  # 이전 과제 시작 시간

    # 계획 리스트를 과제, 시작시간, 수업시간 형식으로 변환하고 시작 시간 순으로 정렬
    plans = [[x[0], parse_time(x[1]), int(x[2])] for x in plans]
    plans.sort(key=lambda x: x[1])

    for subject, start_time, playtime in plans:
        # 연기한 과목이 있으면 완료가 가능한지 확인
        while suspend:
            before_subject, before_duration = suspend.pop()
            # 다음 과제 전에 밀린 과제를 수행 가능한 경우
            if before_start_time + before_duration <= start_time:
                answer.append(before_subject)
                before_start_time += before_duration
            # 밀린 과제를 못 끝내는 경우
            else:
                # 밀린 과제를 stack에 넣기 전에 남은 과제양 갱신
                suspend.append([before_subject, before_duration - (start_time - before_start_time)])
                break
        # 현제 과제를 밀린 과제에 추가
        before_start_time = start_time
        suspend.append([subject, playtime])
    # 기존에 수행한 과제에 연기한 과제들을 역순으로 추가
    while suspend:
        answer.append(suspend.pop()[0])
    return answer