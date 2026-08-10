import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// Evaluates postfix expressions with a stack, following 6.2 item 2.
//
// Two details carry the problem.
//
//   1. The pop order. When an operator arrives, the FIRST value popped is the
//      right operand and the second is the left. Getting it backwards is
//      invisible for + and *, and wrong every time for - and /.
//
//   2. Telling the operator "-" from a negative literal like "-11". A token
//      is an operator only when it is exactly one character long; checking
//      whether the first character is '-' misreads every negative number.
//
// Java's integer division truncates toward zero, so -7 / 2 is -3, not -4.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    private static boolean isOperator(String token) {
        return token.length() == 1 && "+-*/".indexOf(token.charAt(0)) >= 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();
        Deque<Integer> stack = new ArrayDeque<>();

        while (t-- > 0) {
            stack.clear();
            StringTokenizer tokens = new StringTokenizer(br.readLine());

            while (tokens.hasMoreTokens()) {
                String token = tokens.nextToken();
                if (isOperator(token)) {
                    int b = stack.pop();          // right operand
                    int a = stack.pop();          // left operand
                    switch (token.charAt(0)) {
                        case '+': stack.push(a + b); break;
                        case '-': stack.push(a - b); break;
                        case '*': stack.push(a * b); break;
                        default : stack.push(a / b); break;
                    }
                } else {
                    stack.push(Integer.parseInt(token));
                }
            }

            sb.append(stack.pop()).append('\n');
        }

        System.out.print(sb);
    }
}
