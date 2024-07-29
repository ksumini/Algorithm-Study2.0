# O(4 ** m (m + n * m)) = 2^14 * (7 + 700) \approx 16000 * (707) < 16000000

def get_cur_answer(users, emoticons, sales):
    answer = [0, 0]
    for user in users:  # O(n)
        consume = 0
        for idx, price in enumerate(emoticons):  # O(m)
            if user[0] <= sales[idx]:
                consume += int(price * (100 - sales[idx]) / 100)  
                # int(price * (1 - sales[idx] / 100))
                # round(price * (1 - sales[idx] / 100), 0)
                
        if consume < user[1]:
            answer[1] += consume
        else:
            answer[0] += 1
    return answer


def solution(users, emoticons):
    supremum = 4 ** len(emoticons)
    # 완전 탐색을 하면서 bit mask를 활용한다.
    # 이때, 0은 10%, ..., 3은 40%를 의미한다.
    sale_dict={
        0: 10,
        1: 20,
        2: 30,
        3: 40
    }
    
    answer = [-1, -1]
    for bit_mask in range(supremum):  # O(4^m)
        cur_sale = []
        for i in range(len(emoticons)):  # O(m)
            sale_idx = (bit_mask) & 3
            cur_sale.append(sale_dict[sale_idx])
            bit_mask >>= 2
        
        cur_answer = get_cur_answer(users, emoticons, cur_sale)  # O(n * m)
        answer = max(answer, cur_answer)
    
    return answer
