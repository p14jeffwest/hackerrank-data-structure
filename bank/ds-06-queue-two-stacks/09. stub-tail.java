
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());

        StackQueue queue = new StackQueue();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "enqueue":
                        queue.enqueue(Integer.parseInt(t.nextToken()));
                        break;
                    case "dequeue":
                        sb.append(queue.dequeue()).append('\n');
                        break;
                    case "empty":
                        sb.append(queue.isEmpty() ? 1 : 0).append('\n');
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                // reading outside an array is a bug, not an empty queue
                sb.append("crash").append('\n');
            } catch (RuntimeException e) {
                sb.append("empty").append('\n');
            }
        }

        System.out.print(sb);
    }
}
