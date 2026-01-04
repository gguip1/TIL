import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] arr;

    static boolean ok(int mid) {
        int K = mid;
        int count = 1;

        for (int i = 0; i < N; i++) {
            if (arr[i] > mid) {
                return false;
            }

            K -= arr[i];

            if (K < 0) {
                count++;
                K = mid - arr[i];
            }
        }

        if (count <= M) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int left = 0;
        int right = Arrays.stream(arr).sum();
        int mid;

        while (left < right) {
            mid = (left + right) / 2;

            if (ok(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(right);
    }
}
