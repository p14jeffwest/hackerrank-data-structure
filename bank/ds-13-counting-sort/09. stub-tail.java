
    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(
                new BufferedInputStream(System.in, 1 << 16));

        int n = nextInt(in);
        int maxValue = nextInt(in);
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = nextInt(in);

        int[] sorted = countingSort(a, maxValue);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < sorted.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(sorted[i]);
        }
        sb.append('\n');

        System.out.print(sb);
    }

    // Reads one non-negative integer. Leave this part unchanged.
    private static int nextInt(DataInputStream in) throws IOException {
        int c = in.read();
        while (c < '0') c = in.read();
        int x = 0;
        while (c >= '0') {
            x = x * 10 + (c - '0');
            c = in.read();
        }
        return x;
    }
}
