#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<tuple<int, int, int>> intervals(n);
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        intervals[i] = {a, b, i};
    }

    sort(intervals.begin(), intervals.end());  // Sort by start time

    vector<int> rooms(n);  // Store assigned room numbers
    priority_queue<int, vector<int>, greater<int>> available;  // Min-heap for available rooms
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> queue;  // Min-heap (end_time, room)

    // Initialize available rooms
    for (int i = 1; i <= n; i++) {
        available.push(i);
    }

    int max_rooms = 0;

    for (auto &[a, b, index] : intervals) {
        // Free up rooms that are no longer in use
        while (!queue.empty() && queue.top().first < a) {
            available.push(queue.top().second);
            queue.pop();
        }

        // Allocate the smallest available room
        int alloc = available.top();
        available.pop();
        rooms[index] = alloc;

        // Store the new end time and room number
        queue.emplace(b, alloc);
        
        max_rooms = max(max_rooms, (int)queue.size());
    }

    cout << max_rooms << "\n";
    for (int i = 0; i < n; i++) {
        cout << rooms[i] << " ";
    }
    cout << "\n";

    return 0;
}
