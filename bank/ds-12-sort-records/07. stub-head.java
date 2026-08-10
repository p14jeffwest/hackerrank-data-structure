import java.io.*;
import java.util.*;

// A participant. Written as a plain class, not a record: records need Java 16
// and this runs on Java 15.
class Student {
    final String name;
    final int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
}

public class Solution {

    // Reads the participants in the order they signed up.
    // Leave this part unchanged.
    static Student[] readStudents(BufferedReader br, int n) throws IOException {
        Student[] students = new Student[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int score = Integer.parseInt(st.nextToken());
            students[i] = new Student(name, score);
        }
        return students;
    }
