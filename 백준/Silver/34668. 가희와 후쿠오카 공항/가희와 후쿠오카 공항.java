import java.io.*;
import java.util.*;

public class Main {
    static int Q, M;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Q = Integer.parseInt(br.readLine());

        for (int i = 0; i < Q; i++) {
            M = Integer.parseInt(br.readLine());
            int myCount = M / 50;

            int myTime = 6 + (myCount * 12);

            int hh = 6;
            int mm = 0;

            hh += myTime / 60;
            mm += myTime % 60;

            if (hh < 24) {
                System.out.println((hh < 10 ? "0" + hh : hh)  + ":" + (mm < 10 ? "0" + mm : mm));
            } else {
                System.out.println(-1);
            }
        }
    }
}
