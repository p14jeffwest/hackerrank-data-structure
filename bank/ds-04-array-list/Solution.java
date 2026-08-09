import java.io.*;
import java.util.*;

interface ListInterface<T> {
    void add(T newEntry);
    void add(int givenPosition, T newEntry);
    T remove(int givenPosition);
    boolean remove(T anEntry);
    T get(int givenPosition);
    int indexOf(T anEntry);
    int size();
    boolean isEmpty();
    void clear();
}

class Array_List<T> implements ListInterface<T> {
    private T[] list;                               // array storing the elements
    private int numberOfEntries;                    // current number of elements
    private static final int DEFAULT_CAPACITY = 25; // default capacity
    private boolean integrityOK = false;

    public Array_List() {
        this(DEFAULT_CAPACITY);
    }

    @SuppressWarnings("unchecked")
    public Array_List(int desiredCapacity) {
        T[] tempList = (T[]) new Object[desiredCapacity];
        list = tempList;
        numberOfEntries = 0;
        integrityOK = true;
    }

    // ---- provided: add at the end ----
    @Override
    public void add(T newEntry) {
        checkIntegrity();
        ensureCapacity();
        list[numberOfEntries] = newEntry;
        numberOfEntries++;
    }

    // ---- provided: remove by value.
    //      Note that it does no work of its own: it leans entirely on the
    //      indexOf and remove(int) that you are about to write. ----
    @Override
    public boolean remove(T anEntry) {
        int index = indexOf(anEntry);
        if (index < 0) return false;
        remove(index);
        return true;
    }

    // ---- provided: retrieval ----
    @Override
    public T get(int givenPosition) {
        checkIntegrity();
        checkPosition(givenPosition);
        return list[givenPosition];
    }

    @Override
    public int size() {
        return numberOfEntries;
    }

    @Override
    public boolean isEmpty() {
        return numberOfEntries == 0;
    }

    @Override
    public void clear() {
        numberOfEntries = 0;
    }

    // ---- provided: prints as [a, b, c] ----
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < numberOfEntries; i++) {
            sb.append(list[i]);
            if (i < numberOfEntries - 1) sb.append(", ");
        }
        return sb.append("]").toString();
    }

    // ==== provided private helpers ====

    // guards against using an object whose construction did not complete
    private void checkIntegrity() {
        if (!integrityOK) {
            throw new SecurityException("Array_List object is corrupt.");
        }
    }

    // a valid position refers to an existing element: 0 .. numberOfEntries-1
    private void checkPosition(int givenPosition) {
        if (givenPosition < 0 || givenPosition >= numberOfEntries) {
            throw new IndexOutOfBoundsException("Illegal position: " + givenPosition);
        }
    }

    // when the array is full, double its capacity
    private void ensureCapacity() {
        if (numberOfEntries == list.length) {
            list = Arrays.copyOf(list, 2 * list.length);
        }
    }

    // ==== Reference implementation of the three requested methods. ====
    //
    // add(int, T): the shifting loop runs from the BACK toward the front.
    //   Running it from the front would overwrite an element that has not
    //   been moved yet, and every later copy would then duplicate that same
    //   overwritten value.
    //
    // remove(int): after pulling the tail forward, the now-unused last slot
    //   is set to null so the garbage collector can reclaim the object. This
    //   does not change any output, but leaving it out keeps a dead reference
    //   alive inside the array.
    //
    // indexOf(T): comparison uses .equals(), not ==. T is an object type, so
    //   == compares references. With Integer this is the classic trap: the
    //   JVM caches boxed values in -128..127, so == appears to work for small
    //   numbers and silently fails for larger ones.

    @Override
    public void add(int givenPosition, T newEntry) {
        checkIntegrity();
        checkPosition(givenPosition);
        ensureCapacity();
        for (int i = numberOfEntries; i > givenPosition; i--) {
            list[i] = list[i - 1];
        }
        list[givenPosition] = newEntry;
        numberOfEntries++;
    }

    @Override
    public T remove(int givenPosition) {
        checkIntegrity();
        checkPosition(givenPosition);
        T result = list[givenPosition];
        for (int i = givenPosition; i < numberOfEntries - 1; i++) {
            list[i] = list[i + 1];
        }
        list[numberOfEntries - 1] = null;
        numberOfEntries--;
        return result;
    }

    @Override
    public int indexOf(T anEntry) {
        checkIntegrity();
        for (int i = 0; i < numberOfEntries; i++) {
            if (anEntry.equals(list[i])) return i;
        }
        return -1;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());

        ListInterface<Integer> list = new Array_List<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "add":
                        list.add(Integer.parseInt(t.nextToken()));
                        break;
                    case "addAt":
                        list.add(Integer.parseInt(t.nextToken()),
                                 Integer.parseInt(t.nextToken()));
                        break;
                    case "removeAt":
                        sb.append(list.remove(Integer.parseInt(t.nextToken())))
                          .append('\n');
                        break;
                    case "removeValue":
                        sb.append(list.remove((Integer) Integer.parseInt(t.nextToken())) ? 1 : 0)
                          .append('\n');
                        break;
                    case "get":
                        sb.append(list.get(Integer.parseInt(t.nextToken())))
                          .append('\n');
                        break;
                    case "indexOf":
                        sb.append(list.indexOf(Integer.parseInt(t.nextToken())))
                          .append('\n');
                        break;
                    case "size":
                        sb.append(list.size()).append('\n');
                        break;
                    case "print":
                        sb.append(list).append('\n');
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                sb.append("error").append('\n');
            }
        }

        System.out.print(sb);
    }
}
