import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] array = new int[N];
        int idx = 0;
        while(st.hasMoreTokens()) {
            array[idx++] = Integer.parseInt(st.nextToken());
        }

        int[] table = new int[N];

        for (int i = 0; i < N; i++){
            table[i] = 1;
            for (int j = 0; j < i; j++){
                if (array[i] < array[j]){
                    table[i] = Math.max(table[i], table[j] + 1);
                }
            }
        }

        int max = Integer.MIN_VALUE;
        for (int v : table) {
            max = Math.max(max, v);
        }
        System.out.println(max);
    }
}
