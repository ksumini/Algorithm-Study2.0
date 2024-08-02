def solution(cap, n, deliveries, pickups):
    """
    트럭의 최대 배송/픽업 용량이 각각 주어질 때, 모든 배송/픽업을 완료하는 데 필요한 총 거리를 계산하는 함수입니다.

    Args:
        cap: 트럭에 실을 수 있는 재활용 택배 상자의 최대 개수입니다.
        n: 집의 개수입니다.
        deliveries: 각 집에서 배송할 물건의 개수를 담은 리스트입니다.
        pickups: 각 집에서 픽업할 물건의 개수를 담은 리스트입니다.

    Returns:
        트럭이 이동한 총 거리를 반환합니다.
    """

    answer = 0

    # 각 집에서의 배송/픽업 정보를 거리와 작업 타입으로 나타내는 리스트
    dist_d = make_list(deliveries)
    dist_p = make_list(pickups)

    # 배송과 픽업 리스트의 마지막 인덱스
    idx_d, idx_p = len(dist_d) - 1, len(dist_p) - 1

    # 배송과 픽업 작업이 남아있는 동안 반복
    while idx_d + idx_p:
        answer += 2 * max(dist_d[idx_d], dist_p[idx_p]) # 가장 먼 거리의 배송지와 픽업지 중 더 먼 곳까지 이동

        idx_d = set_idx(idx_d, cap)
        idx_p = set_idx(idx_p, cap)

    return answer

def make_list(box_list:list)->list:
    dist = [0]
    for i, d in enumerate(box_list):
        dist.extend([i + 1] * d)  # 거리와 개수를 리스트에 추가
    return dist

def set_idx(idx:int, cap:int)->int:
    idx -= cap  # 트럭의 용량만큼 배송/픽업 작업 처리
    return max(idx, 0)  # 인덱스가 음수가 되지 않도록 처리