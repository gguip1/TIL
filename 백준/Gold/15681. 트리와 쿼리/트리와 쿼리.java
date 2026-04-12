import java.io.*;
import java.util.*;

public class Main {
    static int N, R, Q;
    static List<List<Integer>> tree;
    static int[] dp;

    static int dfs(int root) {
        dp[root] = 1;

        for (int n : tree.get(root)) {
            if (dp[n] == 0) {
                dp[root] += dfs(n);
            }
        }

        return dp[root];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        tree = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            tree.add(new ArrayList<>());
        }

        dp = new int[N + 1];

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());

            int U = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());

            tree.get(U).add(V);
            tree.get(V).add(U);
        }

        dfs(R);

//        for (int i = 0; i < Q; i++) {
//            int root = Integer.parseInt(br.readLine());
//            System.out.println(dp[root]);
//        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            int root = Integer.parseInt(br.readLine());
            sb.append(dp[root]).append('\n');
        }
        System.out.print(sb);
    }
}
