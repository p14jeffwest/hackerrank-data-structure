import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// The monotonic deque of 7.5, Level 3.
//
// The deque holds INDICES, never values, and the values at those indices
// decrease from front to rear. Two rules keep it that way:
//
//   from the front: drop indices that have fallen out of the window
//   from the rear:  drop indices whose value the new element beats, since
//                   they can never be the maximum again while it is present
//
// After both, the front is the index of the current window's maximum.
//
// Indices rather than values, because expiry is a question about position.
// A deque of values cannot tell whether its front has left the window.
//
// O(n): every index is offered once and polled at most once, so the two inner
// while loops run at most n times in total across the whole pass.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();
        Deque<Integer> window = new ArrayDeque<>();

        while (t-- > 0) {
            StringTokenizer header = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(header.nextToken());
            int k = Integer.parseInt(header.nextToken());

            int[] nums = new int[n];
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                nums[i] = Integer.parseInt(values.nextToken());
            }

            window.clear();
            boolean first = true;

            for (int i = 0; i < n; i++) {
                // 1. drop indices that have left the window
                while (!window.isEmpty() && window.peekFirst() < i - k + 1) {
                    window.pollFirst();
                }
                // 2. drop indices the new element beats, keeping the order
                while (!window.isEmpty() && nums[window.peekLast()] <= nums[i]) {
                    window.pollLast();
                }
                window.offerLast(i);

                // 3. once the window is complete, its maximum is at the front
                if (i >= k - 1) {
                    if (!first) sb.append(' ');
                    sb.append(nums[window.peekFirst()]);
                    first = false;
                }
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }
}
