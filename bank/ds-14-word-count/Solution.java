import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// One pass over the list records how many times each word appeared. After
// that every query is one lookup instead of a scan.
//
// Scanning the list per query would be O(N*Q), which at 200,000 of each is
// 4 * 10^10 and does not finish. A HashMap turns each query into average
// O(1), so the whole thing is O(N + Q).
//
// getOrDefault is what handles a word that never appeared: get() would return
// null and unboxing it would throw.
//
// merge(word, 1, Integer::sum) is the short way to write "add one, starting
// from zero if this is the first time".
//
// The input is large, so it is read with StreamTokenizer in word mode rather
// than split into tokens by hand.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));
        in.ordinaryChars(0, 255);
        in.wordChars('a', 'z');
        in.wordChars('0', '9');
        in.whitespaceChars(0, ' ');

        int n = nextInt(in);
        Map<String, Integer> count = new HashMap<>();
        for (int i = 0; i < n; i++) {
            count.merge(nextWord(in), 1, Integer::sum);
        }

        int q = nextInt(in);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            sb.append(count.getOrDefault(nextWord(in), 0)).append('\n');
        }

        System.out.print(sb);
    }

    private static String nextWord(StreamTokenizer in) throws IOException {
        in.nextToken();
        return in.sval;
    }

    private static int nextInt(StreamTokenizer in) throws IOException {
        in.nextToken();
        return Integer.parseInt(in.sval);
    }
}
