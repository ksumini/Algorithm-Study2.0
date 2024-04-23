'''
## 함수 설명
- `airconditioner_off`: 에어컨 끄고 방치했을 때 실내 온도 변화량을 계산합니다.

## 접근 방식
- 1st method
    - DP를 이용하여 풀자!
        - 온도, 전력을 동시에 기록 -> i분에 그 X 온도 유지하는 전력의 경우
            ex) {20:[20, 22, 15], 21:[19,20]} : i분에 20도를 유지하려면 20, 22, 15 / 21도로 유지하려면 19,29 전력이 필요
        - 1st
            - 다음에 사람이 있으면 무조건 에어컨 가동
            - 없다면 가동하거나 가동 안 하거나
        - ith
            - i+1에 사람 없으면 에어컨 OFF, 에어컨 ON with 온도 유지 O, 에어컨 ON with 온도 유지 X
            - i+1에 사람 있으면 각각의 온도가 적정 범위에 있다면 추가
            - i+1에 전력을 추가시에 꼭 i번째의 최소 전력값으로 계산
        - 최종
            - 마지막에 시간에서 최고 온도의 최저 전력을 구한다.
    - 에어컨을 OFF시에 온도의 변화
        - 현재 실내 온도 > 실외 온도 -> 1도 감소
        - 현재 실내 온도 = 실외 온도 -> 온도 유지
        - 현재 실내 온도 < 실외 온도 -> 1도 증가
    - 에어컨 ON시에 온도의 변화
        - 적정 온도 < 실외 온도 -> 1도 감소(+a전력)
        - 적정 온도 > 실외 온도 -> 1도 증가(+a전력)
        - 상관 없음 -> 온도 유지(+b전력)
    
- 2nd method
    - 기존의 방식에서 초기 설정만 수정
    - DP 방법 같음
    - 실외 온도를 항상 적정 온도보다 높게 변경 why? 에어컨은 실내 온도를 낮추거나 온도 유지만 하게 코드 수정
        - if temperature< t1, t2 라면 t1, t2 < temperature 로 수정
        - temperature와 t1의 간격만큼 t2 보다 높게 설정
        - 에어컨을 OFF하면 온도가 증가하는 방향으로만 적용됨(+1, 0)

## 사용한 모듈
`defaultdict`

## 추가 정보
- 시간: 2 hour 이하
- 힌트: `None`
### 1st

<html>
<body>
<!--StartFragment--><pre class="console-content" style="box-sizing: border-box; padding: 0px; margin: 0px 0px 1.3125rem; color: white; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-variant-alternates: inherit; font-variant-position: inherit; font-weight: 400; font-stretch: inherit; font-size: 14px; line-height: inherit; font-family: Hack, Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace, &quot;맑은 고딕&quot;, &quot;malgun gothic&quot;, 돋움, Dotum, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: auto; display: block; border: none; background-color: rgb(38, 55, 71); border-radius: 0px; word-break: break-all; overflow-wrap: break-word; white-space: pre-wrap; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="console-heading" style="box-sizing: border-box; padding: 0px; margin: 1.5rem 0px 0.5rem; color: rgb(152, 168, 185); font: inherit;">채점을 시작합니다.</div><div class="console-message" style="box-sizing: border-box; padding: 0px; margin: 0.25rem 0px; color: rgb(95, 127, 144); font: inherit;">정확성  테스트</div>

테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (680.94ms, 97.8MB)
테스트 3 〉	통과 (13.99ms, 11.7MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.06ms, 10.3MB)
테스트 7 〉	통과 (0.06ms, 10.3MB)
테스트 8 〉	통과 (0.07ms, 10.4MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (6.21ms, 11MB)
테스트 11 〉	통과 (3.49ms, 10.5MB)
테스트 12 〉	통과 (3.68ms, 10.5MB)
테스트 13 〉	통과 (24.90ms, 13.8MB)
테스트 14 〉	통과 (39.64ms, 15.1MB)
테스트 15 〉	통과 (37.61ms, 15.2MB)
테스트 16 〉	통과 (42.51ms, 15.6MB)
테스트 17 〉	통과 (17.82ms, 12.9MB)
테스트 18 〉	통과 (15.60ms, 12.4MB)
테스트 19 〉	통과 (19.23ms, 12.6MB)
테스트 20 〉	통과 (31.83ms, 14.5MB)
테스트 21 〉	통과 (44.91ms, 15.4MB)
테스트 22 〉	통과 (346.08ms, 47.8MB)
테스트 23 〉	통과 (315.69ms, 47.6MB)
테스트 24 〉	통과 (313.50ms, 54.7MB)
테스트 25 〉	통과 (318.77ms, 54.7MB)

<div class="console-heading" style="box-sizing: border-box; padding: 0px; margin: 1.5rem 0px 0.5rem; color: rgb(152, 168, 185); font: inherit;">채점 결과</div><div class="console-message" style="box-sizing: border-box; padding: 0px; margin: 0.25rem 0px; color: rgb(95, 127, 144); font: inherit;">정확성: 100.0</div><div class="console-message" style="box-sizing: border-box; padding: 0px; margin: 0.25rem 0px; color: rgb(95, 127, 144); font: inherit;">합계: 100.0 / 100.0</div></pre><!--EndFragment-->
</body>
</html>


### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- #46
'''
#----------------------------1st----------------------------
from collections import defaultdict

