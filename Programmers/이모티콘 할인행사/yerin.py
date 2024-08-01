'''액
<우선순위>
가입자 수
판매액

10, 20, 30, 40%
'''

def solution(users, emoticons):
    # 최종 답안을 저장할 리스트 초기화: [최대 가입자 수, 총 판매액]
    answer = [0, 0]
    # 모든 가능한 할인 조합을 저장할 리스트
    sales = []
    # 사용할 할인율 목록
    percentage = [10, 20, 30, 40]

    # 가능한 모든 할인 조합을 생성하는 재귀 함수
    def set_percentage_per_emoticons(arr, depth):
        # 만약 깊이가 이모티콘의 개수와 같다면, 완성된 할인 조합을 저장
        if depth == len(emoticons):
            sales.append(arr[:])
            return

        # 각 가능한 할인율에 대해 반복
        for pct in percentage:
            arr.append(pct)
            set_percentage_per_emoticons(arr, depth + 1)
            arr.pop()

    set_percentage_per_emoticons([], 0)

    for i in range(len(sales)):
        join_users = 0  # 현재 할인 조합에서의 가입자 수
        total_profit = 0  # 현재 할인 조합에서의 총 판매액

        for pct_limit, max_total_price in users:
            price = 0  # 현재 사용자가 지불할 총 가격
            for j in range(len(emoticons)):
                # 사용자가 설정한 할인율 제한보다 현재 할인율이 크거나 같다면
                if pct_limit <= sales[i][j]:
                    price += emoticons[j] * (100 - sales[i][j]) * 0.01

            if price >= max_total_price:
                join_users += 1
            else:
                total_profit += price

        # 현재 할인 조합이 더 많은 가입자를 유도한다면 답안 업데이트
        if answer[0] < join_users:
            answer = [join_users, int(total_profit)]
        # 가입자 수가 동일하다면 총 판매액이 더 높은 경우에 답안 업데이트
        elif answer[0] == join_users and answer[1] < total_profit:
            answer = [join_users, int(total_profit)]

    return answer
