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

    @Override
    public void push(T newEntry) {
        checkIntegrity();
        ensureCapacity();
        item[++top] = newEntry;
    }

    @Override
    public T pop() {
        checkIntegrity();
        if (isEmpty()) throw new RuntimeException("called pop on an empty stack");
        T result = item[top];
        item[top] = null;
        top--;
        return result;
    }

    @Override
    public T peek() {
        checkIntegrity();
        if (isEmpty()) throw new RuntimeException("called peek on an empty stack");
        return item[top];
    }
}

class StackQueue {

    // A queue built from two stacks and nothing else.
    // `inbox` receives new elements. `outbox` hands them back out.
    private final StackInterface<Integer> inbox = new ArrayStack<>();
    private final StackInterface<Integer> outbox = new ArrayStack<>();

    // Write the three methods below.
    // Available: inbox and outbox, each a StackInterface<Integer> offering
    //            push, pop, peek, isEmpty, size and clear.
    //
    // dequeue on an empty queue must throw a RuntimeException.

    public void enqueue(int x) {
        // TODO
    }

    public int dequeue() {
        // TODO
        return 0;
    }

    public boolean isEmpty() {
        // TODO
        return true;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());

        StackQueue queue = new StackQueue();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "enqueue":
                        queue.enqueue(Integer.parseInt(t.nextToken()));
                        break;
                    case "dequeue":
                        sb.append(queue.dequeue()).append('\n');
                        break;
                    case "empty":
                        sb.append(queue.isEmpty() ? 1 : 0).append('\n');
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                // reading outside an array is a bug, not an empty queue
                sb.append("crash").append('\n');
            } catch (RuntimeException e) {
                sb.append("empty").append('\n');
            }
        }

        System.out.print(sb);
    }
}
