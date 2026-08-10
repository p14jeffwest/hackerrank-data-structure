import java.io.*;
import java.util.*;

public class Solution {

    // Write the method below.
    //
    //   minMeetingRooms(meetings) : the smallest number of rooms that holds
    //                               every meeting.
    //
    // meetings[i] is {start, end}. The order they arrive in is not fixed, and
    // you may rearrange the array.
    //
    // A meeting ending exactly when another starts does NOT overlap it; the
    // same room takes both.

    static int minMeetingRooms(int[][] meetings) {
        // TODO
        return 0;
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
