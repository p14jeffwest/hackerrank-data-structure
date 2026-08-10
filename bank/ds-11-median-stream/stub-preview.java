import java.io.*;
import java.util.*;

class MedianFinder {

    // The smaller half, largest of them on top.
    protected final PriorityQueue<Integer> lower =
            new PriorityQueue<>(Collections.reverseOrder());

    // The larger half, smallest of them on top.
    protected final PriorityQueue<Integer> upper = new PriorityQueue<>();

    public int size() { return lower.size() + upper.size(); }

    // Write the two methods below.
    //
    //   addNum(x)     : take one more number from the stream.
    //   findMedian()  : the median of everything taken so far.
    //
    // Keep the two halves as halves: every value in `lower` must be at most
    // every value in `upper`, and their sizes must never differ by more than
    // one. Then the median is at the top of one heap, or halfway between the
    // two tops.
    //
    // addNum must be O(log n) and findMedian O(1). findMedian is never called
    // on an empty stream.

    public void addNum(int x) {
        // TODO
    }

    public double findMedian() {
        // TODO
        return 0;
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
