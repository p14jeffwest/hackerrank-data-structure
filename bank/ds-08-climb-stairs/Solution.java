import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// 8.5, Problem 1.
//
// The last move onto step n is either a single step from n-1 or a double
// step from n-2, and those two sets of routes share nothing. So
//
//     ways(n) = ways(n-1) + ways(n-2),   ways(1) = 1, ways(2) = 2
//
// which is Fibonacci shifted by one. Note the base cases: ways(2) is 2, not
// 1, because 1+1 and 2 are different routes.
//
// Writing that recurrence as a plain recursion costs O(2^n), for the reason
// 8.2 item 4 gives -- the same subproblem is solved over and over. The table
// below fills each value once, in order, so the whole table is O(n) and each
// query is then a lookup.
//
// IMPORTANT: the counts must be held in long. ways(45) is 1,836,311,903 and
// still fits in an int; ways(46) is 2,971,215,073 and does not. ways(90)
// reaches 4.66 * 10^18, which is inside long's range but not by much.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    private static final int NMAX = 90;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] ways = new long[NMAX + 1];
        ways[1] = 1;
        ways[2] = 2;
        for (int i = 3; i <= NMAX; i++) {
            ways[i] = ways[i - 1] + ways[i - 2];
        }

        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine().trim());
            sb.append(ways[n]).append('\n');
        }

        System.out.print(sb);
    }
}