def solution(temperature, t1, t2, a, b, onboard):
    """
    에어컨 사용 여부에 따른 실내 온도 변화와 전력 소비를 계산하여
    주어진 조건에서 최소 전력 소비량을 찾는 문제를 해결합니다.

    Args:
        temperature (int): 초기 실내 온도
        t1 (int): 에어컨 사용 시 실내 온도가 낮아지는 최대 한도
        t2 (int): 에어컨 사용 시 실내 온도가 높아지는 최대 한도
        a (int): 에어컨 사용 시 추가되는 전력 소비량
        b (int): 에어컨 끄고 방치했을 때 추가되는 전력 소비량
        onboard (List[int]): 각 시간대별 승객 탑승 여부 (1: 탑승, 0: 미탑승)

    Returns:
        int: 주어진 조건에서 최소 전력 소비량
    """

    def airconditioner_off(now_temperature):
        """
        에어컨 끄고 방치했을 때 실내 온도 변화를 계산합니다.

        Args:
            now_temperature (int): 현재 실내 온도

        Returns:
            int: 에어컨 끄고 방치했을 때 실내 온도 변화량
        """
        if now_temperature > temperature: return -1 # 실내 온도 > 실외 온도
        elif now_temperature == temperature: return 0 # 실내 온도 = 실외 온도
        else: return 1 # 실내 온도 < 실외 온도

    answer = float('inf')
    air_on = -1 if temperature > t2 else 1  # 에어컨 켜면 실내온도가 변하는 정도 / t1, t2 상관 없음
    N = len(onboard)  # 승객이 탑승 중인 시간대의 개수
    cases = [defaultdict(list) for _ in range(N)]  # 각 시간대별 가능한 모든 경우의 수를 저장하는 리스트
    now_temperature = temperature  # 현재 실내온도를 초기화
    air_off = airconditioner_off(now_temperature)  # 에어컨 끌 때의 온도 변화량을 계산

    # 첫 번째 시간대의 경우를 계산
    if onboard[1] == 0:
        # 에어컨 ON
        cases[1][now_temperature + air_on].append(a)
        # 에어컨 OFF
        cases[1][now_temperature + air_off].append(0)
    else:
        # 에어컨 ON
        cases[1][now_temperature + air_on].append(a)

    # 두 번째 시간대부터 마지막 시간대까지의 경우를 계산
    for i in range(1, N - 1):
        for case in cases[i].items():
            now_temperature, powers = case  # 현재 실내온도와 가능한 소비전력들을 가져옴
            air_off = airconditioner_off(now_temperature)  # 에어컨 끌 때의 온도 변화량을 다시 계산

            # 다음 시간대에서의 가능한 경우들을 계산
            if onboard[i + 1] == 0:
                # 에어컨 ON, 온도 유지 X
                cases[i + 1][now_temperature + air_on].append(min(powers) + a)
                # 에어컨 OFF
                cases[i + 1][now_temperature + air_off].append(min(powers))
                # 에어컨 ON, 온도 유지 O
                if air_off != 0 and t1 <= now_temperature <= t2:
                    cases[i + 1][now_temperature].append(min(powers) + b)
            else:
                # 에어컨 ON, 온도 유지 X
                if t1 <= now_temperature + air_on <= t2:
                    cases[i + 1][now_temperature + air_on].append(min(powers) + a)
                # 에어컨 ON, 온도 유지 O
                if t1 <= now_temperature <= t2:
                    cases[i + 1][now_temperature].append(min(powers) + b)
                # 에어컨 OFF
                if air_off != 0 and t1 <= now_temperature + air_off <= t2:
                    cases[i + 1][now_temperature + air_off].append(min(powers))

    # 최저 전력 계산
    for values in cases[-1].values():
        answer = min(answer, min(values))
        
    return answer

