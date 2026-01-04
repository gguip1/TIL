import java.io.*;
import java.util.*;

public class Main {
    static List<Integer> list = new ArrayList<>();
    static int N, M;
    static int[] arr;

    static boolean ok(int mid) {
        int value = 0;
        int count = 1;

        for (int i = 0; i < N; i++) {
            if (arr[i] + value > mid) {
                count++;
                value = arr[i];
            } else {
                value += arr[i];
            }
        }

        return count <= M;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = Arrays.stream(arr).max().getAsInt();
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

        System.out.println(left);
    }
}
