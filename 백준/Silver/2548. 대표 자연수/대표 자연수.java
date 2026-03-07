import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] nums;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        nums = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int value = Integer.MAX_VALUE;
        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            int sum = 0;
            for (int j = 0; j < N; j++) {
                sum += Math.abs(nums[i] - nums[j]);
            }

            if (sum < value) {
                value = sum;
                answer = nums[i];
            } else if (sum == value && nums[i] < answer) {
                answer = nums[i];
            }
        }

        System.out.println(answer);
    }
}
