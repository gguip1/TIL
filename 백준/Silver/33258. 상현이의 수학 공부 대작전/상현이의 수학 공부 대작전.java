import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] A;
    static int L;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        L = Integer.parseInt(br.readLine());

        int s = 1;
        int e = 1_000_000_000;

        while (s < e) {
            int m = (s + e) / 2;
            long v = 0;

            for (int i = 0; i < N; i++) {
                if (m >= A[i]) {
                    v += m;
                } else {
                    v +=  2L * (m - A[i]);
                }
            }

            if (v >= L) {
                e = m;
            } else {
                s = m + 1;
            }
        }

        System.out.println(s);
    }
}
