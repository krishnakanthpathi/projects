#include <bits/stdc++.h>
using namespace std;

signed main() {
    int n;
    cin >> n;
    vector<vector<int>> a(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> a[i][0] >> a[i][1];
    }

    sort(a.begin(), a.end(), [&](const vector<int> x, const vector<int> y) {
        if (x[1] != y[1])
            return x[1] < y[1];
        return x[0] < y[0];
    });

    int res = 1;
    for (int i = 0; i < n; i++) {
        int l = -1, r = i;
        while (r - l > 1) {
            int mid = (l + r) / 2;
            if (a[mid][1] >= a[i][0])
                r = mid;
            else
                l = mid;
        }
        res = max(res, i - r + 1);
    }

    cout << res << endl;
 
    return 0;
}