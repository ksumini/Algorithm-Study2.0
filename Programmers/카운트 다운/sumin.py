"""
<문제>
시작시 무작위로 점수가 정해지고, 다트를 던지면서 점수를 깎아서 정확히 0점으로 만든다.
단, 남은 점수보다 큰 점수로 득점하면 버스트가 되며 실격한다.

과녁에는 1 ~ 20까지의 숫자가 하나씩 있다.
- 싱글: 해당 수만큼 점수를 얻는다
- 더블: 해당 수의 두 배만큼 점수를 얻는다
- 트리플: 해당 수의 세 배만큼 점수를 얻는다
- 불: 50점 득점

가장 먼저 0점을 만든 선수가 승리하는데,
만약 두 선수가 같은 라운드에 0점을 만들면 두 선수 중 '싱글' 또는 '불'을 더 많이 던진 선수가 승리한다.
그마저도 같다면 선공인 선수가 승리한다.

1. 최소한의 다트로 0점을 만든다.
2. 방법이 여러가지라면, '싱글' 또는 '불'을 최대한 많이 던지는 방법

<제한 사항>
1 ≤ target ≤ 100,000

<풀이 시간>
50분

<풀이>
1. 테이블 정의
dp[i] = 점수 i를 달성하기 위한 [최소 다트 수, 그때의 싱글/불 횟수]
2. 점화식 찾기
dp[i] = min(dp[i], dp[i-score][0] + 1, dp[i-score][1] + (1 if score <= 20 or score == 50 else 0))
3. 초기값 정하기
dp[0] = (0, 0)

<시간 복잡도>
O(target) * O(42: scores_by_one_shot의 크기) = O(target)
"""


def solution(target: int) -> list:
    """
    :param target: 목표 점수
    :return: 최선의 경우 던질 [다트 수, '싱글' 또는 '불'을 맞춘 횟수(합)]
    """
    scores_by_one_shot = set() # 1번 던져서 얻을 수 있는 모든 점수
    for i in range(1, 21):
        scores_by_one_shot.add(i)
        scores_by_one_shot.add(i * 2)
        scores_by_one_shot.add(i * 3)
    scores_by_one_shot.add(50)

    # 1. DP 테이블 정의(dp[i] = i점을 얻기 위한 최소한의 [다트 수, 싱글/불을 맞춘 횟수]
    dp = [(float('inf'), 0)] * (target + 1)
    # 2. 초기값 세팅
    dp[0] = (0, 0)
    # 3. 점화식(bottom-up)
    for i in range(1, target+1):
        for score in scores_by_one_shot: # 얻을 수 있는 모든 점수
            if i >= score:
                dart_cnt, single_bull_cnt = dp[i - score]
                new_dart_cnt = dart_cnt + 1
                new_single_bull_cnt = single_bull_cnt + (1 if score <= 20 or score == 50 else 0)
                # 최소한의 다트, '싱글' 또는 '불'을 최대한 많이
                if new_dart_cnt < dp[i][0] or (new_dart_cnt == dp[i][0] and new_single_bull_cnt > dp[i][1]):
                    dp[i] = (new_dart_cnt, new_single_bull_cnt)