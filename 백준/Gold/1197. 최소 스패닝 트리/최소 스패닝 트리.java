import java.io.*;
import java.util.*;

public class Main {
    static int V, E;
    static int[] P;
    static Edge[] edges;

    static int find(int a) {
        if (P[a] > 0) {
            return P[a] = find(P[a]);
        }
        return a;
    }

    static boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) {
            return false;
        }
        P[a] = b;
        return true;
    }

    static class Edge{
        int A, B, C;
        public Edge(int A, int B, int C) {
            this.A = A;
            this.B = B;
            this.C = C;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        P = new int[V + 1];
        edges = new Edge[E];

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            edges[i] = new Edge(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(edges, Comparator.comparingInt(e -> e.C));

        int count = 0;
        int answer = 0;

        for (int i = 0; i < E; i++) {
            if (!union(edges[i].A, edges[i].B)) {
                continue;
            }

            answer += edges[i].C;
            count++;
            if (count == V - 1) {
                break;
            }
        }

        System.out.println(answer);
    }
}