#----------------------------2nd----------------------------

from collections import defaultdict

def solution(temperature, t1, t2, a, b, onboard):
    """
    에어컨 사용 여부에 따른 실내 온도 변화와 전력 소비를 계산하여
    주어진 조건에서 최소 전력 소비량을 찾는 문제를 해결합니다.

    Args:
        temperature (int): 초기 실내 온도
        t1 (int): 에어컨 사용 시 실내 온도가 낮아지는 최대 한도
        t2 (int): 에어컨 사용 시 실내 온도가 높아지는 최대 한도
        a (int): 에어컨 사용 시 추가되는 전력 소비량
        b (int): 에어컨 끄고 방치했을 때 추가되는 전력 소비량
        onboard (List[int]): 각 시간대별 승객 탑승 여부 (1: 탑승, 0: 미탑승)

    Returns:
        int: 주어진 조건에서 최소 전력 소비량
    """

    def airconditioner_off(now_temperature):
        """
        에어컨 끄고 방치했을 때 실내 온도 변화를 계산합니다.

        Args:
            now_temperature (int): 현재 실내 온도

        Returns:
            int: 에어컨 끄고 방치했을 때 실내 온도 변화량
        """
        return 1 if now_temperature != temperature else 0

    answer = float('inf')
    # 실외의 온도가 높게 설정
    if temperature < t1:
        temperature = t2 + (t1 - temperature)
    N = len(onboard)  # 승객이 탑승 중인 시간대의 개수
    cases = [defaultdict(list) for _ in range(N)]  # 각 시간대별 가능한 모든 경우의 수를 저장하는 리스트
    now_temperature = temperature  # 현재 실내온도를 초기화
    air_off = airconditioner_off(now_temperature)  # 에어컨 끌 때의 온도 변화량을 계산

    # 첫 번째 시간대의 경우를 계산
    if onboard[1] == 0:
        # 에어컨 ON
        cases[1][now_temperature - 1].append(a)
        # 에어컨 OFF
        cases[1][now_temperature + air_off].append(0)
    else:
        # 에어컨 ON
        cases[1][now_temperature - 1].append(a)

    # 두 번째 시간대부터 마지막 시간대까지의 경우를 계산
    for i in range(1, N - 1):
        for case in cases[i].items():
            now_temperature, powers = case  # 현재 실내온도와 가능한 소비전력들을 가져옴
            air_off = airconditioner_off(now_temperature)  # 에어컨 끌 때의 온도 변화량을 다시 계산

            # 다음 시간대에서의 가능한 경우들을 계산
            if onboard[i + 1] == 0:
                # 에어컨 ON, 온도 유지 X
                cases[i + 1][now_temperature - 1].append(min(powers) + a)
                # 에어컨 OFF
                cases[i + 1][now_temperature + air_off].append(min(powers))
                # 에어컨 ON, 온도 유지 O
                if air_off != 0 and t1 <= now_temperature <= t2:
                    cases[i + 1][now_temperature].append(min(powers) + b)
            else:
                # 에어컨 ON, 온도 유지 X
                if t1 <= now_temperature - 1 <= t2:
                    cases[i + 1][now_temperature - 1].append(min(powers) + a)
                # 에어컨 ON, 온도 유지 O
                if t1 <= now_temperature <= t2:
                    cases[i + 1][now_temperature].append(min(powers) + b)
                # 에어컨 OFF
                if air_off != 0 and t1 <= now_temperature + air_off <= t2:
                    cases[i + 1][now_temperature + air_off].append(min(powers))

    # 최저 전력 계산
    for values in cases[-1].values():
        answer = min(answer, min(values))

    return answer

