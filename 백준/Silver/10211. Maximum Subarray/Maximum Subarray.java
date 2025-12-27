import java.io.*;
import java.util.*;
//import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++){
            int N = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] array = new int[N];
            int idx = 0;
            while (st.hasMoreTokens()) {
                array[idx++] = Integer.parseInt(st.nextToken());
            }

            int current_max = array[0];
            int total_max = array[0];

            for(int j = 1; j < N; j++){
                current_max = Math.max(array[j], current_max + array[j]);
                total_max = Math.max(total_max, current_max);
            }

            System.out.println(total_max);
        }
    }
}