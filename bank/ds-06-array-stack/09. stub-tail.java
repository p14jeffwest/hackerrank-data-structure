
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());

        StackInterface<Integer> stack = new ArrayStack<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "push":
                        stack.push(Integer.parseInt(t.nextToken()));
                        break;
                    case "pop":
                        sb.append(stack.pop()).append('\n');
                        break;
                    case "peek":
                        sb.append(stack.peek()).append('\n');
                        break;
                    case "size":
                        sb.append(stack.size()).append('\n');
                        break;
                    case "empty":
                        sb.append(stack.isEmpty() ? 1 : 0).append('\n');
                        break;
                    case "clear":
                        stack.clear();
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                // reading outside the array is a bug, not an empty stack
                sb.append("crash").append('\n');
            } catch (RuntimeException e) {
                sb.append("empty").append('\n');
            }
        }

        System.out.print(sb);
    }
}
