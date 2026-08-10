import java.io.*;
import java.util.*;

class MedianFinder {

    // The smaller half, largest of them on top.
    protected final PriorityQueue<Integer> lower =
            new PriorityQueue<>(Collections.reverseOrder());

    // The larger half, smallest of them on top.
    protected final PriorityQueue<Integer> upper = new PriorityQueue<>();

    public int size() { return lower.size() + upper.size(); }

    // Two heaps facing each other. `lower` holds the smaller half with its
    // largest on top; `upper` holds the larger half with its smallest on top.
    // Keep them within one of each other in size, and the middle of the
    // stream is always sitting at one of those two tops.
    //
    // addNum: push into `lower` first, then move its top across to `upper`.
    //   That single move is what enforces the ordering -- whatever the new
    //   value was, the largest of the smaller half ends up on the correct
    //   side. Then, if `upper` has grown larger, move its top back.
    //
    //   Testing "x <= lower.peek()" to choose a side directly works too, but
    //   needs a separate case for the first value. Passing every value
    //   through `lower` avoids that.
    //
    // findMedian: with an odd count `lower` holds the extra element, so its
    //   top IS the median. With an even count the two middles are the two
    //   tops.
    //
    // The sum of two ints can reach 2 * 10^9, so it is taken as a double
    // before halving rather than after.
    //
    // O(log n) per add, O(1) per median.

    public void addNum(int x) {
        lower.offer(x);
        upper.offer(lower.poll());
        if (upper.size() > lower.size()) {
            lower.offer(upper.poll());
        }
    }

    public double findMedian() {
        if (lower.size() > upper.size()) return lower.peek();
        return (lower.peek() + (double) upper.peek()) / 2.0;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine().trim());

        MedianFinder mf = new MedianFinder();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            if (op.equals("add")) {
                mf.addNum(Integer.parseInt(t.nextToken()));
            } else if (op.equals("median")) {
                if (mf.size() == 0) {
                    sb.append("empty").append('\n');
                } else {
                    sb.append(String.format(Locale.ROOT, "%.1f", mf.findMedian()))
                      .append('\n');
                }
            } else if (op.equals("size")) {
                sb.append(mf.size()).append('\n');
            }
        }

        System.out.print(sb);
    }
}
