import java.io.*;
import java.util.*;

public class Main {
    static int N, M, X;
    static List<List<Node>> graph;

    static class Node {
        int t, w;
        Node (int t, int w) {
            this.t = t;
            this.w = w;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph.get(a - 1).add(new Node(b - 1, w));
        }

        int answer = 0;

        for (int i = 0; i < N; i++) {
            int[] distance = new int[N];

            for (int j = 0; j < N; j++) {
                if (i != j) distance[j] = Integer.MAX_VALUE;
            }

            PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.w - o2.w);
            pq.add(new Node(i, 0));

            while(!pq.isEmpty()) {
                Node current = pq.poll();

                for (Node next : graph.get(current.t)) {
                    if (distance[current.t] + next.w < distance[next.t]) {
                        distance[next.t] = distance[current.t] + next.w;
                        pq.add(new Node(next.t, distance[next.t]));
                    }
                }
            }

            for (int j = 0; j < N; j++) {
                if (j != X - 1) distance[j] = Integer.MAX_VALUE;
            }

            pq.add(new Node(X - 1, distance[X - 1]));

            while(!pq.isEmpty()) {
                Node current = pq.poll();

                for (Node next : graph.get(current.t)) {
                    if (distance[current.t] + next.w < distance[next.t]) {
                        distance[next.t] = distance[current.t] + next.w;
                        pq.add(new Node(next.t, distance[next.t]));
                    }
                }
            }

            if (distance[i] > answer) {
                answer = distance[i];
            }
        }

        System.out.println(answer);
    }
}
