import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int s, t;
    static List<List<Node>> abc;

    static class Node {
        int v, w;
        Node (int v, int w) {
            this.v = v;
            this.w = w;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        abc = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            abc.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            abc.get(a - 1).add(new Node(b - 1, c));
            abc.get(b - 1).add(new Node(a - 1, c));
        }

        st = new StringTokenizer(br.readLine());

        s = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());

        int[] weights = new int[n];

        for (int i = 0; i < n; i++) {
            if (i != s - 1) weights[i] = Integer.MAX_VALUE;
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.w - o2.w);

        pq.add(new Node(s - 1, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();

            for (Node next : abc.get(current.v)) {
                if (weights[current.v] + next.w < weights[next.v]) {
                    weights[next.v] = weights[current.v] + next.w;
                    pq.add(new Node(next.v, weights[next.v]));
                }
            }
        }

        System.out.println(weights[t - 1]);
    }
}
