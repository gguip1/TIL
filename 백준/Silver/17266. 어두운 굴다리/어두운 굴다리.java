import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] xs;

    static boolean ok(int mid) {
        if (xs[0] - mid > 0) return false;

        for (int i = 1; i < M; i++) if (xs[i] - xs[i - 1] > 2 * mid) return false;

        return xs[M - 1] + mid >= N;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        M = Integer.parseInt(br.readLine());

        xs = new int[M];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < M; i++) {
            xs[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(xs);

        int left = 0;
        int right = N;
        int mid;

        while (left < right){
            mid = (left + right) / 2;
            if (ok(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(left);
    }
}
