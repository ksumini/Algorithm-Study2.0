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
    queue = [(start, end)]

    while queue:
        s, e = queue.pop(0)
        mid = (s + e) // 2
        if number[mid] == '0' and ('1' in number[s: mid] or '1' in number[mid + 1: e + 1]):
            return 0
        if (mid - s) % 2 == 0:
            return 0

        if s < mid - 1:
            queue.append((s, mid - 1))
            queue.append((mid + 1, e))
    else:
        return 1


def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = format(num, 'b')
        temp = []

        if '0' not in bin_num:
            answer.append(1)
            continue

        for i in range(0, round(len(bin_num) / 2)):
            leaf_cnt = len(bin_num) - (i + 1)
            if leaf_cnt % 2 == 0:
                continue
            temp_num = '0' * (leaf_cnt - i) + bin_num
            temp.append(check_tree(0, len(temp_num) - 1, temp_num))

        if 1 in temp:
            answer.append(1)
        else:
            answer.append(0)
    return answer