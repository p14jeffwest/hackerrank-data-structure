
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());

            ListInterface<Integer> list = new Array_List<>(n);
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                list.add(Integer.parseInt(values.nextToken()));
            }

            // snapshot, so that a solution which rearranges the list is caught
            int[] before = new int[n];
            for (int i = 0; i < n; i++) before[i] = list.get(i);

            int answer = majorityElement(list);

            boolean untouched = list.size() == n;
            for (int i = 0; untouched && i < n; i++) {
                untouched = before[i] == list.get(i);
            }

            sb.append(untouched ? Integer.toString(answer) : "modified").append('\n');
        }

        System.out.print(sb);
    }
}
