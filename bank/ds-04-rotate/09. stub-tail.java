
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            StringTokenizer header = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(header.nextToken());
            int k = Integer.parseInt(header.nextToken());

            ListInterface<Integer> list = new Array_List<>(n);
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                list.add(Integer.parseInt(values.nextToken()));
            }

            ListInterface<Integer> result = rotate(list, k);

            for (int i = 0; i < result.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(result.get(i));
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }
}
