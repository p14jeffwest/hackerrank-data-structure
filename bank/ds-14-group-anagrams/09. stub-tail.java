
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        String[] strs = new String[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            strs[i] = st.nextToken();
        }

        List<List<String>> groups = groupAnagrams(strs);

        StringBuilder sb = new StringBuilder();
        sb.append(groups.size()).append('\n');
        for (List<String> group : groups) {
            for (int i = 0; i < group.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(group.get(i));
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }
}
