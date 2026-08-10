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

class LinkedList<T> implements ListInterface<T> {
    private Node<T> head;           // first node
    private Node<T> tail;           // last node (end insertion in O(1))
    private int numberOfEntries;

    public LinkedList() {
        head = null;
        tail = null;
        numberOfEntries = 0;
    }

    // ---- provided: add at the end ----
    @Override
    public void add(T newEntry) {
        addLast(newEntry);
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
        if (givenPosition < 0 || givenPosition >= numberOfEntries)
            throw new IndexOutOfBoundsException("position out of range");
        return getNodeAt(givenPosition).data;
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
        head = null;
        tail = null;
        numberOfEntries = 0;
    }

    // ---- provided: prints as [a, b, c] ----
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        Node<T> current = head;
        while (current != null) {
            sb.append(current.data);
            if (current.next != null) sb.append(", ");
            current = current.next;
        }
        return sb.append("]").toString();
    }

    // ==== provided private helpers ====

    // insert at the front
    private void addFirst(T newEntry) {
        Node<T> node = new Node<>(newEntry);
        node.next = head;       // the new node points at the old first node
        head = node;            // move head to the new node
        if (tail == null)       // if the list was empty, set tail too
            tail = head;
        numberOfEntries++;
    }

    // insert at the end (uses tail, so no traversal)
    private void addLast(T newEntry) {
        Node<T> node = new Node<>(newEntry);
        if (tail == null) {     // empty list
            head = node;
            tail = node;
        } else {
            tail.next = node;   // point the current last node's next at the new node
            tail = node;        // update tail
        }
        numberOfEntries++;
    }

    // remove at the front
    private T removeFirst() {
        if (head == null) throw new RuntimeException("empty list");
        T result = head.data;
        head = head.next;
        if (head == null) tail = null;   // if there was one node, tail goes too
        numberOfEntries--;
        return result;
    }

    // returns the node at index (0-based). O(n): it walks from head.
    private Node<T> getNodeAt(int index) {
        Node<T> current = head;
        for (int i = 0; i < index; i++)
            current = current.next;
        return current;
    }

    // ==== inner node class ====
    private static class Node<T> {
        T data;
        Node<T> next;
        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    // add(int, T): three cases. Position 0 and position numberOfEntries are
    //   handed to the provided helpers, which already keep head and tail
    //   right. Everything else splices between prev and prev.next.
    //
    //   The order of the two splice lines matters and cannot be swapped:
    //       node.next = prev.next;   // grab what comes after, first
    //       prev.next = node;        // then re-point prev
    //   Assigning prev.next first throws away the only reference to the rest
    //   of the list, and node.next then points at node itself -- a one-node
    //   cycle that makes toString loop forever.
    //
    // remove(int): relink prev past the target. If the target was the last
    //   node, tail has to move back to prev, or a later addLast will attach
    //   to a node that is no longer in the list.
    //
    // indexOf(T): compare with .equals(), not ==. T is an object type here,
    //   and the JVM caches boxed Integer values in -128..127, so == appears
    //   to work for small numbers and quietly fails for larger ones.

    @Override
    public void add(int givenPosition, T newEntry) {
        if (givenPosition < 0 || givenPosition > numberOfEntries)
            throw new IndexOutOfBoundsException("position out of range");
        if (givenPosition == 0) {
            addFirst(newEntry);
        } else if (givenPosition == numberOfEntries) {
            addLast(newEntry);
        } else {
            Node<T> prev = getNodeAt(givenPosition - 1);
            Node<T> node = new Node<>(newEntry);
            node.next = prev.next;
            prev.next = node;
            numberOfEntries++;
        }
    }

    @Override
    public T remove(int givenPosition) {
        if (givenPosition < 0 || givenPosition >= numberOfEntries)
            throw new IndexOutOfBoundsException("position out of range");
        if (givenPosition == 0) return removeFirst();
        Node<T> prev = getNodeAt(givenPosition - 1);
        Node<T> target = prev.next;
        if (target == tail) tail = prev;
        prev.next = target.next;
        numberOfEntries--;
        return target.data;
    }

    @Override
    public int indexOf(T anEntry) {
        Node<T> current = head;
        int index = 0;
        while (current != null) {
            if (anEntry.equals(current.data)) return index;
            current = current.next;
            index++;
        }
        return -1;
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());

        ListInterface<Integer> list = new LinkedList<>();
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
