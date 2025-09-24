import java.util.*;

public class RoomAllocation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] intervals = new int[n][3]; // Stores (start, end, index)
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            intervals[i] = new int[]{a, b, i};
        }

        // Sort intervals based on start time
        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));

        int[] rooms = new int[n]; // Store assigned room numbers
        PriorityQueue<Integer> available = new PriorityQueue<>(); // Min-heap for available rooms
        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(o -> o[0])); // Min-heap (end_time, room)

        int maxRooms = 0;

        // Initialize available rooms
        for (int i = 1; i <= n; i++) {
            available.add(i);
        }

        for (int[] interval : intervals) {
            int a = interval[0], b = interval[1], index = interval[2];

            // Free up rooms that are no longer in use
            while (!queue.isEmpty() && queue.peek()[0] < a) {
                available.add(queue.poll()[1]);
            }

            // Allocate the smallest available room
            int alloc = available.poll();
            rooms[index] = alloc;

            // Store the new end time and room number
            queue.offer(new int[]{b, alloc});

            maxRooms = Math.max(maxRooms, queue.size());
        }

        System.out.println(maxRooms);
        for (int room : rooms) {
            System.out.print(room + " ");
        }
        System.out.println();
    }
}
