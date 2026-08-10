import java.io.*;
import java.util.*;

public class Solution {

    // Euclid's algorithm, written exactly as the property reads:
    //
    //     gcd(a, b) = gcd(b, a mod b),   gcd(a, 0) = a
    //
    // The base case is b == 0. When the remainder reaches zero the previous
    // divisor is the answer, so `a` is returned unchanged.
    //
    // The swap looks after itself. If a < b on the first call, then
    // a % b == a, so the next call is gcd(b, a) with the two the other way
    // round. One wasted step, no special case needed.
    //
    // This is tail recursion (8.3): the recursive call is the whole of the
    // return expression, so nothing is left to do after it comes back and the
    // method converts to a loop by hand in one step.
    //
    // The depth is O(log(min(a, b))) by Lame's theorem -- the worst pairs are
    // consecutive Fibonacci numbers, and even there it stays around 45 for
    // values up to 10^9.

    static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int t = (int) in.nval;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            int a = (int) in.nval;
            in.nextToken();
            int b = (int) in.nval;
            sb.append(gcd(a, b)).append('\n');
        }

        System.out.print(sb);
    }
}