# fail code 32점
from collections import defaultdict

def solution(temperature, t1, t2, a, b, onboard):
    # 에어컨 끄면 실내온도의 변화량을 계산하는 함수
    def airconditioner_off(now_temperature:int)->int:
        if now_temperature > temperature:
            return  -1
        elif now_temperature == temperature:
            return  0
        else:
            return 1
        return air_delta
    
    answer = 0
    air_on = -1 if temperature > t2 else 1  # 에어컨 켜면 실내온도가 변하는 정도
    N = len(onboard)  # 승객이 탑승 중인 시간대의 개수
    cases = [defaultdict(int) for _ in range(N)]  # 각 시간대별로 가능한 모든 경우의 수를 저장하는 리스트
    now_temperature = temperature  # 현재 실내온도를 초기화
    air_off = airconditioner_off(now_temperature)  # 에어컨 끌 때의 온도 변화량을 계산
    
    # 첫 번째 시간대의 경우를 계산
    if onboard[1] == 0:
        cases[1][now_temperature + air_on] = a
        cases[1][now_temperature] = 0
    else:
        if t1 <= now_temperature + air_on <= t2:
            cases[1][now_temperature + air_on] = a
        if t1 <= now_temperature <= t2:
            cases[1][now_temperature] = 0
    
    # 두 번째 시간대부터 마지막 시간대까지의 경우를 계산
    for i in range(1, N-1):
        for case in cases[i].items():
            now_temperature, power = case  # 현재 실내온도와 소비전력을 가져옴
            air_off = airconditioner_off(now_temperature)  # 에어컨 끌 때의 온도 변화량을 다시 계산
            
            # 다음 시간대에서의 가능한 경우들을 계산
            if onboard[i+1] == 0:
                cases[i+1][now_temperature + air_on] = min(power + a, cases[i+1][now_temperature + air_on]) if cases[i+1][now_temperature + air_on] != 0 else power + a
                cases[i+1][now_temperature + air_off] = min(power, cases[i+1][now_temperature + air_off]) if cases[i+1][now_temperature + air_off] != 0 else power
                if air_off != 0:
                    cases[i+1][now_temperature] = min(power + b, cases[i+1][now_temperature]) if cases[i+1][now_temperature] != 0 else power + b
            else:
                if t1 <= now_temperature + air_on <= t2:
                    cases[i+1][now_temperature + air_on] = min(power + a, cases[i+1][now_temperature + air_on]) if cases[i+1][now_temperature + air_on] != 0 else power + a
                if t1 <= now_temperature <= t2:
                    cases[i+1][now_temperature] = min(power + b, cases[i+1][now_temperature]) if cases[i+1][now_temperature] != 0 else power + b
                if air_off != 0 and t1 <= now_temperature + air_off <= t2:
                    cases[i+1][now_temperature + air_off] = min(power, cases[i+1][now_temperature + air_off]) if cases[i+1][now_temperature + air_off] != 0 else power
                
    return min(cases[-1].values())