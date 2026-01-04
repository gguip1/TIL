import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] min_indexes = new int[]{-1, -1};
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < N - 1; i++) {
            int left = i + 1;
            int right = N - 1;
            int mid;

            while (left < right) {
                mid = (left + right) / 2;
                int value = arr[i] + arr[mid];

                if (value < 0) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            if (Math.abs(arr[i] + arr[right]) < min) {
                min = Math.abs(arr[i] + arr[right]);
                min_indexes[0] = i;
                min_indexes[1] = right;
            }

            if (right - 1 >= i + 1) {
                if (Math.abs(arr[i] + arr[right - 1]) < min) {
                    min = Math.abs(arr[i] + arr[right - 1]);
                    min_indexes[0] = i;
                    min_indexes[1] = right - 1;
                }
            }
        }

        System.out.printf("%d %d", arr[min_indexes[0]], arr[min_indexes[1]]);
    }
}
