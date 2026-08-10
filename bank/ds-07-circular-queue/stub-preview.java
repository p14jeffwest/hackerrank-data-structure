import java.io.*;
import java.util.*;

interface QueueInterface<T> {
    void enqueue(T newEntry);   // add at the rear
    T dequeue();                // remove and return the front
    T getFront();               // return the front without removing it
    boolean isEmpty();          // true if empty
    int size();                 // number of elements
    void clear();               // remove all
}

class CircularQueue<T> implements QueueInterface<T> {
    private T[] data;
    private int capacity;
    private int front;     // index of the first element
    private int count;     // current number of elements

    @SuppressWarnings("unchecked")
    public CircularQueue(int capacity) {
        this.capacity = capacity;
        this.data = (T[]) new Object[capacity];
        this.front = 0;
        this.count = 0;
    }

    // ---- provided ----
    @Override
    public boolean isEmpty() { return count == 0; }

    public boolean isFull() { return count == capacity; }

    @Override
    public int size() { return count; }

    @Override
    public void clear() {
        for (int i = 0; i < count; i++)
            data[(front + i) % capacity] = null;
        front = 0;
        count = 0;
    }

    // Write the three methods below.
    // Available: data (T[]), capacity, front, count, isEmpty(), isFull()
    //
    // enqueue on a full queue must throw a RuntimeException.
    // dequeue and getFront on an empty queue must return null.

    @Override
    public void enqueue(T newEntry) {
        // TODO
    }

    @Override
    public T dequeue() {
        // TODO
        return null;
    }

    @Override
    public T getFront() {
        // TODO
        return null;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(br.readLine());
        int capacity = Integer.parseInt(header.nextToken());
        int q = Integer.parseInt(header.nextToken());

        CircularQueue<Integer> queue = new CircularQueue<>(capacity);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "enqueue":
                        queue.enqueue(Integer.parseInt(t.nextToken()));
                        break;
                    case "dequeue": {
                        Integer v = queue.dequeue();
                        sb.append(v == null ? "empty" : v.toString()).append('\n');
                        break;
                    }
                    case "front": {
                        Integer v = queue.getFront();
                        sb.append(v == null ? "empty" : v.toString()).append('\n');
                        break;
                    }
                    case "size":
                        sb.append(queue.size()).append('\n');
                        break;
                    case "empty":
                        sb.append(queue.isEmpty() ? 1 : 0).append('\n');
                        break;
                    case "full":
                        sb.append(queue.isFull() ? 1 : 0).append('\n');
                        break;
                    case "clear":
                        queue.clear();
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                // reading outside the array is a bug, not a full queue
                sb.append("crash").append('\n');
            } catch (RuntimeException e) {
                sb.append("full").append('\n');
            }
        }

        System.out.print(sb);
    }
}
