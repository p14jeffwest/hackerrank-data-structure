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

    // Arrays.sort on an array of OBJECTS is a merge sort, and merge sort is
    // stable: two items the comparator calls equal keep the order they were
    // in. So the sign-up order among equal scores is preserved for free --
    // as long as the comparator looks at the score and nothing else. Adding
    // a tie-break on name would destroy exactly the property being asked for.
    //
    // Descending is expressed in the comparator, not by reversing afterwards.
    // Sorting upward and flipping the array would reverse the ties too, and
    // put the last sign-up on a score ahead of the first.
    //
    // (Arrays.sort on an array of PRIMITIVES is a quicksort and is not
    // stable. It makes no difference there, since equal ints are
    // indistinguishable, but it is why the two overloads differ.)
    //
    // The input array is copied, because the caller keeps it.
    //
    // O(n log n).

    static Student[] sortByScore(Student[] students) {
        Student[] result = Arrays.copyOf(students, students.length);
        Arrays.sort(result, (x, y) -> Integer.compare(y.score, x.score));
        return result;
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
