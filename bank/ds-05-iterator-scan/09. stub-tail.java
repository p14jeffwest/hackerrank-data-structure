
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
