import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] T;
    static long[] pays;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        T = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            T[i] = Integer.parseInt(st.nextToken());
        }

        if (m > 0) {
            pays = new long[n];

            pays[0] = T[0];

            for (int i = 1; i < n; i++) {
                pays[i] = pays[i - 1] + T[i];
                if (i >= m) {
                    pays[i] -= T[i - m];
                }
            }

            Arrays.stream(pays)
                    .max()
                    .ifPresent(System.out::println);
        } else {
            System.out.println(0);
        }
    }
}
