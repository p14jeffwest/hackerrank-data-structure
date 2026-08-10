import java.io.*;
import java.util.*;

public class Solution {

    // Sort by start time and walk through the meetings in order. The heap
    // holds the END times of the meetings currently using a room, smallest
    // first, so its root is the room that frees up soonest.
    //
    // For each meeting: if that soonest room has already finished -- its end
    // time is at most this meeting's start -- reuse it by taking it out.
    // Then put this meeting's end in. The heap therefore grows only when no
    // existing room could be reused, and its final size is the number of
    // rooms that were ever needed at once.
    //
    // Note the comparison is <=, not <. A meeting ending exactly when
    // another starts does not overlap it, and using < would ask for an extra
    // room every time two meetings meet end to start.
    //
    // O(n log n): the sort, plus n heap operations.

    static int minMeetingRooms(int[][] meetings) {
        if (meetings.length == 0) return 0;

        Arrays.sort(meetings, Comparator.comparingInt(m -> m[0]));

        PriorityQueue<Integer> endTimes = new PriorityQueue<>();
        for (int[] meeting : meetings) {
            int start = meeting[0], end = meeting[1];
            if (!endTimes.isEmpty() && endTimes.peek() <= start) {
                endTimes.poll();                 // that room is free again
            }
            endTimes.offer(end);
        }
        return endTimes.size();
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int t = (int) in.nval;

        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            in.nextToken();
            int n = (int) in.nval;
            int[][] meetings = new int[n][2];
            for (int i = 0; i < n; i++) {
                in.nextToken();
                meetings[i][0] = (int) in.nval;
                in.nextToken();
                meetings[i][1] = (int) in.nval;
            }
            sb.append(minMeetingRooms(meetings)).append('\n');
        }

        System.out.print(sb);
    }
}
