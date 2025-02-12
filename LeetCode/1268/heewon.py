# 정규표현식
import re
from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answer = []
        products.sort()
        for i in range(len(searchWord)):
            q = re.compile(searchWord[:i+1])
            a = []
            for product in products:
                if q.match(product):
                    a.append(product)
                if len(a) == 3:
                    break
            answer.append(a)
        return answer
    
# 내장 함수
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answer = []
        products.sort()
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            a = []
            for product in products:
                if product.startswith(prefix):
                    a.append(product)
                if len(a) == 3:
                    break
            answer.append(a)
        return answer