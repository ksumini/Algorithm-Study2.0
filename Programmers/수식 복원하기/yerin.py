'''
덧셈, 뺄셈
2~9진법

X : 지워진 결과값
? : 결과값이 불확실

ex) 51 - 5 = 44 8진법
41 - 5 = 36
44 -> 32 + 4 = 36
'''


# 10진수 -> n진수
def convert_decimal_to_base(num: int, base):
    if num == 0:
        return '0'
    formatted_num = ''
    while num > 0:
        formatted_num = str(num % base) + formatted_num
        num //= base
    return formatted_num


# n진수 -> 10진수
def convert_base_to_decimal(num: str, base):
    # return int(num, base)
    decimal_num = 0
    for i in range(len(num)):
        decimal_num += int(num[i]) * (base ** (len(num) - i - 1))
    return decimal_num

# 이미 완성된 식을 기반으로 가능한 진수들 리스트 확인
def set_base_options(expressions, std):
    # 불가능한 진수의 경우 False. 기본값은 True로 시작
    base_ops = {n: True for n in range(std, 10)}
    for expression in expressions:
        n1, operation, n2, _, n3 = expression.split(' ')

        # 모두 한 자리 수면 진수 상관 x
        if len(n1) == len(n2) == len(n3) == 1:
            continue

        for i in range(std, 10):
            # 10진수로 변환
            dec_n1 = convert_base_to_decimal(n1, i)
            dec_n2 = convert_base_to_decimal(n2, i)
            dec_n3 = convert_base_to_decimal(n3, i)

            if operation == '+' and dec_n1 + dec_n2 != dec_n3:
                base_ops[i] = False
            elif operation == '-' and dec_n1 - dec_n2 != dec_n3:
                base_ops[i] = False

    # True인 경우만 반환
    return [base for base, state in base_ops.items() if state]


# 가능한 진수들을 모아놓은 배열로 x 값 구하기
def get_x_by_base_options(expressions, base_list):
    ans = []
    for expression in expressions:
        n1, operation, n2, _, _ = expression.split(' ')
        n3_set = set()  # 진수별 x 값 저장하기 위한 배열

        for base in base_list:
            dec_n1 = convert_base_to_decimal(n1, base)
            dec_n2 = convert_base_to_decimal(n2, base)
            n3 = dec_n1 + dec_n2 if operation == "+" else dec_n1 - dec_n2
            n3_set.add(convert_decimal_to_base(n3, base))

        # 값이 두 개 이상 나오는 경우는 ? / 한 개 고정인 경우 계산한 값 할당
        if len(n3_set) == 1:
            ans.append(f"{n1} {operation} {n2} = {n3_set.pop()}")
        else:
            ans.append(f"{n1} {operation} {n2} = ?")

    return ans


def solution(expressions):
    un_solved = []
    solved = []
    max_num = 1
    for expression in expressions:
        # 문제가 풀어진 식(solved), 안 풀린 식(un_solved) 각각의 배열에 식 삽입
        if "X" in expression:
            un_solved.append(expression)
        else:
            solved.append(expression)

        n1, _, n2, _, n3 = expression.split(' ')
        # 모든 식을 돌면서 가장 큰 수를 찾음 -> 가능한 최소 진수를 판별하는 데 활용. (ex. 4진수의 경우 4 이상의 숫자를 사용할 수 없다)
        max_num = max(max_num, max(int(d) for d in n1 + n2 + (n3 if n3 != 'X' else '')))

    base_list = set_base_options(solved, max_num + 1)
    answer = get_x_by_base_options(un_solved, base_list)

    return answer

if __name__ == '__main__':
    print(solution(["10 + 2 = 12", "14 + 3 = 17", "30 + 31 = 101"]))
