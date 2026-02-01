import java.io.*;
import java.util.*;

public class Main {
    static String S;
    static int q;

    static int[][] alphabets;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine();
        q = Integer.parseInt(br.readLine());

        alphabets = new int[26][S.length()];

        for (int i = 0; i < 26; i++) {
            if (S.charAt(0) == 97 + i) {
                alphabets[i][0]++;
            }

            for (int j = 1; j < S.length(); j++) {
                alphabets[i][j] = alphabets[i][j - 1];
                if (S.charAt(j) == 97 + i) {
                    alphabets[i][j]++;
                }
            }
        }

        for (int i = 0; i < q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            String alphabet = st.nextToken();
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            if (l == 0) {
                System.out.println(alphabets[alphabet.charAt(0) % 97][r]);
            } else {
                System.out.println(alphabets[alphabet.charAt(0) % 97][r] - alphabets[alphabet.charAt(0) % 97][l - 1]);
            }
        }
    }
}
