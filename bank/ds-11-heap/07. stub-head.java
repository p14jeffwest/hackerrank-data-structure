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
