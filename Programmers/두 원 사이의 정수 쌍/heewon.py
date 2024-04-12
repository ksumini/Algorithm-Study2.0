'''
## 접근 방식
- 1사분면 + x축(x>0) 의 점의 개수를 구하고 X 4를 하자!
    - x축의 점의 개수
        $$r_2 - r_1 + 1$$
    - x값이 0 ~ r1 까지
        $$
        \left\lfloor\sqrt{r_2^2 - x^2}\right\rfloor - \left\lceil\sqrt{r_1^2 - x^2}\right\rceil + 1
        $$
    - x값이 r1 ~ r2 까지
        $$
        \left\lfloor\sqrt{r_2^2 - x^2}\right\rfloor
        $$

## 사용한 모듈
`math`

## 추가 정보
- 시간: 1 hour 이하
- 힌트: `None`
### 1st

<html>
<body>
<!--StartFragment--><pre class="console-content" style="box-sizing: border-box; padding: 0px; margin: 0px 0px 1.3125rem; color: white; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-variant-alternates: inherit; font-variant-position: inherit; font-weight: 400; font-stretch: inherit; font-size: 14px; line-height: inherit; font-family: Hack, Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace, &quot;맑은 고딕&quot;, &quot;malgun gothic&quot;, 돋움, Dotum, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: auto; display: block; border: none; background-color: rgb(38, 55, 71); border-radius: 0px; word-break: break-all; overflow-wrap: break-word; white-space: pre-wrap; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="console-heading" style="box-sizing: border-box; padding: 0px; margin: 1.5rem 0px 0.5rem; color: rgb(152, 168, 185); font: inherit;">채점을 시작합니다.</div><div class="console-message" style="box-sizing: border-box; padding: 0px; margin: 0.25rem 0px; color: rgb(95, 127, 144); font: inherit;">정확성  테스트</div>

정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 9.98MB)
테스트 4 〉	통과 (1.41ms, 10.1MB)
테스트 5 〉	통과 (0.46ms, 10.2MB)
테스트 6 〉	통과 (1.12ms, 10.1MB)
테스트 7 〉	통과 (307.98ms, 10.3MB)
테스트 8 〉	통과 (631.76ms, 10.4MB)
테스트 9 〉	통과 (316.38ms, 10.3MB)
테스트 10 〉	통과 (487.56ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0

<div class="console-heading" style="box-sizing: border-box; padding: 0px; margin: 1.5rem 0px 0.5rem; color: rgb(152, 168, 185); font: inherit;">채점 결과</div><div class="console-message" style="box-sizing: border-box; padding: 0px; margin: 0.25rem 0px; color: rgb(95, 127, 144); font: inherit;">정확성: 100.0</div><div class="console-message" style="box-sizing: border-box; padding: 0px; margin: 0.25rem 0px; color: rgb(95, 127, 144); font: inherit;">합계: 100.0 / 100.0</div></pre><!--EndFragment-->
</body>
</html>


### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- #43
'''

import math

def solution(r1, r2):
    answer = 0
    # x축의 점의 개수
    answer += (r2 - r1 + 1)
    for x in range(1, r2):
        # x값이 0 ~ r1 까지
        if x < r1:
            answer += math.floor(pow(r2*r2-x*x,0.5)) - math.ceil(pow(r1*r1-x*x,0.5)) + 1
        # x값이 r1 ~ r2 까지
        else:
            answer += math.floor(pow(r2*r2-x*x,0.5))
    return answer * 4 # 4배 하기