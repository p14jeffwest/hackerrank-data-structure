
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine().trim());

        MinHeap heap = new MinHeap();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            switch (op) {
                case "push":
                    heap.push(Integer.parseInt(t.nextToken()));
                    break;
                case "pop":
                    sb.append(heap.isEmpty() ? "empty" : Integer.toString(heap.pop()))
                      .append('\n');
                    break;
                case "peek":
                    sb.append(heap.isEmpty() ? "empty" : Integer.toString(heap.peek()))
                      .append('\n');
                    break;
                case "size":
                    sb.append(heap.size()).append('\n');
                    break;
                case "print":
                    sb.append(heap).append('\n');
                    break;
                default:
                    break;
            }
        }

        System.out.print(sb);
    }
}
