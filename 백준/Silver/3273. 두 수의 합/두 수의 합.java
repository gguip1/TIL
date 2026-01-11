import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] arr;
    static int x;
    static int answer = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        x = Integer.parseInt(br.readLine());

        Arrays.sort(arr);

        int left = 0;
        int right = n - 1;

        while (left < right) {
            if (arr[left] + arr[right] == x) {
                answer++;
                left++;
            } else if (arr[left] + arr[right] < x) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(answer);
    }
}
