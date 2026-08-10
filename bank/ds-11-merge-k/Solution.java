import java.io.*;
import java.util.*;

public class Solution {

    // Only the current front of each list can be the next smallest, so the
    // heap never needs to hold more than k entries -- one candidate per list.
    // Take the smallest out, write it down, and put in the next element of
    // whichever list it came from.
    //
    // Each entry carries {value, list index, position in that list}, because
    // the value alone does not say where to look for its successor.
    //
    // O(N log k): every one of the N values enters and leaves a heap of size
    // at most k. Scanning all k fronts at each step instead is O(N * k),
    // which at k = 100,000 does not finish.
    //
    // Empty lists must not be offered at all, or the first poll reads a
    // position that does not exist.

    static int[] mergeKLists(int[][] lists) {
        int total = 0;
        for (int[] list : lists) total += list.length;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (int i = 0; i < lists.length; i++) {
            if (lists[i].length > 0) {
                pq.offer(new int[]{lists[i][0], i, 0});
            }
        }

        int[] result = new int[total];
        int at = 0;
        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            int value = top[0], listIdx = top[1], elemIdx = top[2];
            result[at++] = value;
            if (elemIdx + 1 < lists[listIdx].length) {
                pq.offer(new int[]{lists[listIdx][elemIdx + 1], listIdx, elemIdx + 1});
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int k = (int) in.nval;

        int[][] lists = new int[k][];
        for (int i = 0; i < k; i++) {
            in.nextToken();
            int n = (int) in.nval;
            lists[i] = new int[n];
            for (int j = 0; j < n; j++) {
                in.nextToken();
                lists[i][j] = (int) in.nval;
            }
        }

        int[] merged = mergeKLists(lists);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < merged.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(merged[i]);
        }
        sb.append('\n');

        System.out.print(sb);
    }
}
