import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// Reports what an array-based list would spend on a sequence of operations:
// elements moved by shifting, elements copied by growth, and final capacity.
//
// The idea is that none of this depends on the values stored. Every quantity
// asked for is a function of the current size and the current capacity alone,
// so no array is ever allocated and each operation costs O(1).
//
// IMPORTANT: with 200,000 insertions at the front, the move count reaches
// about 2 * 10^10, which overflows int. It must be accumulated in a long.
// Capacity stays small -- doubling from at most 1000 reaches 200,000 in
// eighteen steps -- but it is kept as a long as well so that the comparison
// with size cannot surprise anyone.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            StringTokenizer header = new StringTokenizer(br.readLine());
            long capacity = Long.parseLong(header.nextToken());
            int q = Integer.parseInt(header.nextToken());

            long size = 0;
            long moves = 0;
            long copies = 0;

            for (int j = 0; j < q; j++) {
                StringTokenizer line = new StringTokenizer(br.readLine());
                String op = line.nextToken();

                if (op.equals("add")) {
                    if (size == capacity) {          // grow before storing
                        copies += capacity;
                        capacity *= 2;
                    }
                    size++;
                } else if (op.equals("addAt")) {
                    long position = Long.parseLong(line.nextToken());
                    if (size == capacity) {          // grow before shifting
                        copies += capacity;
                        capacity *= 2;
                    }
                    moves += size - position;
                    size++;
                } else {                             // removeAt
                    long position = Long.parseLong(line.nextToken());
                    moves += size - 1 - position;
                    size--;
                }
            }

            sb.append(moves).append(' ')
              .append(copies).append(' ')
              .append(capacity).append('\n');
        }

        System.out.print(sb);
    }
}
