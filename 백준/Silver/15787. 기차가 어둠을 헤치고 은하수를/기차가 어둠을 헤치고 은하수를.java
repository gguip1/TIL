import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] trains;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        trains = new int[N];

        int mask = (1 << 20) - 1;

        for (int idx = 0; idx < M; idx++) {
            st = new StringTokenizer(br.readLine());

            int c = Integer.parseInt(st.nextToken());
            int i = Integer.parseInt(st.nextToken());
            int x;

            switch (c) {
                case 1:
                    x = Integer.parseInt(st.nextToken());
                    trains[i - 1] |= 1 << (x - 1);
                    break;
                case 2:
                    x = Integer.parseInt(st.nextToken());
                    trains[i - 1] &= ~(1 << (x - 1));
                    break;
                case 3:
                    trains[i - 1] <<= 1;
                    break;
                case 4:
                    trains[i - 1] >>= 1;
                    break;
            }

            trains[i - 1] &= mask;
        }

        System.out.println(Arrays.stream(trains).distinct().count());
    }
}
