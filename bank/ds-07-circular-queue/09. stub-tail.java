
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(br.readLine());
        int capacity = Integer.parseInt(header.nextToken());
        int q = Integer.parseInt(header.nextToken());

        CircularQueue<Integer> queue = new CircularQueue<>(capacity);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "enqueue":
                        queue.enqueue(Integer.parseInt(t.nextToken()));
                        break;
                    case "dequeue": {
                        Integer v = queue.dequeue();
                        sb.append(v == null ? "empty" : v.toString()).append('\n');
                        break;
                    }
                    case "front": {
                        Integer v = queue.getFront();
                        sb.append(v == null ? "empty" : v.toString()).append('\n');
                        break;
                    }
                    case "size":
                        sb.append(queue.size()).append('\n');
                        break;
                    case "empty":
                        sb.append(queue.isEmpty() ? 1 : 0).append('\n');
                        break;
                    case "full":
                        sb.append(queue.isFull() ? 1 : 0).append('\n');
                        break;
                    case "clear":
                        queue.clear();
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                // reading outside the array is a bug, not a full queue
                sb.append("crash").append('\n');
            } catch (RuntimeException e) {
                sb.append("full").append('\n');
            }
        }

        System.out.print(sb);
    }
}
