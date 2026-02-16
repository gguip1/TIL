import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] X;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = new int[N];

        for (int i = 0; i < N; i++) {
            X[i] = Integer.parseInt(br.readLine());
        }

        int left = 0;
        int right = 1_000_000_001;

        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            long v = 0;

            for (int x : X) {
                if (mid > x) {
                    v += (mid - x);
                }
            }

            if (v <= M) {
                left = mid + 1;
                answer = Math.max(answer, mid);
            } else {
                right = mid - 1;
            }
        }

        System.out.println(answer);
    }
}
