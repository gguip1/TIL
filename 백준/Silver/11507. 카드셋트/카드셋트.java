import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    static String S;
    static boolean[] P = new boolean[13];
    static boolean[] K = new boolean[13];
    static boolean[] H = new boolean[13];
    static boolean[] T = new boolean[13];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine();

        for (int i = 0; i < S.length() / 3; i++) {
            if (S.charAt(i * 3) == 'P') {
                if (P[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1]) {
                    System.out.println("GRESKA");
                    System.exit(0);
                }
                P[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1] = true;
            }

            if (S.charAt(i * 3) == 'K') {
                if (K[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1]) {
                    System.out.println("GRESKA");
                    System.exit(0);
                }
                K[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1] = true;
            }

            if (S.charAt(i * 3) == 'H') {
                if (H[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1]) {
                    System.out.println("GRESKA");
                    System.exit(0);
                }
                H[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1] = true;
            }

            if (S.charAt(i * 3) == 'T') {
                if (T[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1]) {
                    System.out.println("GRESKA");
                    System.exit(0);
                }
                T[Integer.parseInt("" + S.charAt(i * 3 + 1) + S.charAt(i * 3 + 2)) - 1] = true;
            }
        }

        int pCount = 0;
        int kCount = 0;
        int hCount = 0;
        int tCount = 0;

        for (int i = 0; i < 13; i++) {
            if (!P[i]) pCount++;
            if (!K[i]) kCount++;
            if (!H[i]) hCount++;
            if (!T[i]) tCount++;
        }

        System.out.println(pCount + " " + kCount + " " + hCount + " " + tCount);
    }
}
