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

    // Write the four methods below.
    //
    //   hash(key)         which bucket a key belongs to, using key % size.
    //                     Keys can be NEGATIVE, and % gives a negative result
    //                     for them in Java.
    //   put(key, value)   store the value. If the key is already there,
    //                     replace its value and leave its position alone.
    //   get(key)          the stored value, or -1 if the key is absent.
    //   remove(key)       delete the key and its value. Absent keys change
    //                     nothing.
    //
    // Available: bucketAt(i) for the bucket list, tableSize().

    protected int hash(int key) {
        // TODO
        return 0;
    }

    public void put(int key, int value) {
        // TODO
    }

    public int get(int key) {
        // TODO
        return -1;
    }

    public void remove(int key) {
        // TODO
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(br.readLine());
        int size = Integer.parseInt(header.nextToken());
        int m = Integer.parseInt(header.nextToken());

        HashTable table = new HashTable(size);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            switch (op) {
                case "put":
                    table.put(Integer.parseInt(t.nextToken()),
                              Integer.parseInt(t.nextToken()));
                    break;
                case "get":
                    sb.append(table.get(Integer.parseInt(t.nextToken()))).append('\n');
                    break;
                case "remove":
                    table.remove(Integer.parseInt(t.nextToken()));
                    break;
                case "print":
                    sb.append(table).append('\n');
                    break;
                default:
                    break;
            }
        }

        System.out.print(sb);
    }
}
