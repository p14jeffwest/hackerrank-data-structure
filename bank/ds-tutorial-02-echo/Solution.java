import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII. Depending on the compiler's default encoding, a non-ASCII
// character can break compilation with an "unmappable character" error.
//
// NOTE: The class must be named Solution.
// Using "public class Main", as the course material does, fails to compile.
//
// Reads a single line and echoes it back.
// Uses Scanner, following the tutorial's intended approach.
//
// The intended wrong answer is Scanner.next(), which stops at the first
// space and therefore passes only the single-token cases.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        System.out.println(line);
    }
}
