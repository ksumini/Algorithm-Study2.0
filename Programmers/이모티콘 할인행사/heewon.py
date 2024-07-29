from itertools import product

def solution(users, emoticons):
    answer = [0, 0]  # [플러스 가입자 수, 판매액]
    discount = [40, 30, 20, 10]  # 할인율 리스트
    E = len(emoticons)  # 총 이모티콘 개수

    # 모든 가능한 할인율 경우 생성(중복 순열)
    for case in product(discount, repeat=E):
        plus, total_cost = 0, 0  # 플러스 가입자 수, 판매액
        for ratio, limit in users:
            cost = 0
            for idx in range(E):
                if ratio <= case[idx]:  # 할인율이 허용 비율보다 크거나 같을 때
                    cost += emoticons[idx] * (100 - case[idx]) / 100
                if cost >= limit:  # 가격 한도를 초과하면
                    plus += 1
                    break
            else:  # 가격 한도를 초과하지 않으면
                total_cost += cost
        answer = max(answer, [plus, total_cost])

    return answer
