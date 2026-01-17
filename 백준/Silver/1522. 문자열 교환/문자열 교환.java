import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int minCnt = Integer.MAX_VALUE;
        int countA = 0;

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == 'a') {
                countA++;
            }
        }

        for (int i = 0; i < str.length(); i++) {
            str = str.substring(1) + str.charAt(0);

            int cnt = 0;
            for (int j = 0; j < countA; j++) {
                if (str.charAt(j) == 'b') {
                    cnt++;
                }
            }

            minCnt = Math.min(minCnt, cnt);
        }

        System.out.println(minCnt);
    }
}
