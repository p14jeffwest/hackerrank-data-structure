import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII. Depending on the compiler's default encoding, a non-ASCII
// character can break compilation with an "unmappable character" error.
//
// NOTE: The class must be named Solution.
//
// Reads N integers and prints their sum.
// Uses BufferedReader + StringTokenizer, following appendix C.5 item 4.
//
// IMPORTANT: the sum reaches 1e14, which overflows int (max ~2.1e9), so the
// accumulator must be long. Each individual value still fits in int, which is
// exactly the distinction the statement asks the student to notice.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());

        long sum = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(st.nextToken());
        }

        System.out.println(sum);
    }
}
