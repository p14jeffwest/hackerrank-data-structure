import java.io.*;
import java.util.*;

// The ListIterator of 5.4, cut down to the three things this problem needs.
// A cursor sits between elements. next() steps over one element and returns
// it; add() inserts just before the cursor, that is, right after the element
// next() last returned; set() replaces that element.
interface ListCursor<T> {
    boolean hasNext();
    T next();
    void add(T e);
    void set(T e);
}

class LinkedList<T> {
    private Node<T> head;
    private Node<T> tail;
    private int numberOfEntries;

    public LinkedList() {
        head = null;
        tail = null;
        numberOfEntries = 0;
    }

    // ---- index-based access (5.2) ----

    public void add(T newEntry) {                 // append
        Node<T> node = new Node<>(newEntry);
        if (tail == null) {
            head = node;
            tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
        numberOfEntries++;
    }

    public void add(int givenPosition, T newEntry) {
        if (givenPosition < 0 || givenPosition > numberOfEntries)
            throw new IndexOutOfBoundsException("position out of range");
        if (givenPosition == numberOfEntries) { add(newEntry); return; }
        Node<T> node = new Node<>(newEntry);
        if (givenPosition == 0) {
            node.next = head;
            head = node;
        } else {
            Node<T> prev = getNodeAt(givenPosition - 1);
            node.next = prev.next;
            prev.next = node;
        }
        numberOfEntries++;
    }

    public T get(int givenPosition) {
        checkPosition(givenPosition);
        return getNodeAt(givenPosition).data;
    }

    public void set(int givenPosition, T newEntry) {
        checkPosition(givenPosition);
        getNodeAt(givenPosition).data = newEntry;
    }

    public int size() { return numberOfEntries; }

    public boolean isEmpty() { return numberOfEntries == 0; }

    // ---- cursor-based access (5.4) ----

    public ListCursor<T> cursor() {
        return new Cursor();
    }

    private class Cursor implements ListCursor<T> {
        private Node<T> lastReturned = null;
        private Node<T> nextNode = head;

        @Override
        public boolean hasNext() {
            return nextNode != null;
        }

        @Override
        public T next() {
            if (nextNode == null) throw new NoSuchElementException();
            lastReturned = nextNode;
            nextNode = nextNode.next;
            return lastReturned.data;
        }

        @Override
        public void add(T e) {
            Node<T> node = new Node<>(e);
            node.next = nextNode;
            if (lastReturned == null) {       // nothing returned yet: at the front
                head = node;
            } else {
                lastReturned.next = node;
            }
            if (nextNode == null) tail = node;
            lastReturned = node;              // the cursor stays after the new node
            numberOfEntries++;
        }

        @Override
        public void set(T e) {
            if (lastReturned == null) throw new IllegalStateException();
            lastReturned.data = e;
        }
    }

    // ---- printing ----

    @Override
    public String toString() {
        if (head == null) return "(empty)";
        StringBuilder sb = new StringBuilder();
        for (Node<T> current = head; current != null; current = current.next) {
            if (current != head) sb.append(' ');
            sb.append(current.data);
        }
        return sb.toString();
    }

    // ---- private helpers ----

    private void checkPosition(int givenPosition) {
        if (givenPosition < 0 || givenPosition >= numberOfEntries)
            throw new IndexOutOfBoundsException("position out of range");
    }

    private Node<T> getNodeAt(int index) {        // O(n): walks from head
        Node<T> current = head;
        for (int i = 0; i < index; i++)
            current = current.next;
        return current;
    }

    private static class Node<T> {
        T data;
        Node<T> next;
        Node(T data) { this.data = data; this.next = null; }
    }
}

public class Solution {

    // Walk the list once and rewrite it in place:
    //   odd value  -> insert a 0 immediately after it
    //   even value -> replace it with ten times itself
    //
    // Available on the list: size(), get(int), add(int, T), set(int, T),
    //                        and cursor(), which returns a ListCursor<T>.

    public static void transform(LinkedList<Integer> list) {
        // TODO
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());

            LinkedList<Integer> list = new LinkedList<>();
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                list.add(Integer.parseInt(values.nextToken()));
            }

            transform(list);

            sb.append(list).append('\n');
        }

        System.out.print(sb);
    }
}
