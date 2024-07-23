"""
<문제>
일렬로 나열된 N개의 집에 택배를 배달한다.
배달 물건은 모두 재활용 택배 상자에 담아 배달하며, 빈 재활용 택배상자들은 수거한다.
트럭에는 재활용 택배 상자를 최대 cap개 실을 수 있다.
트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리를 구하려 한다.
각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있다.

<제한 사항>
- 1 ≤ cap ≤ 50
- 1 ≤ n ≤ 100,000
- deliveries의 길이 = pickups의 길이 = n
    - deliveries[i]는 i+1번째 집에 배달할 재활용 택배 상자의 개수를 나타낸다.
    - pickups[i]는 i+1번째 집에서 수거할 빈 재활용 택배 상자의 개수를 나타낸다.
    - 0 ≤ deliveries의 원소 ≤ 50
    - 0 ≤ pickups의 원소 ≤ 50
- 트럭의 초기 위치는 물류창고

<풀이 시간>
40분

<풀이>
이동 거리가 최소가 되려면, 왕복을 최대한 줄이기 위해 가야하는 최대로 이동하며 cap만큼 배달하고, 돌아오는 길에 cap만큼 수거해야 한다.
1. 가장 멀리 있는 배달 및 수거 지점을 찾는다.
2. 해당 지점까지 이동하며 cap만큼의 물건을 모두 배달한다.
3. 물류창고까지 돌아오며 cap만큼의 물건을 모두 수거한다.
위의 2, 3 과정을 더 이상 배달 및 수거할 물건이 없을 때까지 반복한다.

<시간 복잡도>
초기 최대 거리 계산: O(n)
각 집을 최대 한 번 방문: O(n)
"""


def solution(cap: int, n: int, deliveries: list, pickups: list) -> int:
    """
    :param cap: 트럭에 실을 수 있는 재활용 택배 상자의 최대 개수
    :param n: 배달할 집의 개수
    :param deliveries: 각 집에 배달할 재활용 택배 상자의 개수를 담은 1차원 정수 배열
    :param pickups: 각 집에서 수거할 빈 재활용 택배 상자의 개수를 담은 1차원 정수 배열
    :return: 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
    """
    answer = 0
    # 가장 멀리 있는 배달 및 수거 지점 찾기
    max_delivery, max_pickup = -1, -1
    for i in range(n):
        if deliveries[i] != 0:
            max_delivery = i
        if pickups[i] != 0:
            max_pickup = i

    # 모든 배달과 수거를 완료할 때까지 반복
    while max_delivery >= 0 or max_pickup >= 0:
        answer += (max(max_delivery, max_pickup) + 1) * 2 # 왕복거리

        # 가는 길에 전부 배달
        cur_left = cap
        while cur_left != 0 and max_delivery >= 0:
            if deliveries[max_delivery] <= cur_left:
                cur_left -= deliveries[max_delivery]
                deliveries[max_delivery] = 0
                while max_delivery >= 0 and deliveries[max_delivery] == 0:
                    max_delivery -= 1
            else:
                deliveries[max_delivery] -= cur_left
                cur_left = 0

        # 돌아오는 길에 전부 수거
        cur_left = cap
        while cur_left != 0 and max_pickup >= 0:
            if pickups[max_pickup] <= cur_left:
                cur_left -= pickups[max_pickup]
                pickups[max_pickup] = 0
                while max_pickup >= 0 and pickups[max_pickup] == 0:
                    max_pickup -= 1
            else:
                pickups[max_pickup] -= cur_left
                cur_left = 0

    # 수거해야할 집의 최대 거리
    return answer