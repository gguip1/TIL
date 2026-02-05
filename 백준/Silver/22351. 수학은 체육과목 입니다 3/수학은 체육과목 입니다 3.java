import java.io.*;
import java.util.*;

public class Main {
    static String S;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine();

        for (int i = 1; i < 1000; i++) {
            int num = i;
            int index = 0;

            while (index < S.length()) {
                String numStr = Integer.toString(num);

                if (S.length() < index + numStr.length()) {
                    break;
                }

                if (S.startsWith(numStr, index)) {
                    index += numStr.length();
                    num++;
                } else {
                    break;
                }

                if (index == S.length()) {
                    System.out.println(i + " " + (num - 1));
                    System.exit(0);
                }
            }
        }
    }
}
