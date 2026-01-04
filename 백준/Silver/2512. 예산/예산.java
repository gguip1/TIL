import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());

        Arrays.sort(arr);

        int left = 0;
        int right = arr[arr.length - 1];
        int mid;

        while (left <= right) {
            mid = (left + right) / 2;

            long sum = 0;

            for (int i = 0; i < N; i++) {
                if (arr[i] < mid) {
                    sum += arr[i];
                } else {
                    sum += mid;
                }
            }

            if (sum <= M) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(right);
    }
}
