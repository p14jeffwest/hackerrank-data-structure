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

    // Write the method below.
    //
    //   sortByScore(students) : the participants ordered from the highest
    //                           score down, with equal scores keeping the
    //                           order they signed up in.
    //
    // `Arrays.sort` on an array of objects takes a Comparator saying which of
    // two items comes first.
    //
    // Sorting upward and then reversing the array is not the same thing.

    static Student[] sortByScore(Student[] students) {
        // TODO
        return new Student[students.length];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        Student[] students = readStudents(br, n);
        Student[] result = sortByScore(students);

        StringBuilder sb = new StringBuilder();
        for (Student s : result) {
            sb.append(s.name).append(' ').append(s.score).append('\n');
        }
        System.out.print(sb);
    }
}
