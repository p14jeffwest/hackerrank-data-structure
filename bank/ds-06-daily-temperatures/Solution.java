import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// The monotonic stack of 6.7, Problem 2.
//
// The stack holds INDICES of days that are still waiting for a warmer one,
// and their temperatures decrease from the bottom up. When a warmer day
// arrives it settles every waiting day it beats, and the distance is just the
// difference of the two indices.
//
// The comparison is strictly greater. A day of the same temperature is not
// warmer, so an equal reading must leave the waiting day on the stack.
//
// O(n): each index is pushed once and popped at most once, so the inner
// while loop runs at most n times over the whole pass even though it can run
// many times in one iteration.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();
        Deque<Integer> stack = new ArrayDeque<>();

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());

            int[] temperature = new int[n];
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                temperature[i] = Integer.parseInt(values.nextToken());
            }

            int[] answer = new int[n];        // 0 by default: no warmer day
            stack.clear();

            for (int i = 0; i < n; i++) {
                while (!stack.isEmpty() && temperature[i] > temperature[stack.peek()]) {
                    int waiting = stack.pop();
                    answer[waiting] = i - waiting;
                }
                stack.push(i);
            }

            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(answer[i]);
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }
}
