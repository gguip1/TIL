import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] p;

    static int find(int x) {
        while (p[x] >= 0) x = p[x];
        return x;
    }

    static boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) {
            return false;
        }

        if (p[a] > p[b]) {
            int t = a;
            a = b;
            b = t;
        }

        p[a] += p[b];
        p[b] = a;
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        p = new int[n + 1];
        Arrays.fill(p, -1);

        for (int i = 0; i < m; i++) {
            int c, a, b;

            st = new StringTokenizer(br.readLine());

            c = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            if (c == 0) {
                union(a, b);
            } else {
                System.out.println(find(a) == find(b) ? "YES" : "NO");
            }
        }
    }
}
