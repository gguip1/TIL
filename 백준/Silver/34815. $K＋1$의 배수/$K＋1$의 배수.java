import java.io.*;
import java.util.*;

public class Main {
    static int N, K;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        if (N % 2 != 0 && N == K) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }
}
