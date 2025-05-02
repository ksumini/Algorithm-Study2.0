def solution(n, tops):
    answer = 0
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    a[0], b[0] = 0, 1

    for i, t in enumerate(tops):
        a[i + 1] = a[i] + b[i]
        if t:
            b[i+1] = 2 * a[i] + 3 * b[i]
        else:
            b[i+1] = a[i] + 2 * b[i]

    answer = (a[-1] + b[-1]) % 10007

    return answer