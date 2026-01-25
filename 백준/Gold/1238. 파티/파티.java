import java.io.*;
import java.util.*;

public class Main {
    static int N, M, X;
    static List<List<Node>> graph;
    static List<List<Node>> reverseGraph;

    static class Node {
        int t, w;
        Node (int t, int w) {
            this.t = t;
            this.w = w;
        }
    }

    static int[] dijkstra(int s, List<List<Node>> graph) {
        int[] distance = new int[N];

        for (int i = 0; i < N; i++) {
            distance[i] = Integer.MAX_VALUE;
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.w - o2.w);

        distance[s] = 0;
        pq.add(new Node(s, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();

            if (current.w > distance[current.t]) continue;

            for(Node next : graph.get(current.t)) {
                if(distance[current.t] + next.w < distance[next.t]) {
                    distance[next.t] = distance[current.t] + next.w;
                    pq.add(new Node(next.t, distance[next.t]));
                }
            }
        }

        return distance;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        reverseGraph = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
            reverseGraph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph.get(a - 1).add(new Node(b - 1, w));
            reverseGraph.get(b - 1).add(new Node(a - 1, w));
        }

        int[] distance_to = dijkstra(X - 1, graph);
        int[] distance_from = dijkstra(X - 1, reverseGraph);

        int answer = 0;
        for (int i = 0; i < N; i++) {
            if (distance_to[i] + distance_from[i] > answer) {
                answer = distance_to[i] + distance_from[i];
            }
        }

        System.out.println(answer);
    }
}
