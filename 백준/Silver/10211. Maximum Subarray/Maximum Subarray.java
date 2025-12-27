import java.io.*;
import java.util.*;

public class Main {
    static int[] a;
    static int[] memo;
    static boolean[] vis;

    static int bestEnd(int i) {
        if (vis[i]) return memo[i];
        vis[i] = true;

        if (i == 0) return memo[i] = a[0];
        return memo[i] = Math.max(a[i], a[i] + bestEnd(i - 1));
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            int N = Integer.parseInt(br.readLine());
            a = new int[N];
            memo = new int[N];
            vis = new boolean[N];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) a[i] = Integer.parseInt(st.nextToken());

            int ans = Integer.MIN_VALUE;
            for (int i = 0; i < N; i++) {
                ans = Math.max(ans, bestEnd(i));
            }
            System.out.println(ans);
        }
    }
}
