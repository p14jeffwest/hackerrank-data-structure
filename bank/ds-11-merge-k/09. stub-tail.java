
    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int k = (int) in.nval;

        int[][] lists = new int[k][];
        for (int i = 0; i < k; i++) {
            in.nextToken();
            int n = (int) in.nval;
            lists[i] = new int[n];
            for (int j = 0; j < n; j++) {
                in.nextToken();
                lists[i][j] = (int) in.nval;
            }
        }

        int[] merged = mergeKLists(lists);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < merged.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(merged[i]);
        }
        sb.append('\n');

        System.out.print(sb);
    }
}
