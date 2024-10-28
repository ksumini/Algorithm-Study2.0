"""
<문제>
각 수식은 2진법 ~ 9진법 중 하나.
덧셈 혹은 뺄셈 수식들이 담긴 1차원 문자열 배열 expressions가 매개변수로 주어진다.
결괏값이 지워진 수식들의 결괏값을 채워 넣어 순서대로 문자열 배열에 담아 반환하라.

<제한 사항>
2 ≤ expressions의 길이 ≤ 100
- expressions의 원소는 "A + B = C" 혹은 "A - B = C" 형태의 문자열이다. A, B, C와 연산 기호들은 공백 하나로 구분되어 있다.
- A, B는 음이 아닌 두 자릿수 이하의 정수이다.
- C는 알파벳 X 혹은 음이 아닌 세 자릿수 이하의 정수이다. C가 알파벳 X인 수식은 결괏값이 지워진 수식을 의미하며, 이러한 수식은 한 번 이상 등장한다.
- 결괏값이 음수가 되거나 서로 모순되는 수식은 주어지지 않다.

<풀이>
풀이 시간: 1시간 30분
1. 계산해야할 수식과 계산된 수식 분리
2. 가능한 진법 후보에 대해서만 계산된 수식으로 결과값이 정상적으로 나오는지 확인
3. 최종적으로 가능한 진법들로 모든 수식을 계산하고 결과값이 여러 개라면 ?로 표시, 동일하다면 해당 값으로 표시

<시간 복잡도>
O(n)
"""


def convert_to_decimal(base: int, num: str):
    """N진수 문자열을 10진수로 변환"""
    result = 0
    base_value = 1
    for digit in num[::-1]:
        result += int(digit) * base_value
        base_value *= base
    return result


def convert_to_base(result: int, n: int):
    """10진수를 N진수로 변환"""
    if result == 0:
        return "0"
    digits = ''
    while result > 0:
        result, mod = divmod(result, n)
        digits += str(mod)
    return digits[::-1]


def check_base(num, expression):
    a, oper, b, _, c = expression.split()
    trans_a = convert_to_decimal(num, a)
    trans_b = convert_to_decimal(num, b)
    result = trans_a + trans_b if oper == '+' else trans_a - trans_b

    if c != 'X':
        trans_c = convert_to_decimal(num, c)
        return result == trans_c
    else:
        return convert_to_base(result, num)


def solution(expressions: list) -> list:
    need_to_calculate = []
    having_result = []

    # 초기 최대 숫자를 위한 변수
    max_digit = 0
    # 결과값이 있는 수식과 값을 구해야 하는 수식 분리
    for expression in expressions:
        parts = expression.split()
        if parts[-1] == 'X': # 결과값이 없는 수식
            need_to_calculate.append(expression)
        else:
            having_result.append(expression)

        a, b, c = parts[0], parts[2], parts[-1]
        max_digit = max(max_digit, max(map(int, a)), max(map(int, b)), max(map(int, c)) if c != 'X' else 0)

    # 진법 후보를 max_digit + 1 ~ 9 범위로 제한된 리스트로 초기화
    min_base = max(2, max_digit + 1)
    possible_bases = range(min_base, 10)
    final_base = []
    # 가능한 진법에 대해서만 계산
    for base_value in possible_bases:
        for expression in having_result:
            # 결과값이 제대로 나오지 않으면 해당 진법으로 더 이상 수식 확인 x
            if not check_base(base_value, expression):
                break
        else:
            final_base.append(base_value)

    # 계산할 수식 계산
    answer = []
    for expression in need_to_calculate:
        result = set()
        for base in final_base:
            result.add(check_base(base, expression))
        if len(result) > 1:
            answer.append(expression.replace('X', '?'))
        else:
            answer.append(expression.replace('X', str(list(result)[0])))
    return answer