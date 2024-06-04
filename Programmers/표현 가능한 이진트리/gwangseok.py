# 시간 복잡도
# tree_depth: O(log(50)) -> O(1), 1e50의 이진수 length = 50  // 최대 depth: 6
# is_all_zero: O(2*6 - 1) -> O(1), 더미를 포함한 최대 길이 = 63
# is_root: O(63 + 2 * is_all_zero) -> O(1), 최대 길이 63이고 root만 확인 + 0일 때 좌, 우 child 확인
# 결국 O(N)


def tree_depth(length: int) -> int:
    # 이진수를 표현하기 위한 최소한의 tree depth를 구한다.
    # int(log_2(length)) + 1
    depth = 0
    while length > 0:
        length //= 2
        depth += 1
        
    return depth


def is_all_zero(tmp_str: str) -> bool:
    # 현재 입력된 binary string이 모두 0인지 판단.
    for c in tmp_str:
        if c == '1':
            return False
    
    return True


def is_root_one(tmp_bin: str) -> int:
    if len(tmp_bin) == 1:
        # 자식 노드가 없다면 root는 0이 되든 1이 되든 상관 없이 True
        return 1
    
    mid = len(tmp_bin) // 2  # root 노드가 될 index
    left_str = tmp_bin[:mid]  # root 노드를 기준으로 좌측 child
    right_str = tmp_bin[mid + 1:]  # root 노드를 기준으로 우측 child
    if tmp_bin[mid] == '0':  # root가 0일 경우
        if is_all_zero(left_str) and is_all_zero(right_str):
            # 좌, 우 child가 모두 0이면 True
            return 1
        else:
            # 모두 0이 아니면 False
            return 0
    
    # 좌, 우를 계속 검사
    # 좌, 우 모두 True여야 True 반환
    return is_root_one(left_str) and is_root_one(right_str)


def is_bin(num: int) -> int:
    str_bin = bin(num)[2:]  # 수를 이진수로 변환
    depth = tree_depth(len(str_bin))  # 이진수를 표현하기 tree depth -> 1e15: 6
    max_length = 2 ** depth - 1  # 포화 이진트리로 표현되는 수의 length -> 1e15: 63
    tree_bin = '0' * (max_length - len(str_bin)) + str_bin  # '0'을 더미로 넣어서 포화 이진트리로 표현
    return is_root_one(tree_bin)


def solution(numbers: list):
    answer = []
    for num in numbers:
        answer.append(is_bin(num))
    return answer
