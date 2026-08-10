import java.io.*;
import java.util.*;

class HashTable {

    // One bucket per slot. A bucket holds {key, value} pairs, in the order
    // they were first put there.
    private final List<List<int[]>> buckets = new ArrayList<>();
    private final int size;

    public HashTable(int size) {
        this.size = size;
        for (int i = 0; i < size; i++) {
            buckets.add(new ArrayList<>());
        }
    }

    // ---- provided ----
    protected List<int[]> bucketAt(int index) { return buckets.get(index); }

    protected int tableSize() { return size; }

    // The contents of every bucket, in order. Used by the `print` command.
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(i).append(':');
            for (int[] entry : buckets.get(i)) {
                sb.append(' ').append(entry[0]).append('=').append(entry[1]);
            }
            if (i < size - 1) sb.append(" |");
        }
        return sb.toString();
    }
