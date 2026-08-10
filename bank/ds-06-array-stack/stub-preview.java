import java.io.*;
import java.util.*;

interface StackInterface<T> {
    void push(T newEntry);   // add on the top
    T pop();                 // remove and return from the top
    T peek();                // return the top without removing it
    boolean isEmpty();       // true if empty
    int size();              // number of elements
    void clear();            // remove all
}

class ArrayStack<T> implements StackInterface<T> {
    private T[] item;
    private int top;                             // current top index (-1 means empty)
    private boolean integrityOK = false;
    private static final int DEFAULT_CAPACITY = 50;
    private static final int MAX_CAPACITY = 1000000;

    public ArrayStack() {
        this(DEFAULT_CAPACITY);
    }

    @SuppressWarnings("unchecked")
    public ArrayStack(int capacity) {
        if (capacity > MAX_CAPACITY)
            throw new IllegalStateException("capacity exceeds the allowed maximum");
        item = (T[]) new Object[capacity];
        top = -1;
        integrityOK = true;
    }

    // ---- provided ----
    @Override
    public boolean isEmpty() {
        return top < 0;
    }

    @Override
    public int size() {
        return top + 1;
    }

    @Override
    public void clear() {
        checkIntegrity();
        // clear the references to null so the GC can reclaim them
        for (int i = 0; i <= top; i++) item[i] = null;
        top = -1;
    }

    // ==== provided private helpers ====

    private void checkIntegrity() {
        if (!integrityOK)
            throw new SecurityException("the stack was not initialized correctly");
    }

    private void ensureCapacity() {
        if (top == item.length - 1) {            // the array is full
            int newLength = 2 * item.length;
            if (newLength > MAX_CAPACITY)
                throw new IllegalStateException("stack capacity exceeds the allowed maximum");
            item = Arrays.copyOf(item, newLength);   // double it
        }
    }

    // Write the three methods below.
    // Available: item (T[]), top (int, -1 when empty),
    //            checkIntegrity(), ensureCapacity(), isEmpty(), size()
    //
    // pop and peek on an empty stack must throw a RuntimeException.

    @Override
    public void push(T newEntry) {
        // TODO
    }

    @Override
    public T pop() {
        // TODO
        return null;
    }

    @Override
    public T peek() {
        // TODO
        return null;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());

        StackInterface<Integer> stack = new ArrayStack<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "push":
                        stack.push(Integer.parseInt(t.nextToken()));
                        break;
                    case "pop":
                        sb.append(stack.pop()).append('\n');
                        break;
                    case "peek":
                        sb.append(stack.peek()).append('\n');
                        break;
                    case "size":
                        sb.append(stack.size()).append('\n');
                        break;
                    case "empty":
                        sb.append(stack.isEmpty() ? 1 : 0).append('\n');
                        break;
                    case "clear":
                        stack.clear();
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                // reading outside the array is a bug, not an empty stack
                sb.append("crash").append('\n');
            } catch (RuntimeException e) {
                sb.append("empty").append('\n');
            }
        }

        System.out.print(sb);
    }
}
