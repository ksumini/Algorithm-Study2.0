def solution(expressions):
    answer = []
    max_num = 0
    knows = []
    unknowns = []
    
    # 진법 계산을 위한 기본 함수 정의
    def n_notation(number, base):
        return int(number, base)

    def ten_to_n(num, n):
        if num == 0: return "0"
        num_n = ''
        while num:
            num, r = divmod(num, n)
            num_n += str(r)
        return num_n[::-1]

    def get_min_n(num1, num2, num3 = '0'):
        return int(max(num1+num2+num3)) + 1

    # 수식 분류 및 진법 범위 설정
    for expression in expressions:
        op = '+' if '+' in expression else '-'
        num1, num2, num3 = expression.replace('+', '').replace('=', '').replace('-', '').split()
        
        if num3 != 'X':
            knows.append((op, num1, num2, num3))
            max_num = max(max_num, get_min_n(num1, num2, num3))
        else:
            unknowns.append((op, num1, num2))
            max_num = max(max_num, get_min_n(num1, num2))

    # 가능한 최대 진법의 범위를 설정
    n_check = set(range(max_num, 10))

    # 알려진 수식을 이용하여 가능한 진법 검증
    for op, num1, num2, num3 in knows:
        removes = set()
        for i in n_check:
            if op == '+' and n_notation(num1, i) + n_notation(num2, i) != n_notation(num3, i):
                removes.add(i)
            elif op == '-' and n_notation(num1, i) - n_notation(num2, i) != n_notation(num3, i):
                removes.add(i)
        n_check -= removes

    # 미지의 수식을 이용하여 X의 값을 계산하고 수식을 완성
    for op, num1, num2 in unknowns:
        num3 = '?'
        for j in n_check:
            result = ten_to_n(n_notation(num1, j) + n_notation(num2, j), j) if op == '+' else ten_to_n(n_notation(num1, j) - n_notation(num2, j), j)
            if num3 == '?':
                num3 = result
            elif num3 != result:
                num3 = "?"
                break
        answer.append(f"{num1} {op} {num2} = {num3}")

    return answer