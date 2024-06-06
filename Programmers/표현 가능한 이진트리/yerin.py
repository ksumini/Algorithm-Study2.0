'''
이진수 --> 문자열
왼쪽 --> 오른쪽 살펴봄(노드 높이 상관x)
if 현재 노드 == 더미 노드 : 문자열 뒤에 0 추가 (*2)
else: 문자열 뒤 1 추가 (*2+1)
return (이진수 --> 십진수)

[풀이]
십진수 input
십진수 --> 이진수
if 표현 가능한 이진트리: return 1
else: return 0

포화 이진트리가 안되는 경우
(예외: 문자열에 0이 없으면 이진트리 표현 가능)
: 루트노드가 0인데 리프노드가 1인 경우

- 십진수 --> 이진수 변환
- 앞에 생략되었을지도 모르는 0 고려. 양쪽 자식 노드 갯수 맞추기.
- 한 숫자에 여러 경우가 존재할 수 있으니 임의 리스트에 결과값을 저장. 그 중 하나의 경우라도 포화 이진트리로 만들어질 수 있다면(즉, 1이 존재한다면) answer에 1 삽입
- mid 계산 --> 부모 노드
- 부모가 0일 때, 자식 노드에 1이 없는지 확인. 1이 있으면 0 리턴
- 자식 노드가 짝수인 경우도 존재할 수 없으니, 짝수인 경우 0 리턴(이 경우를 찾는데 시간이 오래 걸림...)
- 문제가 없을 시, 바로 아래 자식노드들이 부모가 되게 하여 과정 반복
'''


def check_tree(start, end, number):
    '''
    Params
        int start : start 첫 번째 인덱스
        int end : number 마지막 인덱스
        str number : 이진수 문자열
        
    Returns
        int : 현재 노드가 '0'이고 하위 노드에 '1'이 있을 때, 하위 노드의 개수가 2 초과일 때 0 반환. 그 외의 경우 1 반환
    '''
    
    queue = [(start, end)]

    while queue:
        s, e = queue.pop(0)
        mid = (s + e) // 2 # 주어진 구간 [s,e]에서 가운데 노드를 기준으로 설정
        
        # 현재 노드(mid)의 좌우측 각각 확인
        if number[mid] == '0' and ('1' in number[s: mid] or '1' in number[mid + 1: e + 1]):
            return 0
        # 좌측 노드 개수를 카운트
        if (mid - s) % 2 == 0:
            return 0
        
        # 다음 탐색 대상 노드 업데이트
        if s < mid - 1:
            queue.append((s, mid - 1)) # 현재 노드 왼쪽 구간
            queue.append((mid + 1, e)) # 현재 노드 오른쪽 구간
    else:
        return 1


def solution(numbers):
    answer = []
    for num in numbers:
        if num == 1:
            answer.append(1)
            continue
        
        bin_num = format(num, 'b') #앞에 접두어 제거를 위해 format 사용
        temp = []
        
        # bin_num 앞에 생략되었을지도 모르는 '0' 추가.
        # 이진트리는 대칭 형태. 루트노드가 될 수 있는 건 'round(len(bin_num) / 2))' 번째까지
        # ex) 문자열 크기 5일 때 --> 3 번째/ 4일 때 --> 2 번째
        # i : 루트 노드 인덱스
    
        for i in range(0, round(len(bin_num) / 2)):
            leaf_cnt = len(bin_num) - (i + 1) # 오른쪽 하위 노드 개수 카운트
            if leaf_cnt % 2 == 0:
                continue
            temp_num = '0' * (leaf_cnt - i) + bin_num # 오른쪽 하위 노드 개수에 맞춰 더미 노드 추가
            temp.append(check_tree(0, len(temp_num) - 1, temp_num)) # bin_num을 활용하여 만들 수 있는 경우들에 대한 포화 이진트리 여부 검증. 결과값을 임시 리스트(temp)에 삽입

        # 하나의 경우라도 포화 이진트리 만족할 시 1 반환
        if 1 in temp:
            answer.append(1)
        else:
            answer.append(0)
    return answer