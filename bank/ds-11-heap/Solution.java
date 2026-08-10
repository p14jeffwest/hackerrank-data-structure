import java.io.*;
import java.util.*;

class MinHeap {
    // The heap lives in this array, 0-based:
    //   parent of i = (i - 1) / 2,  left of i = 2i + 1,  right of i = 2i + 2
    private final List<Integer> data = new ArrayList<>();

    // ---- provided ----
    public boolean isEmpty() { return data.isEmpty(); }

    public int size() { return data.size(); }

    public int peek() { return data.get(0); }

    public int get(int i) { return data.get(i); }

    public void set(int i, int v) { data.set(i, v); }

    public void addLast(int v) { data.add(v); }

    public int removeLast() { return data.remove(data.size() - 1); }

    public void swap(int i, int j) {
        int t = data.get(i);
        data.set(i, data.get(j));
        data.set(j, t);
    }

    public int parent(int i) { return (i - 1) / 2; }

    public int left(int i) { return 2 * i + 1; }

    public int right(int i) { return 2 * i + 2; }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < data.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(data.get(i));
        }
        return sb.toString();
    }

    // push: put the value at the end, which keeps the shape a complete binary
    //   tree but may break the order, then walk it up while it is smaller
    //   than its parent. It stops at the root or as soon as the parent is
    //   smaller, so it climbs at most the height.
    //
    // pop: the root is the answer. Detach the LAST value and move it into the
    //   root, which again keeps the shape and breaks the order, then walk it
    //   down, always swapping with the SMALLER of the two children. Swapping
    //   with the larger one would put the larger above the smaller and leave
    //   the heap broken.
    //
    //   Removing the last value before overwriting the root matters when the
    //   heap holds one element: there is then nothing to move down.
    //
    // Both are O(log n): the value travels the height of the tree and no
    // further.

    public void push(int x) {
        addLast(x);
        int i = size() - 1;
        while (i > 0) {
            int p = parent(i);
            if (get(i) < get(p)) {
                swap(i, p);
                i = p;
            } else {
                break;
            }
        }
    }

    public int pop() {
        int top = get(0);
        int last = removeLast();
        if (!isEmpty()) {
            set(0, last);
            int i = 0, n = size();
            while (true) {
                int l = left(i), r = right(i), smallest = i;
                if (l < n && get(l) < get(smallest)) smallest = l;
                if (r < n && get(r) < get(smallest)) smallest = r;
                if (smallest == i) break;
                swap(i, smallest);
                i = smallest;
            }
        }
        return top;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine().trim());

        MinHeap heap = new MinHeap();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            switch (op) {
                case "push":
                    heap.push(Integer.parseInt(t.nextToken()));
                    break;
                case "pop":
                    sb.append(heap.isEmpty() ? "empty" : Integer.toString(heap.pop()))
                      .append('\n');
                    break;
                case "peek":
                    sb.append(heap.isEmpty() ? "empty" : Integer.toString(heap.peek()))
                      .append('\n');
                    break;
                case "size":
                    sb.append(heap.size()).append('\n');
                    break;
                case "print":
                    sb.append(heap).append('\n');
                    break;
                default:
                    break;
            }
        }

        System.out.print(sb);
    }
}
