
    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int n = (int) in.nval;
        int[][] intervals = new int[n][2];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            intervals[i][0] = (int) in.nval;
            in.nextToken();
            intervals[i][1] = (int) in.nval;
        }

        int[][] result = merge(intervals);

        StringBuilder sb = new StringBuilder();
        sb.append(result.length).append('\n');
        for (int[] iv : result) {
            sb.append(iv[0]).append(' ').append(iv[1]).append('\n');
        }

        System.out.print(sb);
    }
}
