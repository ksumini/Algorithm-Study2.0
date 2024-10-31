def NToTen(base, num_str):
    # 주어진 문자열 num_str을 base 진법에서 10진수로 변환
    if len(num_str) == 1:
        return int(num_str)

    number = 0
    for idx, digit in enumerate(num_str):
        number += int(digit) * (base ** (len(num_str) - 1 - idx))

    return number


def TenToN(base, num):
    # 10진수 num을 base 진법으로 변환하여 문자열로 반환
    if num == 0:
        return "0"

    answer = ""
    for idx in range(2, -1, -1):
        div = num // (base ** idx)
        if answer or div:  # answer가 비어 있지 않거나 div가 0이 아닌 경우에만 추가
            answer += str(div)
        num %= (base ** idx)

    return answer


def solution(expressions):
    answer, unknown_expressions = [], []
    max_digit, hints = 0, []

    # 힌트 수식과 미지의 수식을 분류하고, 최대 자리수 찾기
    for expression in expressions:
        num1, op, num2, _, result = expression.split(" ")

        # 최대 자리수 갱신
        max_digit = max(max_digit, *map(int, num1 + num2 + (result if result != 'X' else "")))

        # 힌트와 미지의 수식 분류
        if result == "X":
            unknown_expressions.append(expression)
        else:
            hints.append(expression)

    # 가능한 진법 찾기
    valid_bases = []
    for base in range(max_digit + 1, 10):
        valid = True
        for hint in hints:
            num1, op, num2, _, result = hint.split(" ")
            n1, n2, r = NToTen(base, num1), NToTen(base, num2), NToTen(base, result)

            # 수식 검증
            if (op == '+' and n1 + n2 != r) or (op == '-' and n1 - n2 != r):
                valid = False
                break

        if valid:
            valid_bases.append(base)

    # 미지의 수식에 대한 결괏값 채우기
    for expression in unknown_expressions:
        num1, op, num2, _, result = expression.split(" ")
        possible_results = set()

        # 각 가능한 진법에서 결과를 계산하여 집합에 추가
        for base in valid_bases:
            n1, n2 = NToTen(base, num1), NToTen(base, num2)
            if op == "+":
                res = n1 + n2
            elif op == "-":
                res = n1 - n2
            possible_results.add(TenToN(base, res))

        # 결과가 유일하면 추가하고, 그렇지 않으면 "?"
        if len(possible_results) == 1:
            answer.append(f"{num1} {op} {num2} = {possible_results.pop()}")
        else:
            answer.append(f"{num1} {op} {num2} = ?")

    return answer
