import java.io.*;
import java.util.*;

// NOTE: Comments must be written in English, and the whole file must stay
// plain ASCII.
//
// The card game of 7.5, Problem 4, run as a queue simulation.
//
// The rule maps onto a queue exactly: "discard the top card" is one dequeue,
// and "move the next one to the bottom" is a dequeue followed by an enqueue.
// Nothing else is needed.
//
// The point is which structure sits underneath. Removing from the front of an
// ArrayList shifts every remaining element, so the simulation becomes O(n^2)
// and cannot finish at n = 500,000. ArrayDeque removes from the front in O(1),
// which is what 7.3 explains: it is a circular array underneath.
//
// Output is gathered in a StringBuilder. There are n-1 discarded cards of up
// to ten digits, so the output reaches several megabytes.
//
// Verified with javac --release 15 -Xlint:all (no warnings).
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        Deque<Integer> deck = new ArrayDeque<>(n);
        StringTokenizer values = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            deck.addLast(Integer.parseInt(values.nextToken()));
        }

        StringBuilder sb = new StringBuilder();
        boolean first = true;

        while (deck.size() > 1) {
            int discarded = deck.pollFirst();       // 1. discard the top card
            if (!first) sb.append(' ');
            sb.append(discarded);
            first = false;

            deck.addLast(deck.pollFirst());         // 2. next card to the bottom
        }

        sb.append('\n').append(deck.pollFirst()).append('\n');
        System.out.print(sb);
    }
}
