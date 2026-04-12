import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        double a = 0;
        double b = 0;

        for (int i = 0; i < 20; i++) {
            st = new StringTokenizer(br.readLine());
            String c = st.nextToken();
            double d = Double.parseDouble(st.nextToken());
            String e = st.nextToken();

            if (!e.equals("P")) {
                a += d;
            }
            switch (e) {
                case "A+": b += d * 4.5; break;
                case "A0": b += d * 4.0; break;
                case "B+": b += d * 3.5; break;
                case "B0": b += d * 3.0; break;
                case "C+": b += d * 2.5; break;
                case "C0": b += d * 2.0; break;
                case "D+": b += d * 1.5; break;
                case "D0": b += d; break;
            }
        }
        System.out.println(b / a);
    }
}
