#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> update_dp(int e) {
    vector<int> dp(e + 1, 0);    
    for (int step = 1; step <= e; ++step) {
        for (int i = step; i <= e; i += step) {
            dp[i] += 1;
        }
    }
    
    return dp;
}

vector<int> update_large_dp(vector<int> dp, int e, int min_s) {
    vector<int> large_dp(e + 1, 0);
    int max_frequency = -1;
    int max_idx = -1;
    for (int s = e; s >= min_s; --s) {
        if (max_frequency <= dp[s]) {
            max_frequency = dp[s];
            max_idx = s;
        }
        large_dp[s] = max_idx;
    }
    
    return large_dp;
}

vector<int> solution(int e, vector<int> starts) {
    vector<int> answer;
    vector<int> dp = update_dp(e);  // n * (1 + 1/2 + 1/3 + ... + 1/n) \approx O(NlogN)
    int min_s = *min_element(starts.begin(), starts.end());
    vector<int> large_dp = update_large_dp(dp, e, min_s); // O(N)
    
    for (int start : starts) {
        answer.push_back(large_dp[start]);
    }
    
    return answer;
}
