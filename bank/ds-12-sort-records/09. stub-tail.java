
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
