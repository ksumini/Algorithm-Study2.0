def solution(target):
    # 다트 점수와 유형 정의
    single = list(range(1, 21))  # 1부터 20까지의 싱글 점수
    double = [2 * x for x in range(1, 21)]  # 각 숫자의 두 배인 더블 점수
    triple = [3 * x for x in range(1, 21)]  # 각 숫자의 세 배인 트리플 점수
    bull = [50]  # 불 점수 (50점)
    
    # 가능한 점수와 그 유형 정의
    scores = single + double + triple + bull  # 모든 가능한 점수를 리스트로 합침
    types = ['S'] * 20 + ['D'] * 20 + ['T'] * 20 + ['B']  # 각 점수에 대응하는 유형(S, D, T, B)

    # DP 배열 초기화: (최소 다트 수, 싱글 또는 불의 횟수)
    dp = [(float('inf'), float('inf'))] * (target + 1)  # DP 배열을 무한대로 초기화
    dp[0] = (0, 0)  # 점수가 0일 때는 다트를 던질 필요가 없으므로 (0, 0)으로 초기화
    
    # 가능한 각 점수와 유형에 대해 DP 갱신
    for score, t in zip(scores, types):  # 점수와 그 유형을 순회
        for i in range(score, target + 1):  # 현재 점수에서 목표 점수까지 순회
            prev_darts, prev_singles_bulls = dp[i - score]  # 현재 점수에서 해당 점수를 뺀 나머지 점수의 DP 값 가져옴
            if t == 'S' or t == 'B':  # 현재 점수가 싱글이거나 불인 경우
                new_darts = prev_darts + 1  # 다트 수 증가
                new_singles_bulls = prev_singles_bulls + 1  # 싱글/불 횟수 증가
            else:  # 더블이나 트리플인 경우
                new_darts = prev_darts + 1  # 다트 수만 증가
                new_singles_bulls = prev_singles_bulls  # 싱글/불 횟수는 그대로

            # 새로운 다트 수가 현재 저장된 다트 수보다 작거나, 
            # 다트 수가 같고 싱글/불 횟수가 더 많으면 DP 갱신
            if new_darts < dp[i][0] or (new_darts == dp[i][0] and new_singles_bulls > dp[i][1]):
                dp[i] = (new_darts, new_singles_bulls)  # DP 배열 갱신
    
    return list(dp[target])
