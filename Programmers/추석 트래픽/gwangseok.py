def solution(lines):
    starts, ends = [], []
    for line in lines:
        date, times, cost = line.split(" ")
        cost = float(cost[0:-1])
        
        hh, mm, ss = times.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        starts.append(seconds - cost + 0.001)
        ends.append(seconds + 1)
        
    starts.sort()

    cur_traffic = 0
    max_traffic = 0
    start_idx = end_idx = 0
    
    while start_idx < len(lines) and end_idx < len(lines):
        if(starts[start_idx] < ends[end_idx]):
            cur_traffic += 1
            max_traffic = max(max_traffic, cur_traffic)
            start_idx += 1
        else: ## it means that a line is over.
            cur_traffic -= 1
            end_idx += 1

    return max_traffic


""" /*

import java.util.*;

class Solution {
    public int solution(String[] lines) {
        // 9월 15일 데이터만 존재.
        // 처리 시간은 0.001 <= <= 3.000
        // lines는 응답 완료 시간임. 그리고 오름차순 정렬 되어 있다.
        List<Double> starts = new ArrayList<>();
        List<Double> ends = new ArrayList<>();
        int total_lines = lines.length;

        for (String line : lines) {
            String[] parts = line.split(" ");
            String time = parts[1];
            String cost = parts[2]; // 항상 s로 끝남

            double t = Double.parseDouble(cost.substring(0, cost.length() - 1));
            String[] timeParts = time.split(":");
            double hh = Double.parseDouble(timeParts[0]);
            double mm = Double.parseDouble(timeParts[1]);
            double ss = Double.parseDouble(timeParts[2]);

            double seconds = hh * 3600 + mm * 60 + ss;

            ends.add(seconds + 1);
            starts.add(seconds - t + 0.001);
        }

        Collections.sort(starts);

        int cur_traffic = 0;
        int max_traffic = 0;
        int start_idx = 0;
        int end_idx = 0;

        while ((start_idx < total_lines) & (end_idx < total_lines)) {
            if (starts.get(start_idx) < ends.get(end_idx)){
                cur_traffic++;
                max_traffic = Math.max(max_traffic, cur_traffic);
                start_idx++;
            }
            else {
                cur_traffic--;
                end_idx++;
            }
        }

        return max_traffic;
    }
}

*/ """
