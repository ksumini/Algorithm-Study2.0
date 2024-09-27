def solution(cap: int, n: int, deliveries: list, pickups: list) -> int:
    """
    각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거하는데까지 최소 거리
    :param cap: 한 번에 들고 이동할 수 있는 물품 최대 갯수
    :param n: 집 개수. 1~n까지 일렬로
    :param deliveries: 배달 갯수
    :param pickups: 수거 갯수
    :return: 최소 거리
    """
    answer = 0

    del_idx, pick_idx = -1, -1  # 어디서부터 시작할지 idx 찾기 (뒤에서부터(idx 큰 곳) 다녀올 예정)
    for i in range(n - 1, -1, -1):
        if deliveries[i] != 0 and del_idx == -1:
            del_idx = i
        if pickups[i] != 0 and pick_idx == -1:
            pick_idx = i

        if del_idx != -1 and pick_idx != -1:
            break

    def next_idx(lists_: list, idx: int):
        """
        cap 만큼 물건을 배송 / 수거하고 다음 찾아야할 idx
        :param lists_: 배달 / 수거 list
        :param idx: idx부터 시작
        :return: 다음 배달/수거 list, 다음 idx, 움직인 거리
        """
        total_ = 0
        max_length = 0
        if idx == -1: # 이미 배달 / 수거가 다 진행된 상태
            return lists_, idx, 0

        while total_ < cap: # 더 들 수 있음
            if lists_[idx] == 0: # list_ idx가 0이면
                idx -= 1 # 다음 idx로
                if idx == -1: # 그러다 끝나면 끝
                    break
                continue

            if total_ + lists_[idx] > cap: # 더 들 수 없음. 해당 idx까지 일부만 들 수 있음
                if max_length == 0:
                    max_length = idx
                lists_[idx] -= (cap - total_)
                total_ = cap
                break
            else: # 더 들 수 있음
                if max_length == 0:
                    max_length = idx
                total_ += lists_[idx]
                lists_[idx] = 0
                idx -= 1

            if idx == -1:
                break

        if total_ == 0: # 만약 든게 없다면
            max_length = -1

        return lists_, idx, max_length + 1

    cnt = 0
    while True:
        cnt += 1
        if del_idx == -1 and pick_idx == -1:  # 끝까지 다 확인함
            break

        deliveries, del_idx, del_move = next_idx(deliveries, del_idx)
        pickups, pick_idx, pick_move = next_idx(pickups, pick_idx)

        answer += max(del_move, pick_move) * 2  # 가장 큰 배달, 수거 idx *2만큼 이동함
        # print("======================= HERE =======================")
        # print(deliveries, del_idx, del_move)
        # print(pickups, pick_idx, pick_move)
    return answer