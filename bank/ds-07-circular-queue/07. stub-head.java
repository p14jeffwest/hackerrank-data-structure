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
