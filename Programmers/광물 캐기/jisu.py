"""
start : 2024-05-02 11:00
end : 2024-05-02 11:39
"""

"""
- 다이아, 철, 돌은 각 5개씩이므로 모든 경우의 수는 15!
- 하지만 mineals는 50개까지만 주어지므로, 다이어, 철, 돌 곡괭이 순으로 최대 10개만 고려하면 된다. (모든 경우의 수는 10!이므로 완탐 가능)
    - 굳이 다이아 많은데 돌 곡괭이 쓸 필요 없음 (약간 그리디)
"""
import sys
from itertools import permutations
from typing import List


def solution(picks: List[int], minerals: List[str]) -> int:
    piro_dicts = [{'diamond': 1, 'iron': 1, 'stone': 1},  # 다이아 곡괭이 피로도
                  {'diamond': 5, 'iron': 1, 'stone': 1},  # 철 곡괭이 피로도
                  {'diamond': 25, 'iron': 5, 'stone': 1}]  # 돌 곡괭이 피로도

    # 다이아 > 철 > 곡괭이 순으로 최대 10개 뽑기
    picks_flatten = []
    for idx, pick in enumerate(picks):
        picks_flatten += [idx for _ in range(pick)]
    if len(picks_flatten) > 10:
        picks_flatten = picks_flatten[:10]

    visited = set()
    answer = sys.maxsize

    permutation = permutations(picks_flatten)       # 모든 경우의 수(최대 10!)

    # 곡괭이 집는 순서 완탐
    for permu in permutation:
        # 중복 고려
        if permu in visited:
            continue
        else:
            visited.add(permu)

        mineral_idx = 0
        tmp_answer = 0

        for pick in permu:
            for _ in range(5):
                # 미네랄 캐기
                mineral = minerals[mineral_idx]
                tmp_answer += piro_dicts[pick][mineral]     # 현재 곡괭이로 미네랄 캘 시 피로도
                mineral_idx += 1

                # 미네랄 다 캔 경우
                if mineral_idx == len(minerals):
                    break

            # 미네랄 다 캔 경우 다음 경우의 수로
            if mineral_idx == len(minerals):
                break

        # 최소 피로도 업데이트
        if tmp_answer < answer:
            answer = tmp_answer

    return answer
