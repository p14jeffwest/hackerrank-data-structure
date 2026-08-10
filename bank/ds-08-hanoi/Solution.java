import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// The Tower of Hanoi of 8.2 item 3.
//
// The decomposition is the whole solution:
//   1. move the top n-1 disks out of the way, onto the auxiliary peg
//   2. move the largest disk to the target
//   3. move those n-1 disks from the auxiliary peg onto the target
//
// Steps 1 and 3 are the same problem with one fewer disk, and the roles of
// the three pegs rotate between them. Getting that rotation right is the
// only thing to get right: in step 1 the TARGET peg is the spare, and in
// step 3 the ORIGINAL peg is.
//
// M(n) = 2M(n-1) + 1 = 2^n - 1 moves, so n = 20 prints 1,048,575 lines. At
// that volume System.out.println per move is far too slow; the moves are
// gathered in a StringBuilder and written once.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    private static StringBuilder sb;

    static void hanoi(int n, char from, char to, char aux) {
        if (n == 0) return;                       // nothing left to move
        hanoi(n - 1, from, aux, to);              // 1) top n-1 to the auxiliary
        sb.append(from).append(" -> ").append(to).append('\n');   // 2) largest
        hanoi(n - 1, aux, to, from);              // 3) n-1 to the target
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        sb = new StringBuilder();
        sb.append((1 << n) - 1).append('\n');     // 2^n - 1
        hanoi(n, 'A', 'C', 'B');

        System.out.print(sb);
    }
}
