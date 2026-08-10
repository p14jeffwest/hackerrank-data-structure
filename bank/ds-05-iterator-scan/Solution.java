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

    // One pass with a cursor.
    //
    // The cursor remembers where it is, so each next() is a single hop from
    // the previous one and each add() re-points two references on the spot.
    // The whole pass is O(n).
    //
    // The index-based route is available and is a trap. get(i), add(i, x) and
    // set(i, x) all walk from head, so a loop over positions costs
    // 1 + 2 + ... + n hops -- O(n^2) -- and cannot finish at this size. That
    // is the point of 5.4: on a linked list the caller must not drive the
    // navigation.
    //
    // Note x % 2 != 0 rather than x % 2 == 1. In Java the remainder keeps the
    // sign of the dividend, so -3 % 2 is -1, and == 1 silently misses every
    // negative odd value.

    public static void transform(LinkedList<Integer> list) {
        ListCursor<Integer> cursor = list.cursor();
        while (cursor.hasNext()) {
            int value = cursor.next();
            if (value % 2 != 0) {
                cursor.add(0);
            } else {
                cursor.set(value * 10);
            }
        }
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
