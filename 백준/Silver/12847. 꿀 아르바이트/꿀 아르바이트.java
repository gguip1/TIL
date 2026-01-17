import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] T;
    static long[] prefixSums;

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
            prefixSums = new long[n];

            prefixSums[0] = T[0];

            for (int i = 1; i < n; i++) {
                prefixSums[i] = prefixSums[i - 1] + T[i];
                if (i >= m) {
                    prefixSums[i] -= T[i - m];
                }
            }

            Arrays.stream(prefixSums)
                    .max()
                    .ifPresent(System.out::println);
        } else {
            System.out.println(0);
        }
    }
}
