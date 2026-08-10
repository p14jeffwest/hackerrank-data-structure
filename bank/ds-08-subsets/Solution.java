import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// 8.5, Problem 2: every subset of a set, generated recursively.
//
// The book branches "leave the current element out / put it in" at each
// index. This version takes the equivalent shape that produces the required
// order directly: emit whatever has been chosen so far, then extend it with
// each remaining element in turn.
//
//   dfs(start): emit current
//               for i from start to n-1:
//                   choose a[i], dfs(i + 1), unchoose a[i]
//
// With the input sorted first, the subsets come out in exactly the order the
// problem asks for, so nothing has to be sorted afterwards. Walking the
// indices upward is what guarantees it: everything beginning with a[i] is
// finished before anything beginning with a[i+1] starts.
//
// The unchoose step -- removing the element after the recursive call returns
// -- is what backtracking means. Without it the chosen list keeps growing and
// every later subset is wrong.
//
// Subsets are written straight into the StringBuilder rather than collected
// into a list of lists. That sidesteps the copying problem the book warns
// about: a saved reference to `chosen` would keep changing underneath.
//
// O(n * 2^n): 2^n subsets, each up to n numbers long.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    private static int[] a;
    private static int[] chosen;
    private static int depth;
    private static StringBuilder sb;

    static void dfs(int start) {
        emit();
        for (int i = start; i < a.length; i++) {
            chosen[depth++] = a[i];      // choose
            dfs(i + 1);
            depth--;                     // unchoose
        }
    }

    private static void emit() {
        if (depth == 0) {
            sb.append("(empty)").append('\n');
            return;
        }
        for (int i = 0; i < depth; i++) {
            if (i > 0) sb.append(' ');
            sb.append(chosen[i]);
        }
        sb.append('\n');
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        sb = new StringBuilder();

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            a = new int[n];
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(values.nextToken());
            }
            Arrays.sort(a);              // the input arrives in no order

            chosen = new int[n];
            depth = 0;
            dfs(0);
        }

        System.out.print(sb);
    }
}
