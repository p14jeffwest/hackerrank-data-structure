
    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int n = (int) in.nval;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            a[i] = (int) in.nval;
        }

        in.nextToken();
        int m = (int) in.nval;
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            b[i] = (int) in.nval;
        }

        int[] merged = mergeSorted(a, b);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < merged.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(merged[i]);
        }
        sb.append('\n');

        System.out.print(sb);
    }
}
