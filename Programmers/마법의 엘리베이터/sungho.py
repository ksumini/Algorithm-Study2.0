def solution(storey: int):
    """
    +1 -1 +10 -10 +100 -100 ... 으로 절댓값 10^c 형태인 정수로 움직이는데 해당 층에서 0층까지 가는데 움직이는 최소 횟수
    :param storey: 층 수
    :return: 움직이는 최소 횟수
    """
    answer = 0

    # 합이 음수면 움직이지 않음
    # 규칙이 존재함.
    cnt = 0
    while storey != 0:
        if storey % 10 < 5: # 1의 자리가 5보다 작으면 그냥 -1로 내려오면 됨. 그래서 cnt에 1의 자리만큼 추가
            cnt += storey % 10
            storey = storey // 10
        elif storey % 10 > 5: # 1의 자리가 5보다 클 때 반대로 +1로 올라가면 됨. 그래서 cnt에 10 - 1의자리만큼 추가
            cnt += (10 - storey % 10)
            storey = storey // 10 + 1
        else:  # storey%10 == 5: # 만약 끝의 자리가 5인 경우에는 바로 앞자리가 몇인지 확인해서
            if (storey // 10) % 10 >= 5: # 앞자리가 5보다 크거나 같으면 +1로 올라가는게 이득임 (왜냐하면 앞자리가 6으로 변형됨)
                cnt += (10 - storey % 10)
                storey = storey // 10 + 1
            else: # 그게 아니면 그냥 내려오면 됨
                cnt += storey % 10
                storey = storey // 10
    return cnt