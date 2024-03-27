'''
## 함수 설명
- `real_time`: 시침, 분침, 초침들의 실제 값 ex) 12시 30초 -> 0.00833333333333286시 0.5분 30초

## 접근 방식
- 조건에서 h, m, s 값이 정수라는 조건이 없으므로 소수도 고려! -> real time이 중요 -> 하지만 모두 정수였다.
- 문제를 잘못 이해함
    - Fact: 초침이 분침과 시침이 만날 때만 알람
    - 오해: 초침이 분침과 시침이 만날 때 + 분침과 시침의 만날 때 알람
- h1:m1:s1 ~ h2:m2:s2 사이의 알람 수를 직접 구하지 않고 `00:00:00 ~ h2:m2:s2 사이의 알람 수` - `00:00:00 ~ h1:m1:s1 사이의 알람 수`
- 예외 처리 필요
    - 

## 사용한 모듈
`없음`

## 추가 정보
- 시간: 4 hour
- 힌트: (아이디어 및 코드 참고)[https://school.programmers.co.kr/questions/63464]

채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.4MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

def solution(h1, m1, s1, h2, m2, s2):
    # 시침, 분침, 초침들의 실제 값
    def real_time(hour: int, minute: int, second: int):
        return (hour + minute / 60 + second / 3600) % 12, minute + second / 60, second
    # 0시 0분 0초 기준으로 알람이 울린 횟수
    def get_alarm(hour, minute, second):
        real_hour, real_minute, real_second = real_time(hour, minute, second)
        # 기준이 0시 0분 0초 이므로 첫 1바퀴는 1번만 울림
        alarm_cnt = -1
        # 최종 초침이 시침을 지날 때
        if real_hour * 5 <= real_second:
            alarm_cnt += 1
        # 최종 초침이 분침을 지날 때
        if real_minute <= real_second:
            alarm_cnt += 1
        # 12시에 1번만 만나기 때문에
        if hour >=12:
            alarm_cnt -= 2
        # 초침이 1바퀴 도는 횟수
        alarm_cnt += (hour * 60 + minute) * 2
        # 시간당 시침과 안 만남
        alarm_cnt -= hour
        return alarm_cnt
    answer = get_alarm(h2, m2, s2) - get_alarm(h1, m1, s1)
    # 0시, 12시에 시침과 만나서
    if ((h1 == 0 or h1 == 12) and (m1 == 0) and (s1 == 0)):
        answer += 1
    return answer

# fail 시도
# 여러 경우를 고려하여 계산하려고 했지만 머리 과부하로 포기 -> 문제 잘못 이해해서 발생

def solution(h1, m1, s1, h2, m2, s2):
    # 시침과 분침의 정확한 위치
    def real_time(hour, minute, second):
        return hour + minute / 60 + second / 3600, minute + second / 60
    # 처음과 종료에서 침들이 겹치면 count
    def start_end_check(hour, minute, second):
        cnt = 0
        if hour >= 12:
            hour -= 12
        # 3개가 겹치나 2개가 겹치나 1번만 겹치기에 or
        if hour * 5 == minute or second == minute:
            cnt += 1
        return cnt
        
    answer = 0
    sec_cicle = (h2-h1) * 60 + m2 - m1
    min_cicle = h2 - h1
    if s1 > s2:
        sec_cicle -= 1
    if m1 > m2:
        min_cicle -= 1
    h1, m1 = real_time(h1, m1, s1)
    h2, m2 = real_time(h2, m2, s2)
    # print(h1, h2, m1, m2)
    
    # sec_cicle = max(int(m2 - m1), 0) + 60 * int(h2 - h1)
    # min_cicle = int(h2 - h1)
    print(sec_cicle, min_cicle)
    # if s2 == 0: s2 = 60
    if s1 < m1 and m2 < s2:
        # print('1')
        answer += 1
    if s1 < 5 * h1 and (5 * h2 < s2 or (s2 == 0 and 5 * h2 < s2 + 60)):
        # print('2')
        answer += 1
    if m1 < 5 * h1 and 5 * h2 < m2:
        # print('3')
        answer += 1
    answer += start_end_check(h1, m1, s1) + start_end_check(h2, m2, s2)
    answer += (min_cicle) * 2
    answer += sec_cicle * 2
    return answer