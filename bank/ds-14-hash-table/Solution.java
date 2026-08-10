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

    // Chaining: every slot holds a list, and keys that land on the same slot
    // sit in that list together. A lookup finds the slot in O(1) and then
    // walks its list, so the cost is the length of the chain -- which is why
    // 14.5 cares about the load factor.
    //
    // hash: Java's % returns a NEGATIVE remainder for a negative left
    //   operand -- -7 % 10 is -7, not 3 -- and a negative index throws. Adding
    //   size and taking the remainder again brings it back into range, and
    //   the second % is needed because the first sum can reach size itself.
    //
    // put: an existing key keeps its place in the chain and only its value
    //   changes. Appending a second entry instead would leave two entries for
    //   one key, and which one get() found would depend on the order of the
    //   walk.
    //
    // get: -1 for an absent key, which is what the problem asks for. Note
    //   that a stored value of -1 is then indistinguishable from a miss; that
    //   is the problem's convention, not a property of hash tables.
    //
    // remove: taking the entry out of the list closes the gap, so nothing
    //   else has to move.

    protected int hash(int key) {
        return ((key % tableSize()) + tableSize()) % tableSize();
    }

    public void put(int key, int value) {
        List<int[]> bucket = bucketAt(hash(key));
        for (int[] entry : bucket) {
            if (entry[0] == key) {
                entry[1] = value;              // replace, keeping the position
                return;
            }
        }
        bucket.add(new int[]{key, value});
    }

    public int get(int key) {
        for (int[] entry : bucketAt(hash(key))) {
            if (entry[0] == key) return entry[1];
        }
        return -1;
    }

    public void remove(int key) {
        List<int[]> bucket = bucketAt(hash(key));
        for (int i = 0; i < bucket.size(); i++) {
            if (bucket.get(i)[0] == key) {
                bucket.remove(i);
                return;
            }
        }
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
