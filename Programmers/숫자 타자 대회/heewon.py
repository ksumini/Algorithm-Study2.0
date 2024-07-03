'''
## 함수 설명
- `get_weight`: 두 숫자 버튼 간의 거리에 해당하는 가중치 값
- `square_dist`: 두 좌표 간의 제곱 거리 값

## 접근 방식
- 1st method - fail
    - 웬지 아닐 것 같지만 떠오르는 방법이 없어서 그리디로 접근
    - 최소 가중치를 가지는 번호로 이동
    - 동일한 가중치면 저장하고 나중에 계산
    - 반례를 찾음 '7240'
    - 느낀점
        - 일단 구현할 생각 보다는 반례를 생각해 보고 구현 하자(구현 시간 >> 반례 찾는 시간)
- 2nd method - 힌트 참고(`n이 10만이지만, 타이핑하기전의 엄지의 위치는 0 1 ~ 9 8 까지 100개가 되지 않습니다`)
    - 각각의 step마다 가능한 손가락들의 조합을 저장한다.
    - 겹치는 조합들은 최솟값으로 저장
    - 손가락이 동일한 숫자를 안 누르게 조심

## 추가 정보
- 시간: 2 hour 이하
- 힌트: `Tip`
'''

def solution(numbers: str) -> int:
    """
    입력된 문자열 `numbers`에서 가장 적은 손가락 움직임으로 텍스트를 입력하는 방법을 찾아 최소 움직임 값을 반환하는 함수입니다.

    Args:
        numbers: 숫자 버튼으로 구성된 입력 문자열입니다.

    Returns:
        입력된 텍스트를 입력하는 데 필요한 최소 손가락 움직임 값입니다.
    """

    prev_weight = {'46': 0} # 초기의 손가락의 가중치 값
    prev_fingers = ['46']   # 초기의 손가락 위치

    for num in numbers:
        current_fingers = [] # 현재의 손가락 위치들
        current_weight = {}     # 현재의 손가락 위치의 가중치 값

        for fingers in prev_fingers:    # 이전의 손가락 위치들
            left, right = fingers       # 왼손가락, 오른손가락의 "숫자"
            weight = prev_weight[fingers]   # 이전까지의 가중치 총합

            if num != right:   # 손가락 중복 피하기 위한 조건
                new_fingers = num + right   # 새로운 손가락 조합
                if new_fingers in current_weight:   # 기존의 조합이 존재하면
                    current_weight[new_fingers] = min(current_weight[new_fingers], weight + get_weight(left, num))  # 최솟값으로 수정
                else:   # 첫 손가락 조합
                    current_weight[new_fingers] = weight + get_weight(left, num)
                    current_fingers.append(new_fingers)    # 손가락 조합 추가 

            if num != left:     # 손가락 중복 피하기 위한 조건
                new_fingers = left + num    # 새로운 손가락 조합
                if new_fingers in current_weight:   # 기존의 조합이 존재하면
                    current_weight[new_fingers] = min(current_weight[new_fingers], weight + get_weight(right, num)) # 최솟값으로 수정
                else:   # 첫 손가락 조합
                    current_weight[new_fingers] = weight + get_weight(right, num)
                    current_fingers.append(new_fingers)    # 손가락 조합 추가 

        prev_fingers = current_fingers  # 이전 조합 갱신
        prev_weight = current_weight    # 이전 가중치 정보 갱신

    return min(prev_weight.values())    # 가장 적은 가중치 반환


def get_weight(n1: str, n2: str) -> int:
    """
    두 개의 문자열 `n1`과 `n2` (숫자 버튼)을 받아 거리에 해당하는 가중치를 반환하는 함수입니다. 
    가중치는 버튼들의 좌표 거리에 따라 결정됩니다.

    Args:
        n1: 첫 번째 숫자 버튼 문자열입니다.
        n2: 두 번째 숫자 버튼 문자열입니다.

    Returns:
        두 숫자 버튼 간의 거리에 해당하는 가중치 값입니다.
    """

    # 숫자 버튼과 그 위치를 매핑하는 사전
    phone_point = {'1': [0, 0], '2': [0, 1], '3': [0, 2],
                   '4': [1, 0], '5': [1, 1], '6': [1, 2],
                   '7': [2, 0], '8': [2, 1], '9': [2, 2],
                                '0': [3, 1]}

    # 입력받은 문자열에 해당하는 좌표값 얻기
    p1, p2 = phone_point[n1], phone_point[n2]

    # 거리 계산 함수를 이용하여 두 좌표 간의 거리 계산
    distance = square_dist(p1, p2)

    # 거리에 해당하는 가중치 정보
    weight_dict = {0: 1, 1: 2, 2: 3, 4: 4, 5: 5, 8: 6, 9: 6, 10: 7}

    return weight_dict[distance]


def square_dist(point1: list, point2: list) -> int:
    """
    두 개의 리스트 `point1`과 `point2` (좌표)를 받아 제곱 거리를 반환하는 함수입니다.

    Args:
        point1: 첫 번째 좌표 리스트입니다. (예: [x, y])
        point2: 두 번째 좌표 리스트입니다. (예: [x, y])

    Returns:
        두 좌표 간의 제곱 거리 값입니다.
    """

    # 각 차원에서의 거리 제곱 계산
    distance_x = (point1[0] - point2[0])**2
    distance_y = (point1[1] - point2[1])**2

    # 두 거리 제곱을 합하여 제곱 거리 계산
    return distance_x + distance_y
