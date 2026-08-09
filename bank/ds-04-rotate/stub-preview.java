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

    // ---- provided: insert at a position ----
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

    // ---- provided: remove at a position ----
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

    // ---- provided: search by value ----
    @Override
    public int indexOf(T anEntry) {
        checkIntegrity();
        for (int i = 0; i < numberOfEntries; i++) {
            if (anEntry.equals(list[i])) return i;
        }
        return -1;
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
}

public class Solution {

    // Return a list holding the elements of `list` rotated k slots right.
    // Available: list.size(), list.get(i), and add(x) on a new Array_List.

    public static ListInterface<Integer> rotate(ListInterface<Integer> list, int k) {
        // TODO
        return list;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            StringTokenizer header = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(header.nextToken());
            int k = Integer.parseInt(header.nextToken());

            ListInterface<Integer> list = new Array_List<>(n);
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                list.add(Integer.parseInt(values.nextToken()));
            }

            ListInterface<Integer> result = rotate(list, k);

            for (int i = 0; i < result.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(result.get(i));
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }
}
