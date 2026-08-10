import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// The queue simulation of 7.6, Problem 1.
//
// The rule itself maps straight onto a queue: take the front, and either send
// it to the back or run it. What costs is the test in the middle -- "is any
// waiting process more important than this one?"
//
// Asking that by walking the queue is O(n) per step. The number of steps is
// already quadratic in the worst case (with priorities 1, 2, ..., n the queue
// turns over n times), so walking it as well makes the whole thing O(n^3) and
// it does not finish at n = 1000.
//
// Instead, note that the processes still in the queue are exactly the ones
// not yet run. So sort the priorities in descending order once, and keep a
// pointer: sorted[p] is the highest priority still waiting, and it advances by
// exactly one every time a process runs. The test becomes a comparison.
//
// Note that the comparison is strict. Equal priorities do not displace each
// other -- if they did, a queue of identical priorities would circulate for
// ever.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            StringTokenizer header = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(header.nextToken());
            int target = Integer.parseInt(header.nextToken());

            int[] priority = new int[n];
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                priority[i] = Integer.parseInt(values.nextToken());
            }

            // the highest priority still waiting, read off in order
            int[] sorted = priority.clone();
            Arrays.sort(sorted);                       // ascending, so walk it backwards

            Deque<Integer> queue = new ArrayDeque<>(n);
            for (int i = 0; i < n; i++) queue.addLast(i);   // store original indices

            int remaining = n - 1;                     // index into `sorted` from the top
            int order = 0;
            int answer = -1;

            while (!queue.isEmpty()) {
                int current = queue.pollFirst();
                if (priority[current] < sorted[remaining]) {
                    queue.addLast(current);            // something better is waiting
                } else {
                    order++;
                    remaining--;
                    if (current == target) {
                        answer = order;
                        break;
                    }
                }
            }

            sb.append(answer).append('\n');
        }

        System.out.print(sb);
    }
}
