import java.io.*;
import java.util.*;

public class Main {
    static int V, E;
    static int[][] table;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        table = new int[V][V];

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                table[i][j] = 99999999;
            }
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            table[a - 1][b - 1] = c;
        }

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                for (int z = 0; z < V; z++) {
                    table[j][z] = Integer.min(table[j][z], table[j][i] + table[i][z]);
                }
            }
        }

        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < V; i++) {
            answer = Integer.min(answer, table[i][i]);
        }

        if (answer == 99999999) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }
}
