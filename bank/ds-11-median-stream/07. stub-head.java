import java.io.*;
import java.util.*;

class MedianFinder {

    // The smaller half, largest of them on top.
    protected final PriorityQueue<Integer> lower =
            new PriorityQueue<>(Collections.reverseOrder());

    // The larger half, smallest of them on top.
    protected final PriorityQueue<Integer> upper = new PriorityQueue<>();

    public int size() { return lower.size() + upper.size(); }
