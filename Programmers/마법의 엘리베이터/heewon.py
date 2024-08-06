def solution(storey):
    """
    주어진 층수를 올라가는데 필요한 최소 버튼 횟수를 계산하는 함수

    Args:
      storey: 올라갈 층수

    Returns:
      최소 버튼 횟수
    """

    answer = 0
    while storey:
        # 층수에서 일의 자리 숫자를 분리
        storey, r = divmod(storey, 10)

        # 올라갈 층수가 5 이상이거나, 1의 자리 숫자가 5이고 10의 자리 숫자가 5 이상이면
        if r > 5 or (storey % 10 >= 5 and r == 5):
            # 다음 층까지 올라가는 것이 더 효율적
            answer += 10 - r
            storey += 1
        else:
            # 현재 층에서 버튼을 누르는 것이 더 효율적
            answer += r

    return answer
